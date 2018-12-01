from lxml import html, etree
import requests
import sys


def getWordList(parentNode):
    if len(parentNode) > 0:
        words = ','.join(parentNode[0].itertext()).split(',')
        return [x for x in words if x.strip() != '']
    return None


srchWord = sys.argv[1]
urlThesaurus = 'http://dic.daum.net/search.do?q=%s&dic=kor' % srchWord
print(urlThesaurus)
synSelector = "//div[@id='relatedQuery']/ul"
page = requests.get(urlThesaurus)
tree = html.fromstring(page.content)
syns = tree.xpath(synSelector)
synonyms = getWordList(syns)
print(synonyms)
