import time
from selenium import webdriver
from openpyxl import Workbook, load_workbook
from google.colab import drive

def writeFile(title, constructed, location, possession_val, units_val, full_address_val, pincode_val, society_url):
  drive.mount('/content/drive')
  wb = pd.read_excel('/content/drive/My Drive/Faridabad_Sale.xlsx')
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

def getSocietyUrl(flat_url):
  time.sleep(1)
  driver = webdriver.Chrome()
  driver.get(flat_url)
  try:
    span_el = driver.find_element_by_class_name('prop_address')
    society_url = span_el.find_element_by_xpath('.//a').get_attribute('href')
  except:
    society_url = 'NA'
  driver.close()
  return society_url

def getFlatUrl(s) :
  url = s[s.index("'") + 1:s.index("'", s.index("'") + 1)]
  return url

if __name__ == '__main__':
  main_url = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Faridabad'
  driver = webdriver.Chrome()
  driver.get(main_url)
  driver.maximize_window()
  prev_cnt = 0
  while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    flat_elements = driver.find_elements_by_class_name('SRCard')
    if len(flat_elements) == prev_cnt:
      break
    prev_cnt = len(flat_elements)
  print(len(flat_elements))
  flat_urls = []
  society_links = []
  for each_element in flat_elements:
    try:
      society_url = each_element.find_element_by_xpath('.//a[@class="m-srp-card__summary__link"]').get_attribute('href')
      if not society_url in society_links:
        society_links.append(society_url)
    except:
      attr = each_element.get_attribute('onclick')
      flat_urls.append(getFlatUrl(attr))
  driver.close()
  for each_flat in flat_urls:
    society_url = getSocietyUrl(each_flat)
    if not (society_url == 'NA' or  society_url in society_links):
      society_links.append(society_url)
  print(len(society_links))
  print(len(flat_urls))
  for each_link in society_links:
    societyScrape(each_link)