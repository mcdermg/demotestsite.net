from selenium import webdriver
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

if(browser.title=="Gary Mc Dermott"):
    browser.save_screenshot('./screenshots/test1-pass-'+timestr+'.png')
    print ("Test passed: Page title is correct")
    print exit(0)
else:
    print ("Test failed: Page title is incorrect")
    browser.save_screenshot('./screenshots/test1-fail-'+timestr+'.png')
    # python Datadog raise alert
    print exit(1)

browser.quit()
