from selenium import webdriver
import os

while True:
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    op.add_argument("--headless")
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-sh-usage")

    driver = webdriver.Chrome(executable_path=os.environ.path("CHROMEDRIVER_PATH"), options=op)
    driver.get("https://bit.ly/3CPQ4B7")


# print(driver.page_source)