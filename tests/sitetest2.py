# Import depdency libraries
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import logging

# For logging all events info and above and formatting with log level, datetime and message
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# Timstring for datetime format used in screenshot output
timestr = time.strftime("%Y%m%d-%H%M%S")

# Location of Chromedriver Linux used in pipline. Windows forr local testing.
chromedriver = '/usr/bin/chromedriver'
#chromedriver = 'C:/repos/demotestsite.net/chromedriver/chromedriver.exe'

# Set options for Selienium & Chromedriver. Run headless etc
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

# url to be retrieved.
# Checking S3 url not site url due to CF caching. Needs to be http NOT https.
#browser.get('https://www.demotestsite.net')
browser.get('http://www.demotestsite.net.s3-website.ca-central-1.amazonaws.com')

# test. using try catch as if element does not exist exception is thrown.
# Exception does not get thrown anymore with else in place. keeping as legacy as occured in passed.
try:
    #x=browser.find_elements_by_id("navbarCollapse")
    #x=browser.find_elements_by_id("naddaaaaaaa")
    #x=browser.find_elements_by_xpath("//a[contains(text(),'naddaaaaaaa')]")
    x=browser.find_elements_by_xpath("//a[contains(text(),'About')]")
    if(len(x)>0):
        browser.save_screenshot('./screenshots/test2-pass-'+timestr+'.png')
        logging.info("Success: Found About in navbar")
        logging.info(exit(0))
        #print ("Success: Found About in navbar")
        #print exit(0)
except NoSuchElementException:
    browser.save_screenshot('./screenshots/test2-NoSuchElementException-'+timestr+'.png')
    logging.critical("No such element found exception.")
    logging.critical(exit(1))
    #print("No element found. Breaking...")
    #print exit(1)
else:
    if(len(x)==0):
        browser.save_screenshot('./screenshots/test2-fail-'+timestr+'.png')
        logging.error("Test failed: Could not find About in navbar")
        logging.error(exit(1))
        #print ("Test failed: Could not find About in navbar")
        #print exit(1)

# Close off webdriver & selienium
browser.quit()
