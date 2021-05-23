from selenium import webdriver
import time
import os
from datetime import date
from selenium.webdriver.common.keys import Keys
from scrape_table import scrape_table
from return_dates import return_dates



#Open the link
browser = webdriver.Chrome('chromedriver.exe')
browser.maximize_window()
browser.get("https://www.sharesansar.com/today-share-price")

#Select Commercial Bank
##First click the search box to reveal input box
searchBar = browser.find_elements_by_id('select2-sector-container')
searchBar[0].click()
## Now type vaule into search box 
searchBar = browser.find_element_by_css_selector('input.select2-search__field')
searchBar.send_keys('Commercial Bank')

sdate = date(2011, 3, 20)
edate = date(2021, 2, 25)
dates = return_dates(sdate,edate)
os.mkdir('data')
os.chdir('data')
for day in dates:
    #Enter the date
    date_box = browser.find_elements_by_id('fromdate')
    date_box[0].clear()
    date_box[0].send_keys(day)
    #Click Search
    searchBar=browser.find_element_by_id('btn_todayshareprice_submit')
    searchBar.click()
    time.sleep(3) #Needed don't know why
    searchBar.send_keys(Keys.ENTER)
    time.sleep(5) #Wait for data to show up
    #Scrape the table
    html = browser.page_source
    if(scrape_table(data=html,date=day)):
        print(day,'Done')





