from selenium import webdriver
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys("username@email.com")
driver.find_element_by_id("pass").send_keys("password")
driver.find_element_by_name("login").click()
