import requests
from bs4 import BeautifulSoup

url = "https://jobs.github.com/positions?description=Python"

r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")

for i in s.find_all("tr",class_="job"):
    print("Position : ",i.td.h4.a.text)
    print("Description : ",i.td.h4.a.attrs['href'])
    print("Company Name : ",i.find("a",class_="company").text)
    
    print("Company URL : ",i.find("a",class_="company").attrs['href'])
    
    print("Job Type : ",i.find("strong").text)
    
    print("Location : ",i.find("span",class_="location").text,"\n")