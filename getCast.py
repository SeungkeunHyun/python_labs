from lxml import html, etree
import requests

pageNumber = 1
hasNext = True
while hasNext:
    urlToScrap = "https://www.podty.me/cast/177643/episodes?page=%d&dir=desc" % pageNumber
    print(urlToScrap)
    page = requests.get(urlToScrap)
    tree = html.fromstring(page.content)
    if pageNumber == 1:
        title = tree.xpath(
            '//*[@id="container"]/section/div[2]/div[1]/p')[0].text
        fname = title + ".txt"
        print(title)
    episodes = tree.xpath('//*[@id = "episodes"]/div[3]/ul/li')
    for ep in episodes:
        print(ep.get('data-episode-name'))
        print('\t' + ep.get('data-play-uri'))
    hasNext = False #len(tree.xpath('//a[@class="btnNext"]')) > 0
    if hasNext:
        pageNumber += 1
        print('go to next page')
    else:
        break