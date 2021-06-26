from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time 
import csv
start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(start_url)
time.sleep(10)
def scrap():
    headers=["NAME","Distance","Mass"," Radius"]
    planet_data=[]
    for i in range(0,443):
        soups=BeautifulSoup(browser.page_source,"html.parser")
        for th_tag in soups.find_all("ul",attrs={"class","exoplanet"}):
            tr_tags=th_tag.find_all("li")
            temp_list=[]
            for index,tr_tag in enumerate(tr_tags):
                if index==0:
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper.csv","w") as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)
scrap()