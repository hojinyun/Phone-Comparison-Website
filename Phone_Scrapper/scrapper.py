from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup

driver = Chrome('/Users/chromedriver')

url = "http://search.danawa.com/dsearch.php?query=%ED%95%B8%EB%93%9C%ED%8F%B0&originalQuery=%ED%95%B8%EB%93%9C%ED%8F%B0&previousKeyword=%ED%95%B8%EB%93%9C%ED%8F%B0&volumeType=allvs&"

def extract_phone(result):
    html = result.find('div', {"class": "prod_info"})
    try:
        name = html.find('p',{"class": "prod_name"}).get_text().strip()
        display_size = html.find('a',{"onclick": "$.termDicViewLink(3319,'view',this,0,224,48419); return false;"}).get_text()
        ap = html.find('a',{"onclick": "$.termDicViewLink(28494,'view',this,0,224,48419); return false;"}).get_text()
        ram = html.find('a',{"onclick": "$.termDicViewLink(29426,'view',this,0,224,48419); return false;"}).get_text()
        storage = html.find('a',{"onclick": "$.termDicViewLink(3483,'view',this,0,224,48419); return false;"}).get_text().strip("내장:")
        back_camera = html.find('a',{"onclick": "$.termDicViewLink(11216,'view',this,0,224,48419); return false;"}).get_text().strip("후면:")
        front_camera = html.find('a',{"onclick": "$.termDicViewLink(11216,'view',this,0,224,48419); return false;"}).find_next_sibling('a').get_text().strip("전면:")
        battery = html.find('a',{"onclick": "$.termDicViewLink(11847,'view',this,0,224,48419); return false;"}).get_text()
        charge_speed = html.find('a',{"onclick": "$.termDicViewLink(210751,'view',this,0,224,48419); return false;"}).get_text().strip("최대")
        weight = html.find('a',{"onclick": "$.termDicViewLink(11157,'view',this,0,224,48419); return false;"}).get_text().strip("무게:")
        thickness = html.find('a',{"onclick": "$.termDicViewLink(11201,'view',this,0,224,48419); return false;"}).get_text().strip("두께:")
        prices = result.find_all('a',{"class": "click_log_product_standard_price_"})
       
        #Prvents 가격비교예정
        for price in prices:
            if (price.get_text() == "가격비교예정"):
                continue
            else:
                final_price = price.find('strong').get_text()
            

        display_size = display_size.split('(', 1)[0] #gets rid of inch
        
        return{
            'name': name,
            'display_size': display_size,
            'ap': ap,
            'ram': ram,
            'storage': storage,
            'back_camera': back_camera,
            'front_camera': front_camera,
            'battery': battery,
            'charge_speed': charge_speed,
            'weight': weight,
            'thickness': thickness,
            'price': final_price
        }
    except:
        return


def extract_phones(pages):
    phones = [] 
    for page in range(pages):
        print(f"Scrapping Danawa: Page: {page+1}")
        #Gets HTML
        driver.get(f"{url}page={page+1}&limit=40&sort=dateDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=12215709&defaultPhysicsCategoryCode=224%7C48419%7C48829%7C0&defaultVmTab=100435&defaultVaTab=9212989&tab=main")
        danawa_soup = BeautifulSoup(driver.page_source)
        product_list = danawa_soup.find('ul', {"class": "product_list"})
        results = product_list.find_all('li', {"class": "prod_item"})

        #Gets phone name
        for result in results:
            phone = extract_phone(result)
            phones.append(phone)
        driver.refresh()
    print(phones)
    return phones

    
