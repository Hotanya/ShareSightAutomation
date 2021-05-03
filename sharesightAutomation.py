from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
#Navigate to Vanguard holding
browser.get('https://portfolio.sharesight.com/holdings/9426381')

#################### Authentication #############################
#getting creds
file = open('creds') 
  
# read the content of the file opened 
pass_file = file.readlines() 

# locating ‘Email or Phone’ element using ‘id’ attribute
userName = browser.find_element_by_id('user_email')

# Entering username
userName.send_keys(pass_file[0]) #use env variable!


password = browser.find_element_by_id('user_password')
password.send_keys(pass_file[1])

# locating ‘login button’ element using the ‘id’ attribute and pressing ‘Enter’
browser.find_element_by_id('recaptcha_submit').send_keys(Keys.ENTER)
#################### Authentication #############################
sleep(10)
browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[1]/div/div[1]/button').click()
