"""The requests module lets you easily download files from the web using requests.get() Function"""

import requests

try:
    request = requests.get('https://inventwithpython.com/page_that_does_not_exist')
    request.raise_for_status()   # 404: Page not Found
                                 # 200: Success   
except Exception as e:
    print(f"There was a problem: {str(e)}")
    