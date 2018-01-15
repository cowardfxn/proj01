#!/bin/python3
# encoding: utf-8


import urllib.request as request
import feedparser
import ssl


def get_https_feed(rss_src):
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    context = ssl._create_unverified_context()

    with request.urlopen(rss_src, context=context) as req:
        cont = req.read()

    return feedparser.parse(cont)


if __name__ == '__main__':
    feed1 = 'https://www.apple.com/newsroom/rss-feed.rss'
    feed2 = 'https://venturebeat.com/tag/500-startups/feed/'
    d1 = get_https_feed(feed2)
    print(d1.feed.title)
    print(d1.feed.links)


import string
from random import choice, randint

chars = string.ascii_letters

values = []
for i in range(20):
    l = []
    for i in range(randint(6, 17)):
        l.append(choice(chars))
    values.append(l)


from pymongo import MongoClient
import os.path

cli = MongoClient()
db = cli['radar']

invalid_urls = []
with db.url_status.find({"invalid": True}) as cur1:
    with open(os.path.expanduser("~/Desktop/invalid-urls.txt"), "w") as ofs:
        for rec in cur1:
            invalid_urls.append(rec.get('url'))
            ofs.write(rec.get("url") + '\n')



with db.url_status.find().sort([("invalid", -1), ("url", 1)]) as cur1:
    with open(os.path.expanduser("~/Desktop/invalid-urls1.txt"), "w") as ofs:
        for rec in cur1:
            ofs.write("{}\t{}".format(rec.get('url'), rec.get("invalid") and "invalid" or "valid") + '\n')

