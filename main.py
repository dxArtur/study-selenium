from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()

#options.add_argument("--headless=new")
driver = webdriver.Edge(options=options)
driver.get("https://dxartur.github.io/portfolio/")
element = driver.find_element(by=By.ID, value="greet")
print(element.text)
driver.close()