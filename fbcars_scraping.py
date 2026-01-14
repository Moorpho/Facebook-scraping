from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

EMAIL = "твій_email"
PASSWORD = "твій_пароль"

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://www.facebook.com")
time.sleep(3)

driver.find_element(By.ID, "email").send_keys(EMAIL)
driver.find_element(By.ID, "pass").send_keys(PASSWORD)
driver.find_element(By.NAME, "login").click()

time.sleep(10)
