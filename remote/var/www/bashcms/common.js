window.onload = function () {
    lastArticles(10);
    pvRanking(10);
    fullSearch("");
}

function lastArticles(num){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("last-articles").innerHTML = httpReq.responseText;
    }
    var url = "/ajax/last_articles.cgi?num=" + num;
    httpReq.open("GET",url,true);
    httpReq.send(null);
}

/* タグ検索 */
function categorySearch(word){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("article").innerHTML = httpReq.responseText;
    }
    var url = "/ajax/categories.cgi?word=" + encodeURIComponent(word);
    httpReq.open("GET",url,true);
    httpReq.send(null);
}

/* 全文検索 */
function fullSearch(word){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("full-search").innerHTML = httpReq.responseText;
        document.body.style.cursor = "default";
    }
    var url = "/ajax/full_search.cgi?word=" + encodeURIComponent(word);
    httpReq.open("GET",url,true);
    httpReq.send(null);
    document.body.style.cursor = "wait";
}

/* ランキング */
function pvRanking(num){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("pv-ranking").innerHTML = httpReq.responseText;
    }
    var url = "/ajax/pv_ranking.cgi?num=" + encodeURIComponent(num);
    httpReq.open("GET",url,true);
    httpReq.send(null);
}
