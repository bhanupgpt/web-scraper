import time
from selenium import webdriver

def getFlatUrl(s) :
  url = s[s.index("'") + 1:s.index("'", s.index("'") + 1)]
  return url

if __name__ == '__main__':
  society_links = []
  flat_urls = []
  with open('society.txt') as societyf:
    file_society_links = societyf.readlines()
    for line in file_society_links:
      society_links.append(line.replace('\n', ''))
  with open('flat.txt') as flatf:
    file_flat_urls = flatf.readlines()
    for line in file_flat_urls:
      flat_urls.append(line.replace('\n', ''))
  main_url = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Ahmedabad'
  # ----------------------------------------- webdriver here --------------------------------------------
  driver = webdriver.Chrome()
  driver.get(main_url)
  driver.maximize_window()
  budget = driver.find_element_by_id('inputbudget')
  budget.click()
  time.sleep(1)
  minBudget = driver.find_element_by_id('rangeMinLinkbudgetinput')
  minBudget.send_keys('20000000')
  time.sleep(1)
  maxBudget = driver.find_element_by_id('rangeMaxLinkbudgetinput')
  maxBudget.send_keys('200000000')
  time.sleep(1)
  budget.click()
  time.sleep(3)
  prev_cnt = 0
  while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    flat_elements = driver.find_elements_by_class_name('SRCard')
    if len(flat_elements) == prev_cnt:
      break
    prev_cnt = len(flat_elements)
  society_file = open('society.txt', 'a')
  flat_file = open('flat.txt', 'a')
  print(len(flat_elements))
  for each_element in flat_elements:
    try:
      society_url = each_element.find_element_by_xpath('.//a[@class="m-srp-card__summary__link"]').get_attribute('href')
      if not society_url in society_links:
        society_file.write(society_url)
        society_file.write('\n')
        society_links.append(society_url)
    except:
      attr = each_element.get_attribute('onclick')
      flat_url = getFlatUrl(attr)
      if not flat_url in flat_urls:
        flat_file.write(flat_url)
        flat_file.write('\n')
        flat_urls.append(flat_url)
  driver.close()