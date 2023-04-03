# 
import os
import requests
from bs4 import BeautifulSoup

with open("simple.html") as html_file:
    soup = BeautifulSoup(html_file, "lxml")

# get the contents in HTML format 
# print(soup)

# get the contents in HTML format with proper indentation
# print(soup.prettify())

# get the title of the page
# title = soup.find("title").text
# print(title)

# parsing one article
# site_title = soup.find("h1").text
# print(site_title)

# article = soup.find("div", class_="article")
# # print(article)


# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)

# parse all articles
for article in soup.find_all("div", class_="article"):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    print()