import time
from selenium import webdriver
from openpyxl import Workbook, load_workbook

def writeFile(title, constructed, location, possession_val, units_val, full_address_val, pincode_val, society_url):
  wb = load_workbook('Ahmedabad.xlsx')
  ws = wb.active
  ws.append([title, constructed, location, possession_val, units_val, full_address_val, pincode_val, society_url])
  wb.save('Ahmedabad.xlsx')

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
  main_url = 'https://www.magicbricks.com/property-for-rent/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment&cityName=Ahmedabad'
  driver = webdriver.Chrome()
  driver.get(main_url)
  driver.maximize_window()
  driver.find_element_by_id('refineMoreTitle').click()
  time.sleep(1)
  driver.find_element_by_xpath('//label[contains(text(), "Society Only")]').click()
  driver.find_element_by_class_name('m-filter__btn').click()
  time.sleep(2)
  while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    time.sleep(5)
    society_elements = driver.find_elements_by_xpath('//a[@class="m-srp-card__link"]')
    
    if len(society_elements) > 3000:
      break
  print(len(society_elements))
  society_links = []
  for each_element in society_elements:
    society_url = each_element.get_attribute('href')
    if not society_url in society_links:
      society_links.append(society_url)
  print(len(society_links))
  driver.close()
  for each_link in society_links:
    societyScrape(each_link)