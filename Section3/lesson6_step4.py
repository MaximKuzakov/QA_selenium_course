import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


# answer = math.log(int(time.time()))


@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898",
                                   "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, links):
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    el = browser.find_element(By.TAG_NAME, "textarea")
    el.clear()
    el.send_keys(math.log(int(time.time())))
    btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    )
    btn.click()
    assert browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text == 'Correct!'
