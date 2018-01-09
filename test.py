# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re

class Test():

	#Define your url here
	url = "file:///home/shaque/Desktop/test.html"

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)

	def waitForElementByXpath(self, elementXpath):
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, elementXpath)))

	def waitForElementByID(self, elementId):
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, elementId)))

	# Close random popup
	def clickCloseButton(self):
		self.waitForElementByXpath("//input[@class='button']")
		closeButton = self.driver.find_element_by_xpath("//input[@class='button']")
		closeButton.click()
		print "Close button clicked"

	# Try to close Main popup
	def clickXButton(self):
		#uncomment the next command and change sleeping time to see test result more detailed.
		#Random popup opens in 1-5 seconds, if you set a unit higher than 5 (seconds) the test won't ever be finished 
		###time.sleep(3)
		try:
			self.waitForElementByID("close")
			xButton = self.driver.find_element_by_id("close")
			if xButton.is_displayed():
				xButton.click()
				print "x button clicked"
		except:
			pass

	# Check if Main popup is closed
	def validateMainPopupExistance(self):
		xButton = self.driver.find_element_by_id("close")
		if xButton.is_displayed():
			print "Main popup found"
			return True
		else:
			print "Main popup not found"
			return False

	def test(self):
		while 1:
			self.clickXButton()
			if self.validateMainPopupExistance() is False:
				print "\n\nMain popup is closed\nTest is finished"
				exit()
			else:
				self.clickCloseButton()

	def tearDown(self):
		self.driver.quit()

	def run(self):
		self.setUp()
		self.driver.get(self.url)
		self.test()
		self.tearDown()

test = Test()
test.run()
