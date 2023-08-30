# from selenium import webdriver
#
# chrome_driver = "C:\dev\chromedriver"
#
# driver = webdriver.Chrome(executable_path=chrome_driver)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:/Users/safarig/Downloads/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/s?k=instant+pot&crid=1JYVD0KCAHQ49&sprefix=instant+%2Caps%2C214&ref=nb_sb_ss_ts-doa-p_1_8")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)
driver.quit()

