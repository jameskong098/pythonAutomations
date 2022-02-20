
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

import time

driver = webdriver.Chrome()

driver.get("https://slate.brandeis.edu/portal/brandeis_covid19")

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("[enter Brandeis username]") #Brandeis username should replace this string

driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("[enter Brandeis password]") #Brandeis password should replace this string

driver.find_element(By.XPATH, '/html/body/div/div[3]/div/form/div[6]/button').click()

time.sleep(5)

iFrame = driver.find_element(By.XPATH, "//iframe[@id='duo_iframe']")
driver.switch_to.frame(iFrame)

maxTime = 10

try:
    WebDriverWait(driver, maxTime).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
except TimeoutException:
    print("Duo Submit Timed Out!")

try:
    WebDriverWait(driver, maxTime).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Daily Health Assessment']"))).click()
except TimeoutException:
    print("Daily Health Assessment Button Timed Out!")

driver.find_element(By.XPATH, '//*[@id="form_febaa6cf-a91c-4512-9a62-1b4d9fc76087_10"]').click()

driver.find_element(By.XPATH, '//*[@id="form_d18b4fe3-24e1-48fa-8275-eac56f2485fc_2"]').click()

driver.find_element(By.XPATH, '//*[@id="form_7621d269-5d6c-4104-90c4-ea21e5c0a953_1"]').click()

driver.find_element(By.XPATH, '//*[@id="form_718644d8-2fac-43e8-9ee4-b292aafe4f45_1"]').click()

driver.find_element(By.XPATH, '//*[@id="form_32d2699d-af14-421e-b709-fb6270bdbf8e_container"]/div[4]/button').click()

driver.quit()

