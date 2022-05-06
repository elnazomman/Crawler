from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget

driver = webdriver.Chrome('...') #the path of chromdriver
driver.get("https://www.instagram.com/") #get the url

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

username.send_keys(input('enter user name: '))
password.send_keys(input('enter password: '))

#make brand new variable for our loggin. after loggin in click on loggin
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type = 'submit']"))).click()

#save login info? which button? yes or Not Now?
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

searchpage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchpage.clear()
keyword = "#iran"
searchpage.send_keys(keyword)

searchpage.send_keys(Keys.ENTER)

#scroll down the page and save the images on your pc
driver.execute_script("window.scrollTo(0,4000);")
images = driver.find_elements(by=By.TAG_NAME, value='img')
images 

images = [image.get_attribute('src') for image in images]
images

#save images to pc
path = os.getcwd()   #get the path to save
path = os.path.join(path, keyword[1:])
os.mkdir(path)
path

#download with wget
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
    
#save images to pc
path = os.getcwd()   #get the path to save
path = os.path.join(path, keyword[1:])
os.mkdir(path)
path
