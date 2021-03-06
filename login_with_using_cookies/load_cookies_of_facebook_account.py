"""Module for loading cookies for the domain."""

import time

import config
from utilities import Utilities


class LoadCookies(Utilities):
    """Class for loading cookies for the domain."""

    def __init__(self, name_of_cookies_file):
        """Method for loading cookies for the domain."""

        config.DOMAIN = "https://www.facebook.com"
        self._set_up()

        # Go to URL.
        self.driver.get(config.DOMAIN)
        time.sleep(config.DELAY2)

        # Loading user's pre-saved cookies.
        self.load_cookie(name_of_cookies_file)
        time.sleep(config.DELAY2)

        # Refresh the page to see the changes (user should be logged in).
        self.refresh_page()
        time.sleep(config.DELAY2 * 5)

        self._tear_down()


if __name__ == '__main__':
    COOKIE = LoadCookies("ratmir.asanov.demo")
