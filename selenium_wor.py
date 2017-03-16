#import webdriver
from selenium import webdriver
#import time
import time
#Select Chrome browser
driver=webdriver.Chrome()
#Maximize the window
driver.maximize_window()
#Go to the url of wisdom of reddit
driver.get("https://wisdomofreddit.com/")
#Take the input to search reddit comment
enter_val=input("Enter the values")
time.sleep(2)
#Put the input into search field
enter_text=driver.find_element_by_xpath("//input[@name='query']").send_keys(enter_val)
time.sleep(3)
#Click on 'Find me some tangents'
serch=driver.find_element_by_xpath("//button[text()='Find me some tangents!']").click()
time.sleep(3)
#Take input for choosing the reddit comment
url1=input("Enter the url")
time.sleep(3)
#Go to the input Url
driver.get(url1)
time.sleep(5)
#Come back to again main page
driver.back()
time.sleep(5)
driver.back()
time.sleep(5)
#Select 'Why' from web page
why_w=driver.find_element_by_xpath("//a[text()='Why']").click()
time.sleep(3)
#Go to 'this article' web page
this_art=driver.find_element_by_xpath("//a[text()='this article']").click()
time.sleep(5)
#Come back to 'Why' page
driver.back()
time.sleep(2)
#Select 'Uses' from web page
uses_w=driver.find_element_by_xpath("//a[text()='Uses']").click()
time.sleep(2)
#Go to 'lived in moscow' comment list
uses_1=driver.find_element_by_xpath('//a[@href="/search?query=%22lived+in+moscow%22"]').click()
time.sleep(3)
#Coome back to 'Uses' page
driver.back()
#Select 'protips' from web page
protips_w=driver.find_element_by_xpath("//a[text()='Pro tips']").click()
time.sleep(2)
#Select 'Examples' from web page
eg_w=driver.find_element_by_xpath("//a[text()='Examples']").click()
time.sleep(2)
#Select 'Blog' from web page
blog_w=driver.find_element_by_xpath("//a[text()='Blog']").click()
time.sleep(2)
#Select 'About' from web page
about_w=driver.find_element_by_xpath("//a[text()='About']").click()
time.sleep(2)
#Click on logo for coming to home page
logo_1=driver.find_element_by_xpath("//img[@src='/static/img/wor_logo.png']").click()
time.sleep(3)
#Close the driver
driver.close()
