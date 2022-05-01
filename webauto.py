"""Hopefully autocomplete shoppinglist with a full basket
of items from ICA.SE"""

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException



def fillshoppinglist(fullist):
    """Fills a basket of items att ICA.SE based on inputlist"""
    
    driver = webdriver.Chrome(r'/Users/oskarsoderbom/chromedriver')

    driver.get('https://www.ica.se/')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="onetrust-button-group"]/div').click()
    print('cookies accepted')
    driver.find_element_by_xpath('/html/body/div[1]/div/header/div[2]/div/div/div[2]/a').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="zipcode"]').send_keys('70358')
    sleep(1)
    driver.find_element_by_xpath('//*[@id="store-selector-app"]/div/div[2]/button[1]').click()
    driver.find_element_by_xpath('//*[@id="store-selector-app"]/div/div[2]/ul/li[1]/div[3]/button').click()
    sleep(1)

    notfoundlist = []
    for i in fullist:
        if i != ' ':
            print(i)
            driver.find_element_by_xpath('//*[@id="application-bar"]/div[1]/div/div[2]/form/input[1]').send_keys(i)
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

    print("Shopping list done, please complete the order in your browser")
    print("These products could not be found:")
    print(notfoundlist)