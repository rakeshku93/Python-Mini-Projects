import requests


payload = {"page": 2, "count": 25}
r = requests.get("https://httpbin.org/get", params=payload)

print(f"url={r.url}")
print(r.ok)
print(r.status_code)
print(r.text)