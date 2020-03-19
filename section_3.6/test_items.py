link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_available(browser):
	browser.get(link)
	add_to_basket_btn = browser.find_element_by_css_selector("#add_to_basket_form .btn-add-to-basket")

	assert add_to_basket_btn