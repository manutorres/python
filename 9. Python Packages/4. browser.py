from typing import Text
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser.get("https://github.com/login")

# link = browser.find_element(
#     By.CLASS_NAME, "HeaderMenu-link--sign-in")

username_box = browser.find_element(By.ID, "login_field")
username_box.send_keys("manutorres")
password_box = browser.find_element(By.ID, "password")
password_box.send_keys("****")
password_box.submit()

profile_link = browser.find_element(
    By.CLASS_NAME, "details-reset")
print("Tag name:", profile_link.tag_name)

link_label = profile_link.get_attribute("innerHTML")
assert "manutorres" in link_label

# browser.quit()
