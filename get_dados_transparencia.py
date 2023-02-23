from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver (you can use other drivers like Firefox, Safari, etc.)
driver = webdriver.Chrome()

# Open the web page
driver.get("https://transparencia.joaopessoa.pb.gov.br/#/dados-abertos")

# Find the element with "savings" written on it and click it
try:
    savings_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'savings')]"))
    )
    savings_element.click()
    
    # Wait for the next page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "card-body"))
    )
    
    # Find the list of span elements and print out their text values
    span_elements = driver.find_elements("class name","card-body")
    for span in span_elements:
        print(span.text)
    
finally:
    # Close the browser window
    driver.quit()
