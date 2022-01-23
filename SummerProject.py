from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.nasdaq.com/market-activity/stocks/aapl")
action = webdriver.ActionChains(driver)


element = driver.find_element_by_xpath("//div[@class='page__content']//div[2]//ul[1]//li[1]//a[1]")
time.sleep(2)
action.move_to_element(element).perform()#moves to the news element
time.sleep(0.5)
action.move_by_offset(200,0).click().perform()



#element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_loacted((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/main[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/span[1]/p[1]")))
with open('data1.csv', 'a') as csv_file:
		csv_writer = csv.writer(csv_file, delimiter = '')
		csv_writer.writerow("POGU")
for i in range(2, 100):
	action.move_by_offset(i,0).click().perform()
	try:
		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/main[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/span[1]/strong[1]")))
		print(element.text)
		element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[4]/div[1]/main[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/span[1]/p[1]")))
		print(element2.text)
	except:
		print('failed')
	with open('data1.csv', 'a') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([element.text, element2.text])
	time.sleep(0.1)
	
	print("______________________")
	
    	



print("finished")