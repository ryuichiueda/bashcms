#!/bin/bash -xv
dir=$(dirname $0)/..
pages=$dir/pages
tmp=/tmp/$$
exec 2> $dir/../www-data/$(basename $0).$(date +%Y%m%d%H%M%S).$$

num=$(tr -dc '0-9' <<< ${QUERY_STRING})
[ -z "$num" ] && num=0

#返信するHTML片のテンプレート
cat << FIN > $tmp-html
<h1>人気記事</h1>
LIST
<div><a href="/?p=%2">%3 (%1PVs)</a></div>
LIST
FIN

echo "Content-Type: text/html"
echo
ls -lU "$dir/cache/"                    |
grep '\.counter$'                       |
awk '{print $5,$NF}'                    |
#1:pv 2:カウンタファイル名
sed 's;\.counter$;.title;'              |
#1:pv 2:タイトルのキャッシュファイル名
sort -k1,1nr                            |
head -n "$num"                          |
while read n f ; do
    echo "$n" $(cat "$dir/cache/$f")
done                                    |
#1:pv 2:記事ディレクトリ名 3:タイトル
mojihame -lLIST $tmp-html -

rm $tmp-*
