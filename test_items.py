from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
time.sleep(30)

def test_launch_for_different_languages(browser):
    browser.get(link)
    assert browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket"), 'basket button not found'
    
    