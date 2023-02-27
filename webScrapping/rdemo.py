
import requests

try:
    request = requests.get("https://xkcd.com/353/")
    print(request)
    request.raise_for_status()  # None if page exists
    
    # # view methods of this request instance
    # print(dir(request))
    
    # # get details of requests instance methods
    # print(help(request))
    
    
    
except Exception as e:
    print(str(e))
    
    
    
