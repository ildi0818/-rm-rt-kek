from lib2to3.pgen2 import driver
from operator import truediv
from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def Teszt ():
    deciMezo = driver.find_element(By.XPATH, '//*[@id="wrapper"]/fieldset/input[2]')
    icceMezo = driver.find_element(By.XPATH, '//*[@id="wrapper"]/fieldset/input[4]')
    pintMezo = driver.find_element(By.XPATH, '//*[@id="wrapper"]/fieldset/input[6]')
    gomb = driver.find_element(By.XPATH, '//*[@id="wrapper"]/fieldset/button')
    deciMezo.send_keys(1)
    gomb.click()
    try:
        assert icceMezo.get_attribute('value') == 0.11792452830188678 and pintMezo 
    except:
        print("Nem jó!")




driver = webdriver.Chrome()
url = 
driver.get(url)
driver.maximize_window() 