#Program to extract Title of a webpage


from bs4 import BeautifulSoup
import requests
url = "http://www.google.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)