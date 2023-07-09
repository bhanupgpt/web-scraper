import time
from selenium import webdriver

def getSocietyUrl(flat_url):
  time.sleep(1)
  # --------------------------------- webdriver here -----------------------------------
  driver = webdriver.Chrome()
  driver.get(flat_url)
  try:
    span_el = driver.find_element_by_class_name('prop_address')
    society_url = span_el.find_element_by_xpath('.//a').get_attribute('href')
  except:
    society_url = 'NA'
  driver.close()
  return society_url

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
  file1 = open('society.txt', 'a')
  for i in range(2000):
    society_url = getSocietyUrl(flat_urls[i])
    if not (society_url == 'NA' or  society_url in society_links):
      file1.write(society_url)
      file1.write('\n')
      society_links.append(society_url)
  file1.close()