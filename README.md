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
- Make sure the file is in csv format (If not you can change your file into csv using some available online tools.) <br>
- Name should be entered along with the .csv extension <br>

```sh
from selenium import webdriver
import time
import csv
```
#### Taking data from CSV Files

```sh
def sheet(sheet):
    file = open(sheet, mode='rt')
    reader = csv.reader(file)
    rownum = 0
    val = []
    for row in reader:
        # Save header row.
        if rownum == 0:
            header = row
        # save other data
        else:
            val.append(row)
        rownum += 1

    file.close()
    return (header, val)
```
#### We enter data using two for loops as we have taken data into two lists : Topic and Value

```sh
for i in range(len(value)):
        for j in range(len(topic)):
            if (j == 0):
                data = str(topic[j]) + ' : ' + str(value[i][j])
            else:
                data = data + '\n' + str(topic[j]) + ' : ' + str(value[i][j])
```

#### If you want to go headless just uncomment these two lines

```sh
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
```

## License:

#### MIT

**Free Software, Hell Yeah!**
