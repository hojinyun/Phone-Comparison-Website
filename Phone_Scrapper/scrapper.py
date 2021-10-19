from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

from bs4 import BeautifulSoup

url = "http://search.danawa.com/dsearch.php?query=%ED%95%B8%EB%93%9C%ED%8F%B0&originalQuery=%ED%95%B8%EB%93%9C%ED%8F%B0&previousKeyword=%ED%95%B8%EB%93%9C%ED%8F%B0&volumeType=allvs&page=1&limit=40&sort=dateDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=12215709&defaultPhysicsCategoryCode=224%7C48419%7C48829%7C0&defaultVmTab=100435&defaultVaTab=9212989&tab=main"

driver = Chrome()
driver.get(url)

#for page in range(1,10):
#print("Page: ", page)
danawa_soup = BeautifulSoup(driver.page_source)
product_list = danawa_soup.find('ul', {"class": "product_list"})
phones = product_list.find_all('li', {"class": "prod_item"})
for phone in phones:
  try:
    phone_name = phone.find('p',{"class": "prod_name"}).get_text()
  except:
    continue;