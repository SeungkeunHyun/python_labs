from lxml import html, etree
import requests
from pprint import pprint
from urllib.parse import urlparse, parse_qs
from elasticsearch import Elasticsearch
import re


def fetchContent(item, xp):
    page = requests.get(item['url'])
    dom = html.fromstring(page.content)
    if len(dom.xpath(xp)) == 0:
        return ''
    iterText = dom.xpath(xp)[0].itertext()
    txt = ''
    mainStarted = False
    item['provider'] = dom.xpath(
        "//div[@class='press_logo']//a/img")[0].get('title')
    for t in iterText:
        if mainStarted:
            txt += t
        if not mainStarted:
            mainStarted = 'function' in t
    item['text'] = re.sub(r'["]{2}', '', txt.strip())
    print('extracted text: ' + txt)
    dom = page = None
    return txt


def gatherComments(curl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    cpage = requests.get(curl, headers=headers, timeout=2)
    print(cpage.content.decode(encoding='euc-kr'))
    cpageDOM = html.fromstring(cpage.content)
    cmtLis = cpageDOM.xpath(".//ul[@class='u_cbox_list']/li")
    print(cmtLis)
    comments = list()
    for cmt in cmtLis:
        comment = {}
        comment['nick'] = cmt.xpath(".//span[@class='u_cbox_nick']/text()")[0]
        comment['text'] = cmt.xpath(
            ".//span[@class='u_cbox_contents']/text()")[0]
        comment['agree'] = cmt.xpath(
            ".//em[@class='u_cbox_cnt_recomm']/text()")[0]
        comment['disagree'] = cmt.xpath(
            ".//em[@class='u_cbox_cnt_unrecomm']/text()")[0]
        comments.append(comment)
        cpage = cpageDOM = None
    return comments


pageUrl = "https://news.naver.com"
page = requests.get(pageUrl)
pageDOM = html.fromstring(page.content.decode("euc-kr"))
lsts = pageDOM.xpath("//ul[@class='newsnow_txarea']")
es = Elasticsearch(hosts="localhost:9200")
idx = "naver.news.now"
for lst in lsts:
    articles = lst.xpath("//li/div[@class='newsnow_tx_inner']")
    for article in articles:
        item = {}
        item['url'] = article.xpath("./a")[0].get('href')
        item['title'] = article.xpath(".//strong/text()")[0]
        item['article_id'] = urlparse(item['url']).query
        item['queryParams'] = parse_qs(urlparse(item['url']).query)
        if 'oid' not in item['queryParams']:
            continue
        fetchContent(item, "//div[@id='articleBodyContents']")
        pprint(item)
        res = es.index(index=idx, doc_type='_doc',
                       id=item['article_id'], body=item)
        cmtUrl = "https://news.naver.com/main/read.nhn?m_view=1&includeAllCount=false&" + \
            item['article_id']
        print(cmtUrl)
        print(res)
        comments = gatherComments(cmtUrl)
        pprint(comments)
