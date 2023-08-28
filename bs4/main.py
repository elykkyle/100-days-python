import re

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.find(name="a").text)
    article_links.append(article.find(name="a")["href"])

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(class_="score")]



# scores = soup.find_all(class_="score")
# for score in scores:
#     article_upvotes.append(score.getText().split(" ")[0])

article_links = [link for link in article_links if not re.match("^item.", link)]
print(article_texts)
print(article_links)
print(article_upvotes)
largest_idx = article_upvotes.index(max(article_upvotes))
print(largest_idx)

print(article_texts[largest_idx])
print(article_links[largest_idx])
print(article_upvotes[largest_idx])


# with open("website.html") as website_file:
#     contents = website_file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.li)
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#     pass
#
# heading = soup.find(name="h1", id="name")
# # print(heading.getText())
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)