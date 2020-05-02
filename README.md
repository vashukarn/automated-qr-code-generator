# automated-qr-code-generator

[![N|Solid](https://vashukarn.github.io/top-logo.png)](https://vashukarn.github.io/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/vashukarn/automated-qr-code-generator)

## General Information

This script helps to automate browser using selenium to generate QR codes taking data from CSV file. It is a python automated script that creates QR codes according to the data provided in CSV file at once. I used the selenium web browser to generate QR codes.

## Prerequisites

These should run without any error: <br>

- Selenium Module should be installed <br>
- Chrome webdriver should be installed <br>
- Path of Chrome Browser should be added to PATH <br>

```sh
from selenium import webdriver
import time
import csv
```

#### If you want to go headless just uncomment these two lines

```sh
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
```

## License:

#### MIT

**Free Software, Hell Yeah!**
