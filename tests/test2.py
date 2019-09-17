from selenium import webdriver
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

chromedriver = '/usr/bin/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
browser.get('https://www.demotestsite.net')

if(browser.title=="Gary Mc Dermott"):
    browser.save_screenshot('/home/tests/picture-'+timestr+'.png')
    print ("Success: Main blog page exists")
    print exit(0)
else:
    print ("Test failed: page title is incorrect")
    browser.save_screenshot('/home/tests/picture-'+timestr+'.png')
    # python Datadog raise alert
    print exit(1)

browser.quit()
