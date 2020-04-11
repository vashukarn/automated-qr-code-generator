from selenium import webdriver
import time
import csv

# Install selenium browser in case you don't have it preinstalled it before

# Path of the csv file from which data is extracted
reader = csv.DictReader(open(r'C:\Users\Venom\Downloads\halwa.csv')) 
print("Program Started")
driver.maximize_window()
# we will be using a site named qr code-monkey.com
driver.get("https://www.qrcode-monkey.com/#text")
time.sleep(3)
for raw in reader:
    # the columns to be imported
    enroll = raw.get('Enroll ID')
    name = raw.get('Name')
    father = raw.get("Father's Name")
    address = raw.get('Address')
    phone = raw.get('Phone')
    cls = raw.get('Class')
    # format in which we need to store data in a qr code
    halwa = 'Enrollment Number : ', enroll, '\n', 'Name : ', name, '\n', "Father's Name : ", father, '\n', 'Address : ', address, '\n', 'Phone : ', phone, '\n', 'Class : ', cls, '\n'
    print(enroll)
    driver.find_element_by_name("qrcodeText").clear()
    driver.find_element_by_name("qrcodeText").send_keys(halwa)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/button[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/button[2]").click()
    time.sleep(2)
