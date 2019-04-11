from features.settings import BASE_URL, personas
import os
from selenium import webdriver


chromedriver_path = os.path.join("drivers", "chromedriver", "chromedriver")


def before_all(context):
    context.base_url = BASE_URL
    context.personas = personas


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome(chromedriver_path)
    context.browser.implicitly_wait(10)
    context.browser.fullscreen_window()


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    context.browser.quit()


def after_feature(context, feature):
    pass


def after_all(context):
    pass
