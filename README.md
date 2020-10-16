# autoplay-2048


This is software to play the game 2048 on the site https://gabrielecirulli.github.io/2048/ which redirects to https://play2048.co/ .

This is inspired by "Automate the Boring Stuff with Python" by Al Sweigart.



To get this working for the Firefox browser, you would need to install geckodriver and need the location of the installed geckodriver.

This has been tested on MacOSX. 




usage: autoplay_2048.py [FILEPATH] 

Autoplays 2048 via Firefox browser given the filepath of the geckodriver.

positional arguments:
  path           the filepath to the geckodriver

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit



An example of running this would look something like this (if you are using MacOSX):
python3 autoplay_2048.py /path/to/geckodriver/

Note that filepaths are different on different operating systems. 