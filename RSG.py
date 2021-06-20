import pandas
import random
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#driver = webdriver.Firefox()

df = pandas.read_csv('songs.csv')
ch = random.randint(0,34)
print("                                        "+df['name'][ch])
print("")
print("                                         Link to the song!")
#print("Opening Song in Browser")
song = str(df['link'][ch])
print("                                    "+"\033[2;36;40m"+song)
print("\033[1;37;40m")
#driver.get(song)





