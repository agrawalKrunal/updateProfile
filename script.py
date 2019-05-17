from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.

chromedriver = "chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.naukri.com/')

driver.find_element_by_id("login_Layer").click()

username = driver.find_element_by_id("eLoginNew")
password = driver.find_element_by_id("pLogin")

username.send_keys("agrawal.krunal4444@yahoo.com")
password.send_keys("krunaloo7" + Keys.RETURN)

driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

driver.get("https://my.naukri.com/Profile/edit?id=&amp;altresid")
edit = driver.find_element_by_xpath('//*[@id="lazyResumeHead"]/div/div/div/div[1]/span[2]')
edit.click()
driver.find_element_by_id("resumeHeadlineTxt").click()
driver.find_element_by_id("resumeHeadlineTxt").clear()
driver.find_element_by_id("resumeHeadlineTxt").send_keys("3Years of experience as a Software Developer")
save = driver.find_element_by_xpath('/html/body/div[5]/div[8]/div[2]/form/div[3]/div/button')
save.click()

time.sleep(2)
driver.close()
