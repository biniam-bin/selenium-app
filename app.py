# from selenium import webdriver
# import os
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# while True:
#     s=Service(ChromeDriverManager().install())
#     op = webdriver.ChromeOptions()
#     op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#     op.add_argument("--headless")
#     op.add_argument("--no-sandbox")
#     op.add_argument("--disable-dev-sh-usage")

#     driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=op, service=s)
#     driver.get("https://bit.ly/3CPQ4B7")


# # print(driver.page_source)





from selenium import webdriver


while True:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_options)
    try:
        browser.get("https://bit.ly/3CPQ4B7")
        print("Page title was '{}'".format(browser.title))
    finally:
        browser.quit()