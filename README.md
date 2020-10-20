# autoplay-2048


This is software to play the game 2048 on the site https://gabrielecirulli.github.io/2048/ which redirects to https://play2048.co/ .

This is inspired by "Automate the Boring Stuff with Python" by Al Sweigart.



```
usage: autoplay_2048.py [BROWSER_NAME] --filepath [WEBDRIVER_PATH if needed]

Autoplays 2048 via supported browsers that may require filepath of the
webdriver.

positional arguments:
  browser              the name of the web browser. Firefox|Chrome|Safari

optional arguments:
  -h, --help           show this help message and exit
  -v, --version        show program's version number and exit
  --filepath FILEPATH  the filepath to the webdriver
  --loop               set loop to be True which will keep playing the game till user quits
```


An example of running this would look something like this (if you are using MacOSX):

`python3 autoplay_2048.py Firefox /path/to/geckodriver/`


This has been tested on MacOSX. 

To get this working for the Firefox browser, you would need to install geckodriver and need the location of the installed geckodriver.

To get this working for the Chrome browser, you would need to install chromedriver and need the location of the installed chromedriver.

To get this working for the Safari browser, you would need to enable the 'Allow Remote Automation' option in Safari's Develop menu to control Safari via WebDriver.







Note that filepaths are different on different operating systems. 