#!/bin/bash -xv
dir=$(dirname $0)/..
pages=$dir/pages
tmp=/tmp/$$
exec 2> $dir/../www-data/$(basename $0).$(date +%Y%m%d%H%M%S).$$

word=$(nkf --url-input <<< ${QUERY_STRING} | sed 's/^word=//')
numchar=$(numchar <<< "$word")

#返信するHTML片のテンプレート
cat << FIN > $tmp-html
<h1>カテゴリー: $numchar</h1>
LIST
<div><a href="/?p=%1">%2</a></div>
LIST
FIN

echo "Content-Type: text/html"
echo
find "$pages" -name categories          |
xargs grep -l -- "$word"                |
sed 's;.*/pages/\(.*\)/categories;\1;'  |
xargs -i@ cat $dir/cache/@.title        |
mojihame -lLIST $tmp-html -

rm $tmp-*
