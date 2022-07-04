import time
from selenium import webdriver
import os
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
img = []
rating = []
compname = []
linksok = []
productname = []
company_name = []
productlinks = []
image_url = []
price = []
productUrl = []
productname = []
listprodname = []
listcompname= []
listprice = []
listrate = []
listurl = []
listimgurl = []
missinglink = "https://www.jumia.com.eg"
html_text = requests.get(f"https://www.jumia.com.eg/catalog/?q=shoes").text
src = html_text
soup = BeautifulSoup(src, "lxml")
products = soup.find_all("div", {"class" : "-paxs row _no-g _4cl-3cm-shs"})
products_names = soup.find_all("h3", {"class" : "name"})
compsnames = soup.find_all("svg", {"class" : "ic xprss"})
imageslinks = soup.find_all("div", {"class" : "img-c"})
productsPrice = soup.find_all("div", {"class" : "prc"})
links = soup.find("a", {"class" : "core"})
linksok = links.get("href")

url = (missinglink + linksok)

i=0
links = soup.find_all("article", {"class" : "prd _fb col c-prd"})
for productlink in links:
    image_url = imageslinks[i].find("img").attrs["data-src"]
    img.append(image_url)
    productname.append(products_names[i].text)
    price.append(productsPrice[i].text)
    page = productlink.find("a", {"class": "core"})
    urlss = missinglink + page.get("href")
    productUrl.append(urlss)
    codesource = requests.get(urlss).text
    sourcecode = codesource
    soup2 = BeautifulSoup(sourcecode, "lxml")
    ratenn = soup2.find("div",{"class": "stars _s _al"}).text
    rating.append(ratenn)
    print(rating)
    complink = soup2.find("div", {"class" : "-hr -pas"})
    comp = complink.find("p", {"class": "-m -pbs"}).text
    compname.append(comp)
    print(compname)
    i = i + 1
    print("product: " , productname,"   price: " , price,"    company: " , compname,"   rate:     " , rate)
    print(image_url)
    print(productUrl)

file_list = [productname, price , img, compname, productUrl, rating]
exported = zip_longest(*file_list)
with open ("projectTest.csv", "w", encoding="utf-8") as myfile:
 wr = csv.writer(myfile)
 wr.writerow(["Product Name", "Product Price", "Product Image", "Company Name", "Links" , "Rating"])
 wr.writerows(exported)
