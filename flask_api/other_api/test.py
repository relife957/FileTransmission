import urllib.parse
encoded_url = "1627406006/%E5%85%B4%E9%AB%98%E9%87%87%E7%83%88"

url = urllib.parse.unquote(encoded_url,'utf-8')
print(url)