from lxml import html, etree
import requests
import sys


def getWordList(parentNode):
    if len(parentNode) > 0:
        return ','.join(parentNode[0].itertext()).split(',')
    return None


srchWord = sys.argv[1]
urlThesaurus = 'https://www.thesaurus.com/browse/%s?s=t' % srchWord
print(urlThesaurus)
synSelector = "//section[contains(@class, 'synonyms-container')]/ul"
antonSelector = "//section[contains(@class, 'antonyms-container')]/ul"
page = requests.get(urlThesaurus)
tree = html.fromstring(page.content)
syns = tree.xpath(synSelector)
ants = tree.xpath(antonSelector)
print(ants)
synonyms = getWordList(syns)
anonyms = getWordList(ants)
print(synonyms)
print(anonyms)
