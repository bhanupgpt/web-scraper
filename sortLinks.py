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
  flat_urls.sort()
  society_links.sort()
  society_file = open('society_sorted.txt', 'w')
  for society_url in society_links:
    society_file.write(society_url)
    society_file.write('\n')
  society_file.close()
  flat_file = open('flat_sorted.txt', 'w')
  for flat_url in flat_urls:
    flat_file.write(flat_url)
    flat_file.write('\n')
  flat_file.close()