import os
import csv
import requests
from bs4 import BeautifulSoup

csv_file = open("./cms_scrapper.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["headline", "summary", "yt_video_link"])

source = requests.get("https://coreyms.com/").text
soup = BeautifulSoup(source, "lxml")

# print(soup.prettify())

for article in soup.find_all("article"):
    headline = article.h2.a.text
    print(headline)

    summary = article.find("div", class_="entry-content").p.text
    print(summary)

    try:

        vid_src = article.find("iframe", class_="youtube-player")["src"]
        vid_id = vid_src.split("/")[4].split("?")[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}"
        print(yt_link)
        print()
    except Exception as e:
        yt_link = None
        
    csv_writer.writerow([headline, summary, yt_link])
    
csv_file.close()
        

        