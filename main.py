from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
import webbrowser
import pyautogui

specific_country = input("Do you want to know the forecast or listen to radio(yes for forecast / no for radio) ? ")

if specific_country == 'yes':
        city = input('Which city forecast you want to know? ')
        driver = webdriver.Chrome()

        driver.get("https://www.yr.no/en")
        WebDriverWait(driver, 10)
        
        try:

                search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "page-header__search-button")))
                search.click()

                time.sleep(1)

                search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "page-header__search-input")))
                WebDriverWait(driver, 1)
                search_box.send_keys(city)

                time.sleep(1)

                first_result = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "search__suggested-item")))
                first_result.click()
                
                find = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "daily-weather-list-item__forecast")))
                temp = find.text
                driver.quit()

                temp = temp.split('\n')
                pos1 = [line.split() for line in temp]

                df = pd.DataFrame(list(zip(pos1)), columns = ['[temperature:]']) 
                removed_df = df.drop(df.index[0])
                print(removed_df)

                driver.quit()
        except TimeoutException:
                print("City not found or does not exist.")
                driver.quit()
           
elif specific_country == 'no':
        try:
                radio = input('Which radio station do you want to listen to? ')
                driver = webdriver.Chrome()
        
                webbrowser.open_new_tab('http://radio.lv/' + radio +'/')
                
                time.sleep(4)
                
                pyautogui.moveTo(310, 330)
                
                pyautogui.click()
                
                time.sleep(1)
        except TimeoutException:
                print("Radio station not found or does not exist.")
                driver.quit()