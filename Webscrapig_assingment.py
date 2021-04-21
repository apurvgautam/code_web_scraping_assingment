from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as cdm

url='https://www.harveynorman.com.au/hp-14-inch-celeron-n4020-4gb-64gb-emmc-laptop.html'

driver= webdriver.Chrome(cdm().install())
driver.get(url)

driver.implicitly_wait(30)

product_title=driver.find_element_by_xpath('//*[@id="breadcrumbs"]/li[8]').text
review_tab=driver.find_element_by_xpath('//*[@id="tab-product-reviews"]')
review_tab.click()
review_title=driver.find_element_by_xpath('//*[@id="BVRRContainer"]/div/div/div/div/ol/li[1]/div[2]/div[1]/div/div[1]/div/div[2]/h3').text
print("Product name: ",product_title)
print("Title of the first review: ",review_title)

driver.quit()