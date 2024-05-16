from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.medicamentosplm.com/Home/Laboratorio/A/1"
driver.get(url)
print("Loading finished!")
sleep(3)
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in letters:
    url_1 = url.rsplit("/", 2)[0] + "/" + letter + "/1"
    print(url_1)
    driver.get(url_1)
    sleep(1)
    elements = driver.find_elements(By.ID, "editable")
    for element in elements:
        element.click()
    