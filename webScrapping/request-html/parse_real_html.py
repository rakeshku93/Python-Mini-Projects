from requests_html import HTML, HTMLSession
import csv

csv_file = open("cms_scrape.csv", "w", newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["headline", "summary", "video"])


session = HTMLSession()
r = session.get("https://coreyms.com/")

# create same obj as html = HTML(html=source)
html = r.html

# get the HTML contents
# print(html.html)

# get the text contents
# print(html.text)

# # get the article.html and save to .html thus we don't have to look into the chrome.
# article = html.find("article", first=True)
# # print(article.html)

# headline = article.find(".entry-title-link", first=True)
# print(headline.text)

# summary = article.find('.entry-content p', first=True)
# print(summary.text)

# vid_src = article.find("iframe", first=True)
# vid_src_embedded_url = vid_src.attrs["src"]  #  .attrs method makes the containet in python dict
# # vid_src_url is embedded URL. So, need to do some preprpcessing
# vid_id = vid_src_embedded_url.split("/")[-1].split("?")[0]
# yt_link = f"https://youtube.com/watch?v={vid_id}"
# print(yt_link)

#  to parse all the articles
articles= html.find("article")

for article in articles:
    headline = article.find(".entry-title-link", first=True).text
    print(headline)

    summary = article.find('.entry-content p', first=True).text
    print(summary)
    
    try:
        vid_src = article.find("iframe", first=True)
        vid_src_embedded_url = vid_src.attrs["src"]  #  .attrs method makes the containet in python dict
        # vid_src_url is embedded URL. So, need to do some preprocessing to fetch the video-id
        vid_id = vid_src_embedded_url.split("/")[-1].split("?")[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}"
        print(yt_link)
    except Exception as e:
        yt_link = None
        
    csv_writer.writerow([headline, summary, yt_link])
    
csv_file.close()