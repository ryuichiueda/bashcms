#!/bin/bash -xv
dir=$(dirname $0)/..
pages=$dir/pages
tmp=/tmp/$$
exec 2> $dir/../www-data/$(basename $0).$(date +%Y%m%d%H%M%S).$$

word=$(nkf --url-input <<< ${QUERY_STRING} | sed 's/^word=//')
numchar=$(numchar <<< "$word")

#返信するHTML片のテンプレート
cat << FIN > $tmp-html
<h1>サイト内全文検索</h1>
<input type="text" id="full-search-box" value="$numchar" />
<button onclick="fullSearch(
    document.getElementById('full-search-box').value)" >検索</button>
LIST
<div><a href="/?p=%1">%2</a></div>
LIST
FIN

echo "Content-Type: text/html"
echo
if [ -z "$word" ] ; then
    echo | mojihame -lLIST $tmp-html -
else
    find "$dir/pages"                                         |
    grep '/html$'                                             |
    xargs grep -lF -- "$word"                                 |
    sort -r                                                   |
    awk -F"/" -v d="$dir/cache/" '{print d $(NF-1) ".title"}' |
    xargs cat                                                 |
    mojihame -lLIST $tmp-html -
fi

rm $tmp-*
