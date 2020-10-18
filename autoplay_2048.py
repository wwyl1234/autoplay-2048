"""This is software meant to autoplay the game called 2048."""

import os
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def is_game_over(driver):
    """Returns true if game is over. Otherwise, returns False."""
    try:
        driver.find_element_by_class_name('game-over')
        return True
    except NoSuchElementException:
        return False


def al_strategy(driver):
    """This strategy is from the book 'Automate the Boring Stuff with Python' by Al Sweigart.

    The strategy is to move up, right, down and then left and then repeat.
    """

    html_elem = driver.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.UP)

    # need to repeat getting the html elem to avoid error when browser refreshes
    html_elem = driver.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.RIGHT)

    html_elem = driver.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.DOWN)

    html_elem = driver.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.LEFT)


def check_file_exists(filepath):
    """Returns true if filepath exists. Otherwise, returns false."""
    if not os.path.isfile(filepath):
        print(f"""The file does not exist at {filepath}.""")
        sys.exit()


def init_webdriver(browser_name, webdriver_filepath):
    """Returns the Selenium webdriver object with browser's name and
     its webdriver filepath is needed."""

    browser_name_lower = browser_name.lower()
    if browser_name_lower == "firefox":
        # Selenium and Firefox browser needs the geckodriver and its filepath

        check_file_exists(webdriver_filepath)
        return webdriver.Firefox(executable_path=webdriver_path)
    if browser_name_lower == "safari":
        # Selenium and Safari browser needs user to enable the
        # 'Allow Remote Automation' option in Safari's Develop menu to control Safari via WebDriver

        return webdriver.Safari()
    if browser_name_lower in ("chrome", "googlechrome"):
        # Selenium and Google Chrome browser needs the corresponding chromedriver and its filepath

        check_file_exists(webdriver_filepath)
        return webdriver.Chrome(executable_path=webdriver_path)

    # Browser is not supported.
    print(f"""This program does not support {browser_name}.""")
    sys.exit()


def init_argparse():
    """Initalizes the argparser."""
    parser = argparse.ArgumentParser(
        usage="%(prog)s [BROWSER_NAME] --filepath [WEBDRIVER_PATH if needed]",
        description="Autoplays 2048 via supported browsers that may require \
            filepath of the webdriver."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 1.0.0"
    )

    parser.add_argument('browser',
                        metavar='browser',
                        type=str,
                        help='the name of the web browser. Firefox|Chrome|Safari')

    parser.add_argument('--filepath',
                       dest='filepath',
                       help='the filepath to the webdriver')
    return parser


if __name__ == "__main__":

    arg_parser = init_argparse()
    args = arg_parser.parse_args()
    browser = args.browser
    webdriver_path = args.filepath

    chosen_driver = init_webdriver(browser, webdriver_path)
    chosen_driver.get('https://gabrielecirulli.github.io/2048/')

    while not is_game_over(chosen_driver):
        # This is algorithm from book which says to repeat up, right, down and left.
        al_strategy(chosen_driver)

    # Either close the browser or stop this program to stop running the program.
