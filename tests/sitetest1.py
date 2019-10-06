# Import depdency libraries
from selenium import webdriver
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

# url to be retrieved
browser.get('https://www.demotestsite.net')

# Test
if(browser.title=="Gary Mc Dermott"):
    browser.save_screenshot('./screenshots/test1-pass-'+timestr+'.png')
    #print ("Test passed: Page title is correct")
    logging.info("Test passed: Page title is correct")
    logging.info(exit(0))
    #print exit(0)
else:
    browser.save_screenshot('./screenshots/test1-fail-'+timestr+'.png')
    # TODO python Datadog raise alert
    logging.error("Test failed: Page title is incorrect")
    logging.error(exit(1))
    #print ("Test failed: Page title is incorrect")
    #print exit(1)

# Close off webdriver & selienium
browser.quit()
