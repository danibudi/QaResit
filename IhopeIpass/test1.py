from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Users\stefa\PycharmProjects\IhopeIpass\chromedriver.exe")

driver.get('https://the-internet.herokuapp.com/login')

login = driver.find_element(By.ID, 'username')
login.send_keys('tomsmith')
login = driver.find_element(By.ID, 'password')
login.send_keys('SuperSecretPassword!')
element = driver.find_element_by_css_selector('.fa.fa-2x.fa-sign-in')
login.send_keys(Keys.ENTER)
driver.close()