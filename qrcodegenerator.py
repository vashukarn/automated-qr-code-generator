from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import csv

# Taking data from sheet


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


def download():
    driver.find_element_by_class_name('btn-success').click()
    sleep(4)
    driver.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/button[2]').click()


def main():
    data = ''
    driver.maximize_window()
    driver.get('https://www.qrcode-monkey.com/#text')
    for i in range(len(value)):
        for j in range(len(topic)):
            if (j == 0):
                data = str(topic[j]) + ' : ' + str(value[i][j])
            else:
                data = data + '\n' + str(topic[j]) + ' : ' + str(value[i][j])
        driver.find_element_by_id('qrcodeText').clear()
        driver.find_element_by_id('qrcodeText').send_keys(data)
        sleep(1)
        download()
        print('QR Code no : ' + str(i) + ' Downloaded')
        data = ''


# Enter filename here
sheetname = str(input('Input csv file name : '))
# Taking data by header and value
topic, value = sheet(sheetname)
print('Opening QR CODE GENERATOR SITE')

chrome_options = Options()
# Uncomment two lines down if you don't want chrome window to popup and go headless
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')


driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)
main()
