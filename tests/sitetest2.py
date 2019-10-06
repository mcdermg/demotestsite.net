from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

chromedriver = '/usr/bin/chromedriver'
#chromedriver = 'C:/repos/demotestsite.net/chromedriver/chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

browser.get('https://www.demotestsite.net')

try:
    #x=browser.find_elements_by_id("navbarCollapse")
    #x=browser.find_elements_by_id("naddaaaaaaa")
    #x=browser.find_elements_by_xpath("//a[contains(text(),'naddaaaaaaa')]")
    x=browser.find_elements_by_xpath("//a[contains(text(),'About')]")
    if(len(x)>0):
        print ("Success: Found About in navbar")
        browser.save_screenshot('./screenshots/test2-pass-'+timestr+'.png')
        print exit(0)
except NoSuchElementException:
    print("No element found. Breaking...")
    browser.save_screenshot('./screenshots/test2-NoSuchElementException-'+timestr+'.png')
    print exit(1)
else:
    if(len(x)==0):
        print ("Test failed: Could not find About in navbar")
        browser.save_screenshot('./screenshots/test2-fail-'+timestr+'.png')
        print exit(1)

browser.quit()
