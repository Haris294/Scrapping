from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq

url = 'https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as'

client = uReq(url)
page_html = client.read()
client.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div", {"class":"_3O0U0u"})
container = containers[0]
print(container.div.img["alt"])

price = container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
print(price[0].text)

ratings = container.findAll("div",{"class":"niH0FQ"})
print (ratings[0].text)
