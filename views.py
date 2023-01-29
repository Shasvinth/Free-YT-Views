from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

no_of_driver = int(input("Enter Number of Drivers : "))
url = input("Enter URL : ")
time_to_refresh = int(input("Enter refresh rate in seconds : "))
drivers = []

for i in range(no_of_driver):
    drivers.append(webdriver.Chrome(executable_path=ChromeDriverManager().install()))
    drivers[i].get(url)
while True:
    time.sleep(time_to_refresh)
    for i in range(no_of_driver):
        drivers[i].refresh()