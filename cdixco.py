import time
from selenium import webdriver

drivers = webdriver.Firefox(executable_path=r'/home/harshchhatbar/Downloads/geckodriver-v0.28.0-linux32/geckodriver')
drivers.get('https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1')
time.sleep(5)
drivers.find_element_by_id('ltkpopup-email').send_keys('harshchhatbar34@gmail.com')
time.sleep(5)
drivers.find_element_by_id('submitButton').click()
drivers.find_element_by_id('x-mark-icon').click()
productBox = drivers.find_elements_by_class_name('price')
company = drivers.find_elements_by_class_name('catalog-item-brand')
stock = drivers.find_elements_by_class_name('status')
name = drivers.find_elements_by_class_name('catalog-item-name')
output = []
for i in range(len(productBox)):
    tempdict = {}
    tempdict['price'] = productBox[i].text
    tempdict['Title'] = name[i].text
    if stock[i].text == 'Out of Stock':
        tempdict['stock'] = False
    else:
        tempdict['stock'] = True
    tempdict['Manufacturer'] = company[i].text
    output.append(tempdict)

print(output)
