from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")

