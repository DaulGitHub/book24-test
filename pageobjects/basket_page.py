from pageobjects.base import BasePage


class BasketPage(BasePage):

    url = "/personal/cart/"

    @property
    def checkout_button(self):
        element = self._browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[4]/div[2]/div")

        return element
