from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import csv
import time

from selenium.webdriver.firefox.service import Service
service = Service(executable_path="./geckodriver")
options = webdriver.FirefoxOptions()
options.add_argument("--headless")


# creating csv file
filename = "jac.csv"

# open csv file to write
f = open(filename, 'w')

# create header in file


# put range of rollnumber
for i in range(10001, 10302):
	
	# use try and exception because if any
	# rollnumber is invalid then whole
	# program is not stop.
	try:
		driver = webdriver.Firefox(service=service, options=options)
		
		# link is given above copy and paste
		driver.get(
			"https://www.jacresults.com/cls-eleven-2023/index.php")

		# put rollcode
		driver.find_element(By.XPATH,
			'/html/body/form/div/div/div/div/div[1]/table/tbody/tr[1]/td[2]/input').send_keys("32010")
		
        # put rollnumber
		driver.find_element(By.XPATH,
			'/html/body/form/div/div/div/div/div[1]/table/tbody/tr[2]/td[2]/input').send_keys(i)
		
		# view result xpath
		driver.find_element(By.XPATH,
			'/html/body/form/div/div/div/div/div[2]/div[1]/button').click()
		
		# student name
		name = driver.find_element(By.XPATH,
			'/html/body/div[1]/form/div/div/div[2]/table[1]/tbody/tr[3]/td/p').text

    	# roll code 
		code = driver.find_element(By.XPATH,
			'/html/body/div[1]/form/div/div/div[2]/table[1]/tbody/tr[1]/th[1]/span[2]').text

		# roll number 
		roll = str(i)

		# all details fill into file
		f.write(name+","+roll+"\n")
		driver.close()
	
	except NoSuchElementException as exception:
		continue

f.close()
