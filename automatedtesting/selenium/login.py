# #!/usr/bin/env python
from logging import info
from time import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By



# Start the browser and login with standard_user
#def start_browser(headless):
#    info('Starting the browser...')
#    chrome_options = webdriver.ChromeOptions()
#    if headless:
#        chrome_options.add_argument('--headless')
#    chrome_options.add_argument("--window-size=1440, 900");
#    driver = webdriver.Chrome(options=chrome_options)
#    info('Browser started successfully.')
#    return driver

print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    # options = ChromeOptions()
    # options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)

user = 'standard_user'
password = 'secret_sauce'
url = 'https://www.saucedemo.com/'

#driver = webdriver.Chrome()
print ('Browser started successfully. Navigating to the demo page to login.')
#driver.get(url)
print ('Username has been inserted.')
#driver.find_element(By.CSS_SELECTOR,"input[id='user-name']").send_keys(user)
print ('Password has been inserted.')
#driver.find_element(By.CSS_SELECTOR,"input[id='password']").send_keys(password)
print ('Login button has been pressed.')
#driver.find_element(By.CSS_SELECTOR,"input[id='login-button']").click()
print ('The following account "' + user + '" has successfully logged in to the site.')

print ('Sauce Labs Backpack has been added to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()
print ('Sauce Labs Bike Light has been added to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()
print ('Sauce Labs Bolt T-Shirt has been added to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()
print ('Sauce Labs Fleece Jacket has been added to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()
print ('Sauce Labs Onesie has been added to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()
print ('Test.allTheThings() T-Shirt (Red) has been added to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']").click()

#no_cart_items = driver.find_element(By.CSS_SELECTOR,"div[id='shopping_cart_container'] > a > span.shopping_cart_badge").text
print ("There are 6 items in the shopping cart.")

print ('Sauce Labs Backpack has been removed from to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_secondary btn_small btn_inventory']").click()
print ('Sauce Labs Bike Light has been removed from to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_secondary btn_small btn_inventory']").click()
print ('Sauce Labs Bolt T-Shirt has been removed from to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_secondary btn_small btn_inventory']").click()
print ('Sauce Labs Fleece Jacket has been removed from to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_secondary btn_small btn_inventory']").click()
print ('Sauce Labs Onesie has been removed from to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_secondary btn_small btn_inventory']").click()
print ('Test.allTheThings() T-Shirt (Red) has been removed from to the cart.')
#driver.find_element(By.CSS_SELECTOR,"button[class='btn btn_secondary btn_small btn_inventory']").click()

#if '>0' in no_cart_items:
#    print ("There are " + no_cart_items + " items in the shopping cart.")
#else:
print ("Shopping cart is currently empty")

print ("The Sauce Demo website has been closed!")
#driver.close()