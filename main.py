import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def login():
    driver = webdriver.Firefox()
    driver.get("https://www.twitter.com")
    
    enter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div'))
    )
    enter.click()
    
    enter_username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'))
    )
    enter_username.send_keys(os.getenv('USERNAME'))
    
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'))
    )
    next_button.click()
    
    enter_password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))
    )
    enter_password.send_keys(os.getenv('PASSWORD'))
    
    final_enter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'))
    )
    final_enter.click()
    
    return driver

def go_to_profile(driver):
    time.sleep(5)
    driver.get("https://www.twitter.com/" + os.getenv('USERNAME'))
    
def find_first_visible_element(driver, css_selector):
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector))
    )
    
    for element in elements:
        if element.is_displayed():
            return element

    raise Exception("No visible elements found.")

def unretweet(driver):
    try:
        unretweet_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'r-4qtqp9 r-yyyyoo r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1xvli5t r-1hdv0qi'))
        )
        unretweet_button.click()
        
        confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div'))
        )
        confirm.click()
    except Exception as e:
        erase(driver)

def erase(driver):

    try:
        time.sleep(5)
        dots = find_first_visible_element(driver, '.r-4qtqp9.r-yyyyoo.r-dnmrzs.r-bnwqim.r-1plcrui.r-lrvibr.r-1xvli5t.r-1hdv0qi')
        dots.click()
    
        erase_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[1]'))
        )
        erase_button.click()
        
        confirm = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div'))
    )
        confirm.click()

    except Exception as e:
        driver.execute_script("window.scrollBy(0, 300)")
    
    
    time.sleep(5)


driver = login()
go_to_profile(driver)
while True:
    unretweet(driver)