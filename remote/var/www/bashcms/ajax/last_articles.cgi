#!/bin/bash -xv
dir=$(dirname $0)/..
pages=$dir/pages
tmp=/tmp/$$
exec 2> $dir/../www-data/$(basename $0).$(date +%Y%m%d%H%M%S).$$

num=$(tr -dc '0-9' <<< ${QUERY_STRING})
[ -z "$num" ] && num=0

#返信するHTML片のテンプレート
cat << FIN > $tmp-html
<h1>最新記事</h1>
LIST
    <div><a href="?p=%2">%3 (%1)</a></div>
LIST
FIN

echo "Content-Type: text/html"
echo
ls -f $pages                      |
grep -E '^[0-9]{14}_'             |
sort -r                           |
head -n "$num"                    |
xargs -i@ cat $dir/cache/@.title  |
# 投稿日付をつけるため、ディレクトリから日時をとりわけ
self 1.1.14 1 2                   |
dayslash "m月d日" 1               |
mojihame -lLIST $tmp-html -

rm $tmp-*
