import time
from selenium import webdriver
from openpyxl import Workbook, load_workbook

def writeFile(title, constructed, location, possession_val, units_val, full_address_val, pincode_val, society_url):
  wb = load_workbook('Ahmedabad_Sale.xlsx')
  ws = wb.active
  ws.append([title, constructed, location, possession_val, units_val, full_address_val, pincode_val, society_url])
  wb.save('Ahmedabad_Sale.xlsx')

def societyScrape(society_url):
  driver = webdriver.Chrome()
  driver.get(society_url)
  title = driver.find_element_by_xpath('//h1[@class="heading"]').text
  try:
    [constructed, loc] = (driver.find_element_by_xpath('//h2[@class="proj-info__name"]').text).split('\n')
  except:
    [constructed, loc] = ['NA', 'NA']
  try:
    location = driver.find_element_by_xpath('//div[@class="proj-info__address"]').text
  except:
    location = 'NA'
  try:
    possession_val = driver.find_element_by_xpath('//div[contains(text(), "Possession by")]/following-sibling::div').text
  except:
    possession_val = 'NA'
  try:
    units_val = driver.find_element_by_xpath('//div[contains(text(), "Total Units")]/following-sibling::div').text
  except:
    units_val = 'NA'
  try:
    full_address_val = driver.find_element_by_xpath('//div[contains(text(), "Full Address")]/following-sibling::div').text
  except:
    full_address_val = 'NA'
  try:
    pincode_val = driver.find_element_by_xpath('//div[contains(text(), "Pincode")]/following-sibling::div').text
  except:
    pincode_val = 'NA'
  driver.close()
  writeFile(title, constructed, location, possession_val, units_val, full_address_val, pincode_val, society_url)

if __name__ == '__main__':
  with open('society_sorted.txt') as f:
    lines = f.readlines()
    for line in lines:
      society_url = line.replace('\n', '')
      societyScrape(society_url)