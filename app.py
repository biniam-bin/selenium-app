from selenium import webdriver

while True:
    op = webdriver.ChromeOptions()
    op.add_argument("--headless")
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-sh-usage")

    driver = webdriver.Chrome(options=op)
    driver.get("https://bit.ly/3CPQ4B7")


# print(driver.page_source)