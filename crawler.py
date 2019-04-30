
from selenium import webdriver
import time, csv, parameters

# defining new variable passing two paramaters
#writer = csv.writer(open(parameters.file_name, 'wb'))

# writerow() method to the write to the file object
#writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/usr/bin/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# get all elements by class
username = driver.find_element_by_id('login-email')
log_in_button = driver.find_element_by_id('login-submit')
password = driver.find_element_by_id('login-password')

# send info to login
username.send_keys(parameters.linkedin_username)
password.send_keys(parameters.linkedin_password)


#click to login
log_in_button.click()

time.sleep(2)

#click para o link de conexões
driver.find_element_by_id('mynetwork-nav-item').click()

time.sleep(2)

#click para abrir os perfis com conexões
driver.find_element_by_partial_link_text('Conexões').click()

time.sleep(2)

connections_names = []

for i in driver.find_element_by_class_name('mn-connection-card__name'):
    connections_names.append(i)
print("###########################")
print(connections_names)
print("###########################")
print(parameters.message)
