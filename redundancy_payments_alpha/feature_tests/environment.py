from splinter import Browser
from steps.test_support.app import App
import logging

selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
selenium_logger.setLevel(logging.WARNING)


def before_all(context):
    context.app = App()
    context.app.run()
    context.browser = Browser(driver_name="firefox")


def after_all(context):
    context.browser.quit()
    context.app.stop()

