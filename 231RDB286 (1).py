from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import PyPDF2
import pandas as pd

specific_country = input("do you want tp know about specific country ? ")


if specific_country == 'yes':
        city = input('which country? ')
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

                # Create a pandas DataFrame from the data
                
                
                df = pd.DataFrame(list(zip(pos1)), columns = ['[temperature:]']) 
                removed_df = df.drop(df.index[0])
                print(removed_df)

                driver.quit()
        except TimeoutException:
                print("Country not found or does not exist.")
                driver.quit()
           
elif specific_country == 'no':
        print('TAVA MAMMA')