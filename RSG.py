import pandas
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path='./geckodriver.exe')

df = pandas.read_csv('songs.csv')
ch = random.randint(0,34)
print("                                        "+df['name'][ch])
print("")
print("                                         Link to the song!")
#print("Opening Song in Browser")
song = str(df['link'][ch])
print(song + "/")

driver.get(song+"/?autoplay=1")
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH , "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[5]/button")))
element.click()



