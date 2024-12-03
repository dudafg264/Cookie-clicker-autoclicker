import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(2)

button_language = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[10]")
button_language.click()

time.sleep(2)

starting_time = time.time()
future_time = starting_time + 5 * 60

clicks = 0
now = time.time()

while now < future_time:
    button = driver.find_element(By.ID, "bigCookie")
    button.click()
    clicks += 1
    now = time.time()


elapsed_time = now - starting_time
cps = clicks / elapsed_time
print(f"{cps:.2f} cliques por segundo.")

input("Pressione Enter para encerrar o script...")
driver.quit()
