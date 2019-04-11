from time import sleep
from pageobjects.basket_page import BasketPage
from pageobjects.ordering import Ordering
from behave import *


def parse_raw_cookie(cookie):

    cookie = cookie.split("; ")
    parsed = {}
    for row in cookie:
        key_val = row.split("=")
        parsed[key_val[0]] = key_val[1]

    return parsed


@given('Logged as persona "Autotester"')
def step_impl(context):

    context.execute_steps("""
        Given a browser
    """)

    raw_cookie = "BITRIX_SM_location_type=%D0%B3; BX_USER_ID=d7f73fbc427128ca6efecedd7e6a08d2; dd__persistedKeys=[%22user.anonymousId%22]; dd_user.anonymousId=02a7a280-492c-11e9-a200-ade5a006c4d5; _ym_uid=1552878898680441455; _ym_d=1552878898; _ga=GA1.2.1913905480.1552878899; _gid=GA1.2.198401238.1552878899; tracker_ai_user=XSDM9|2019-03-18T03:14:58.807Z; mindboxDeviceUUID=e7d450eb-6702-4155-8ecf-06f2a81e7317; directCrm-session=%7B%22deviceGuid%22%3A%22e7d450eb-6702-4155-8ecf-06f2a81e7317%22%7D; _ym_isad=1; _gcl_aw=GCL.1552878899.~CjwKCAjw4LfkBRBDEiwAc2DSlBcLAdIXZn8xFtPqW1o9LBZVYdsW3Ce5fGdll0hrx-6RT6JMclQt6xoC6VwQAvD_BwE; cto_lwid=9762f1b2-11f2-4e1c-bd7d-793517127447; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; flocktory-uuid=9be9b339-eb29-412a-99d1-f92c086ed506-7; co_hash=SJgEYbxOIDcG3qPC584FSXjOw; co_session=F7azcHuwap; _gac_UA-79355680-1=1.1552878901.CjwKCAjw4LfkBRBDEiwAc2DSlBcLAdIXZn8xFtPqW1o9LBZVYdsW3Ce5fGdll0hrx-6RT6JMclQt6xoC6VwQAvD_BwE; BL_D_PROV=; BL_T_PROV=; ___dmpkit___=22bcdcf6-861f-4819-b127-227b8683874c; jv_enter_ts_X1I9Jp9tMk=1552878903588; jv_visits_count_X1I9Jp9tMk=1; jv_refer_X1I9Jp9tMk=https%3A%2F%2Fwww.google.ru%2F; jv_utm_X1I9Jp9tMk=; BITRIX_SM_location_accept=Y; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; BITRIX_SM_utm_campaign=240682; BITRIX_SM_utm_source=trackad_admitad; BITRIX_SM_location_code=0c5b2444-70a0-4932-980c-b4dc0d3f02b5; BITRIX_SM_location_name=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0+%D0%B3; BITRIX_SM_location_region=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F; book24_user_data_layer_data=%7B%22userid%22%3A%223877859%22%2C%22user_type%22%3A%22user%22%2C%22user_status%22%3A10%7D; PHPSESSID=fm0a53e8p1c5jijrbbijj54hl5; BITRIX_SM_UIDH=870d41f27d2a85c01fe454b7a241ee0e; BITRIX_SM_UIDL=daul_m%40mail.ru; BITRIX_SM_SALE_UID=834627793; BITRIX_SM_LOGIN=daul_m%40mail.ru; _ym_visorc_37971640=w; jv_pages_count_X1I9Jp9tMk=24; amplitude_id_d63f8d40e210615c23acacb0456bab69book24.ru=eyJkZXZpY2VJZCI6IjBhNmRmYmMzLWZiY2UtNDJiOS04ZmU1LWYzMzE3ZjYzMjk5MVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU1Mjg5MzY2ODU0OCwibGFzdEV2ZW50VGltZSI6MTU1Mjg5MzY5NTQ4OSwiZXZlbnRJZCI6MzMsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjozM30=; tmr_detect=1%7C1552893696004; __tld__=null"
    parsed_cookies = parse_raw_cookie(raw_cookie)

    for name in parsed_cookies:
        context.browser.add_cookie({"name": name, "value": parsed_cookies[name]})

    context.browser.refresh()


@given('a browser')
def step_impl(context):
    location = "/?location=0c5b2444-70a0-4932-980c-b4dc0d3f02b5"
    context.browser.get("{}{}".format(context.base_url, location))


@step('basket page')
def step_impl(context):

    context.browser.get("{}{}".format(context.base_url, BasketPage.url))


@step('I press "Оформить заказ" button')
def step_impl(context):

    page = BasketPage(context.browser)
    page.checkout_button.click()


@when('I press "Далее" button')
def step_impl(context):
    sleep(8)
    page = Ordering(context.browser)
    page.receiver_button.click()
    page.receiver.further_button.click()

    assert page.delivery.courier_button is not None


@when('I press "Курьер" button')
def step_impl(context):

    sleep(3)
    page = Ordering(context.browser)
    page.delivery.courier_button.click()

    assert page.delivery.block_title.text == "Курьерская доставка"


@when('I fill address fields')
def step_impl(context):
    page = Ordering(context.browser)
    page.delivery.address_field.clear()
    page.delivery.address_field.send_keys("Хорошёвское шоссе, д 88 стр 1")
    sleep(1)
    page.delivery.address_popup.click()
    sleep(2)
    page.delivery.office_num_field.clear()
    page.delivery.office_num_field.send_keys("4")

    assert page.delivery.block_title.text == "Курьерская доставка"


@when('I press "Далее" button on courier block')
def step_impl(context):

    sleep(2)
    page = Ordering(context.browser)
    page.delivery.further_button.click()


@when('I press "Далее" button on payment block')
def step_impl(context):

    sleep(3)
    page = Ordering(context.browser)
    assert page.payment.title.text == "Выберите способ оплаты"
    page.payment.further_button.click()


@then('I should see confirmation page')
def step_impl(context):

    params = context.table[0]
    page = Ordering(context.browser)

    assert page.confirmation.payer_type_title.text == params["payer type"]
    assert page.confirmation.name_title.text == params["name"]
    assert page.confirmation.mail_title.text == params["mail"]
    assert page.confirmation.phone_title.text == params["phone"]

    assert page.confirmation.title.text == "Подтвердите ваш заказ"
    assert page.confirmation.address_title.text == params["address"]
    assert page.confirmation.coast_delivery_title.text == params["coast delivery"]
    assert page.confirmation.payment_title.text == params["payment"]

