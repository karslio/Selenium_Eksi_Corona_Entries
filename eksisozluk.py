from selenium import webdriver
import random
import time

browser = webdriver.Chrome()

url = "https://eksisozluk.com/corona-virusu-sayesinde-fark-edilen-gercekler--6435737?p="

pageCount = 1
entries = []
entryCount = 1
while pageCount <=3:
    newUrl = url + str(pageCount)
    browser.get(newUrl)
    elements =browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount +=1

with open ("entries.txt" , "w" ,encoding = "UTF-8") as file: 
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry +"\n")
        file.write("******************************************\n")
        entryCount +=1
   
browser.close()



     
