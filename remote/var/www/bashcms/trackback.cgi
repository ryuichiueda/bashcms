#!/bin/bash -xv
dir=$(dirname $0)
exec 2> $dir/../www-data/$(basename $0).$(date +%Y%m%d%H%M%S).$$

ERROR (){
	HTTPSEND 1
	exit 1
}

HTTPSEND (){
	cat <<- FIN
	Content-Type: text/html

	<?xml version="1.0" encoding="iso-8859-1"?>
	<response>
	<error>$1</error>
	</response>
FIN
}

#GETの文字列から記事ディレクトリ名を得る
page=$(echo ${QUERY_STRING} | tr -dc 'a-zA-Z0-9_=' | grep '^p=' | sed 's/^p=//')
#チェック
[ "$page" = "" ]          && ERROR
[ -d "$dir/pages/$page" ] || ERROR

#リクエストにIDをつける
id=$(date +%Y%m%d%H%M%S)_$(maezero 1.6 <<< $$)
#リクエストファイルに追記
echo "$id" "$page" >> $dir/trackback/request
#受信内容を保存
dd bs=${CONTENT_LENGTH} > "$dir/trackback/$id.$page"

HTTPSEND 0

cat << FIN | mail -s '[bashCMS] trackback request' mail@address
許可する：
ssh $HTTP_HOST 'echo "$id" "$page" OK >> $dir/trackback/accept'

許可しない：
ssh $HTTP_HOST 'echo "$id" "$page" NG >> $dir/trackback/accept'

リクエスト内容：
$(nkf --url-input "$dir/trackback/$id.$page" | sed 's/\&/\n/g' | tr -d '><"')
FIN
