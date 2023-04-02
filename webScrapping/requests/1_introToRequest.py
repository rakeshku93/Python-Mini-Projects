"""This is introduction to request library. Discussioning the import methods of request library"""

# import libraries
import requests

try:
    request = requests.get("https://xkcd.com/353/")
    print(request)
    
    # Status True/False
    print(request.ok)
    
    # None if page exists
    print(request.raise_for_status())  
    
    # See the header details of request
    print(request.headers)
    
    # view methods of this request instance
    print(dir(request))
    
    # get details of requests instance methods
    print(help(request))
    
    # get the content of response in unicode(use for text)
    print(request.text)
    
    # get the content of response in bytes(use for images)
    r = requests.get("https://imgs.xkcd.com/comics/python.png")
    with open("./logs/comic.png", "wb") as f:
        f.write(r.content)
    
except Exception as e:
    print(str(e))
    
    
    
