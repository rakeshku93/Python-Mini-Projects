"""This is sample script, to get accustomed with requests-html"""

# 
from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

# get the HTML contents
# print(html.html)

# get the text contents
# print(html.text) 

# find returns list of values
# match = html.find(selector="title")
# print(match[0].text)

# get the article under div
article = html.find(selector="div.article", first=True) # first=True return the 1st match
headline = article.find("h2", first=True)
summary = article.find("p", first=True)
# print(headline.text)
# print(summary.text)


# now let's parse all articles at once
articles = html.find(selector="div.article", first=False)
# print(articles.text)

headlines = []
summaries = []
for article in articles:
    headline = article.find("h2", first=True).text
    summary = article.find("p", first=True).text

    headlines.append(headline)
    summaries.append(summary)
    
print(headlines)
print(summaries)