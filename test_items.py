import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:
    
    def test_button_add_to_basket_is_visible(self, browser):
        browser.get(link)

        """Время ожидания для визуальной проверки языка кнопки указано как в задании, 30с.
        Можно изменить на меньшее"""
        time.sleep(30)
        
        assert browser.find_element_by_css_selector("button.btn-add-to-basket")
