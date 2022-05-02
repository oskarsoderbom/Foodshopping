"""Hopefully autocomplete shoppinglist with a full basket
of items from ICA.SE"""

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException



def fillshoppinglist(fullist):
    """Fills a basket of items att ICA.SE based on inputlist"""
    
    driver = webdriver.Chrome(r'/Users/oskarsoderbom/chromedriver')

    driver.get('https://www.ica.se/handla/maxi-ica-stormarknad-orebro-boglundsangen-id_01093/')
    sleep(2)
    
    notfoundlist = []
    for i in fullist:
        if i != ' ':
            print(i)
            try:
                driver.find_element_by_xpath('//*[@id="application-bar"]/div[1]/div/div[2]/form/input[1]').send_keys(i)
            except NoSuchElementException:
                driver.refresh()
                notfoundlist.append(i)
            sleep(1)
           
        #första gången man väljer en vara
            try:
                driver.find_element_by_xpath('//*[@id="application-bar"]/div[3]/div/div/ul/li[1]/a/aside/div/div/button').click()
            except NoSuchElementException:    #Om varan redan finns måste man trycka på ett plustecken istället
                try:
                    driver.find_element_by_xpath('//*[@id="application-bar"]/div[3]/div/div/ul/li[1]/a/aside/div/div/div/button[2]').click()
                except NoSuchElementException:
                    notfoundlist.append(i)
                    
            sleep(1)
            try:
                driver.find_element_by_xpath('//*[@id="application-bar"]/div[1]/div/div[2]/form/input[1]').clear()
            except NoSuchElementException:
                pass
            sleep(1.5)
   
    timetocomplete = 300
    print(f"Shopping list done, please complete the order in your browser, you need to interact with the browser in {timetocomplete} seconds before it closes")
    print("These products could not be found:")
    print(notfoundlist)
    
    sleep(timetocomplete)