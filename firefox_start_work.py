import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile

# set profile firefox
profile = FirefoxProfile('/home/dima/.mozilla/firefox/mwad0hks.default/')
driver = selenium.webdriver.Firefox(profile)
# open "CRM"
driver.get("http://fox.tenet.kettle.te.net.ua/CallCenter/login.php")
# find id "txt_login"
username = driver.find_element_by_id(id_="txt_login")
# find id "pas_password"
password = driver.find_element_by_id(id_="pas_password")
# enter login
username.send_keys("dmitryb")
# enter password
password.send_keys("D380675561828")
# click button "login"
driver.find_element_by_id("sub_submit").click()
###############################################
# open tab
ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
# open "adm"
driver.get("http://adm.te.net.ua/")
# find id "P101_USERNAME"
username = driver.find_element_by_id(id_="P101_USERNAME")
# find id "P101_PASSWORD"
password = driver.find_element_by_id(id_="P101_PASSWORD")
# enter login
username.send_keys("dmitryb")
# enter password
password.send_keys("D380675561828")
# click button "enter"
driver.find_element_by_id(id_="P101_LOGIN").click()
###############################################
# open tab
ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
# open "monica"
driver.get("https://monica.tenet.ua/snmpc/summary")
###############################################
# open tab
ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
# open "RT"
driver.get("https://mail.te.net.ua/")
# find name "Username"
username = driver.find_element_by_name("Username")
# find password "Password"
password = driver.find_element_by_name("Password")
# enter login
username.send_keys("dmitryb")
# enter password
password.send_keys("D380675561828")
# click button "enter"
driver.find_element_by_name("Logon").click()
###############################################
# open tab
ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
# open URL 5
# driver.get("https://rt.tenet.ua/")
# driver.close()