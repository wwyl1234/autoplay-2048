"""This is software meant to autoplay the game called 2048."""

import os
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def is_game_over(browser):
    """Returns true if game is over. Otherwise, returns False."""
    try:
        browser.find_element_by_class_name('game-over')
        return True
    except NoSuchElementException:
        return False

def al_strategy(browser):
    """This strategy is from the book 'Automate the Boring Stuff with Python' by Al Sweigart.

    The strategy is to move up, right, down and then left and then repeat.
    """

    html_elem = browser.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.UP)

    # need to repeat getting the html elem to avoid error when browser refreshes
    html_elem = browser.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.RIGHT)

    html_elem = browser.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.DOWN)

    html_elem = browser.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.LEFT)


def init_argparse():
    """Initalizes the argparser."""
    parser = argparse.ArgumentParser(
        usage="%(prog)s [FILEPATH] ",
        description="Autoplays 2048 via Firefox browser given the filepath of the geckodriver."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 1.0.0"
    )

    parser.add_argument('path',
                       metavar='path',
                       type=str,
                       help='the filepath to the geckodriver')
    return parser

if __name__ == "__main__":

    arg_parser = init_argparse()
    args = arg_parser.parse_args()
    gecko_path = args.path

    if not os.path.isfile(gecko_path):
        print('The file does not exist')
        sys.exit()

    firefox_browser = webdriver.Firefox(executable_path=gecko_path)
    firefox_browser.get('https://gabrielecirulli.github.io/2048/')

    while not is_game_over(firefox_browser):
        # This is algorithm from book which says to repeat up, right, down and left.
        al_strategy(firefox_browser)

    # Either close the browser or stop this program to stop running the program.
