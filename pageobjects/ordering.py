from pageobjects.base import BasePage


class Receiver(BasePage):

    @property
    def name_field(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/div/div/form/div[2]/div/div[3]/div/div/div[2]')

        return element

    @property
    def further_button(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/div/div/form/div[5]/div/div[1]/button')

        return element


class Delivery(BasePage):

    @property
    def courier_button(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[3]/div/div[2]')

        return element

    @property
    def block_title(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[4]/div/div[1]/div/label/div/div[2]/div[1]')

        return element

    @property
    def address_field(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[4]/div/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div/div/div/input')

        return element

    @property
    def address_popup(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[4]/div/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div[2]')

        return element


    @property
    def office_num_field(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[4]/div/div[2]/form/div[2]/div/div[2]/div/div[2]/div/div/input')

        return element

    @property
    def further_button(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[6]/div/div[1]/button')

        return element


class Ordering(BasePage):

    def __init__(self, browser):

        super().__init__(browser)

        self.receiver = Receiver(browser)
        self.delivery = Delivery(browser)
        self.payment = Payment(browser)
        self.confirmation = Confirmation(browser)

    @property
    def receiver_button(self):
        element = self._browser.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[1]/div/div/a[1]/div[2]')

        return element


class Payment(BasePage):

    @property
    def title(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[1]/div')

        return element

    @property
    def further_button(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[4]/div/div[1]/button')

        return element


class Confirmation(BasePage):

    @property
    def title(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[1]/div')

        return element

    @property
    def address_title(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div')

        return element

    @property
    def coast_delivery_title(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[2]/div/div[2]/div/div[2]/div/div[3]/div')

        return element

    @property
    def payment_title(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[2]/div/div[3]/div/div[2]/div/div/div/b')

        return element

    @property
    def payer_type_title(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[2]/div/div[1]/div/div[2]/div/div[1]/div')

        return element

    @property
    def name_title(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/b')

        return element

    @property
    def mail_title(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[2]/div/div[1]/div/div[2]/div/div[3]/div')

        return element

    @property
    def phone_title(self):
        element = self._browser.find_element_by_xpath(
            '//*[@id="order-layout-content"]/div/form/div[2]/div/div[1]/div/div[2]/div/div[4]/div')

        return element
