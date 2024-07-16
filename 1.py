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
data_set = []
for letter in letters:
    url_1 = url.rsplit("/", 2)[0] + "/" + letter + "/1"
    print(url_1)
    driver.get(url_1)
    sleep(1)
    links = []
    lis = driver.find_elements(By.ID, "editable")
    for li in lis:
        links.append(li.find_element(By.TAG_NAME, "a").get_attribute('href'))
    print(links)
    for link in links:
        print("AAAAAAAA")
        print(link)
        sleep(2)
        # link_url = link.find_element(By.TAG_NAME, "a").get_attribute('href')
        # print(link_url)
        # sleep(2)
        driver.get(link)
        sleep(2)
        filas = driver.find_elements(By.ID, "editable")
        for fila in filas:
            company = fila.find_element(By.ID, "prescription-division-1").text
            medicine = fila.find_element(By.CLASS_NAME, "first").text
            substance = fila.find_element(By.ID, "prescription-substance-1").text
            pharmaceutical_form = fila.find_element(By.ID, "prescription-pharmaForm-1").text
            presentation = fila.find_element(By.ID, "prescription-presentation-1").text
            data = {"company": company, "medicine": medicine, "substance": substance, "pharmaceutical_form": pharmaceutical_form, "presentation": presentation}
            data_set.append(data)
        print(data_set)
        driver.back()
        # link_url = ""
        print("BBBBBBBBB")
        sleep(5)
driver.quit()
    