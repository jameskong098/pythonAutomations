
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

import time

driver = webdriver.Chrome()

driver.get("https://slate.brandeis.edu/portal/brandeis_covid19")

login = driver.find_element(By.XPATH, '//*[@id="username"]')
login.send_keys("[Enter username here]")

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("[Enter password here]")

enter = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/form/div[6]/button')
enter.click()

delay = 10

try:
    myElem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable(By.XPATH('//button[contains(text(),"Send Me a Push ")]'))).click()
    print("found submit button!!!!!!")
except TimeoutException:
    print("Operation Timed Out!")

dlh = driver.find_element(By.XPATH, '//*[@id="part_f279cdf7-5861-4d4d-b429-e929dd0f19d3"]/form/div/span/input')
dlh.click()

answer1 = driver.find_element(By.XPATH, '//*[@id="form_febaa6cf-a91c-4512-9a62-1b4d9fc76087_10"]')
answer1.click()

answer2 = driver.find_element(By.XPATH, '//*[@id="form_d18b4fe3-24e1-48fa-8275-eac56f2485fc_2"]')
answer2.click()

answer3 = driver.find_element(By.XPATH, '//*[@id="form_7621d269-5d6c-4104-90c4-ea21e5c0a953_1"]')
answer3.click()

answer4 = driver.find_element(By.XPATH, '//*[@id="form_718644d8-2fac-43e8-9ee4-b292aafe4f45_1"]')
answer4.click()

answer5 = driver.find_element(By.XPATH, '//*[@id="form_32d2699d-af14-421e-b709-fb6270bdbf8e_container"]/div[4]/button')
answer5.click()

time.sleep(3)

driver.quit()

