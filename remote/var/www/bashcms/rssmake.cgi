#!/bin/bash -xv
dir=$(dirname $0)
tmp=/tmp/$$

export url="http://$SERVER_NAME"

ls -f $dir/pages/        |
grep -E "^[0-9]{14}_"    |
head -n 10               |
sort -r                  |
xargs -n 1 $dir/bin/rssitem > $tmp-items

cat << FIN > $dir/rss/rss20.xml
<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>bashCMSブログ</title>
        <link>$url</link>
        <description>bashCMS作ってます。</description>
$(sed 's/^/\t\t/' $tmp-items)
    </channel>
</rss>
FIN

echo "Content-Type: text/html"
echo

rm -f $tmp-*
