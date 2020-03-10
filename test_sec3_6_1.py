import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def answer():
	return str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestLogin(object):
	def test_check_correct_answer(self, browser, number):
	    link = f"https://stepik.org/lesson/{number}/step/1"
	    browser.get(link)

	    browser.implicitly_wait(50)
	    # ввести в textarea заданное число
	    textarea = browser.find_element_by_tag_name("textarea")
	    textarea.send_keys(answer())

	    # Нажать кнопку "Submit"
	    submit = browser.find_element_by_tag_name("button")
	    submit.click()

	    # проверить, верно ли введенное значение
	    browser.implicitly_wait(50)
	    conclusion = browser.find_element_by_class_name("smart-hints__hint")
	    text_conclusion = conclusion.text
	    assert "Correct!" in text_conclusion
