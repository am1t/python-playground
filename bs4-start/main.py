from bs4 import BeautifulSoup
import requests

toparticles = []

hackernewshtml = requests.get("https://news.ycombinator.com")

newssoup = BeautifulSoup(hackernewshtml.text, "html.parser")

for title in newssoup.select(".titleline")[:10]:
    article = {}
    article["heading"] = title.text
    article["link"] =  title.select("a")[0].get("href")
    toparticles.append(article)

cur_count = 0
for score in newssoup.select(".score")[:10]:
    toparticles[cur_count]["score"] = int(score.getText().split()[0])
    cur_count += 1

print(toparticles)

high_score_article = {}
max = 0
for article in toparticles:
    if article["score"] > max:
        high_score_article = article
        max = article["score"]

print(high_score_article)

