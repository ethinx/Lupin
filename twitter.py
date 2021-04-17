import urllib
import requests
import json
import re

from bs4 import BeautifulSoup

def LogTwitterUrl(url):
    api = 'https://publish.twitter.com/oembed?url={}'.format(url)
    req = requests.get(api)

    data = json.loads(req.text)

    print(data['html'])

    soup = BeautifulSoup(data['html'], 'html.parser')

    tweet = soup.p.get_text()

    regexUser = re.search("http[s]://twitter.com/(\S+)/status", url)
    if regexUser:
        user = regexUser.group(1)

    logseqEntry = "[{}]({}) - [[@{}]]".format(tweet, url, user)

    # print(logseqEntry)
    return logseqEntry


if __name__ == '__main__':
    LogTwitterUrl("https://twitter.com/laixintao/status/1383070858889990148?s=20")
