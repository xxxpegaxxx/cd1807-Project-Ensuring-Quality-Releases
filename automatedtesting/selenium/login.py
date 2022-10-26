# #!/usr/bin/env python
from time import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


# Start the browser and login with standard_user
#def login (user, password, url):
print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    # options = ChromeOptions()
    # options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)

user = 'standard_user'
password = 'secret_sauce'
url = 'https://www.saucedemo.com/'

driver = webdriver.Chrome()
print ('Browser started successfully. Navigating to the demo page to login.')
driver.get(url)
print ('Username has been inserted.')
driver.find_element(By.CSS_SELECTOR,"input[id='user-name']").send_keys(user)
print ('Password has been inserted.')
driver.find_element(By.CSS_SELECTOR,"input[id='password']").send_keys(password)
print ('Login button has been pressed.')
driver.find_element(By.CSS_SELECTOR,"input[id='login-button']").click()

driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()

no_cart_items = driver.find_element(By.CSS_SELECTOR,"div[id='shopping_cart_container'] > a > span.shopping_cart_badge").text
print ("There are " + no_cart_items + " items in the shopping cart")
driver.find_element(By.CSS_SELECTOR,"input[id='shopping_cart_link']").click()

time.wait(10)
#login('standard_user', 'secret_sauce', 'https://www.saucedemo.com/')

