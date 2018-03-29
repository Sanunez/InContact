# Script Name: InContact350047.py
# Date: 02/02/2018 (February 2, 2018)
# Description: This script will run daily, it will access the log in page for incontact.com and download the
# specific report 350047 and download daily reports in a month-to-yesterday range.
# Developed by Sergio A. Nunez and Joel Gutierrez
# Collaborators: Amanda De Leon

import os
import re
import time

from datetime import datetime, date, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Starting Process...")

opts = webdriver.ChromeOptions()
opts.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\deleona\PycharmProjects\InContact350047",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# SET UP Chrome
driver = webdriver.Chrome(chrome_options = opts)
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.get("https://login.incontact.com/inContact/Login.aspx?ReturnUrl=%2f")

# Get the Date and the date range.
default_date = datetime.strptime(str(date.today()), '%Y-%m-%d').str
ftime('%m/%d/%Y')
file_date = datetime.strptime(str(date.today()), '%Y-%m-%d').strftime('%m-%d-%Y')
d_date = default_date.split("/")
print("Default Date: " + default_date)
print("File Date: " + file_date)
date1 = datetime.strptime(str(date.today() - timedelta(1)), '%Y-%m-%d').strftime('%m/%d/%Y')
print("Date 1: " + str(date1))
date_1a = re.split("/", str(date1))
date2 = datetime.strptime(str(date.today().replace(day = 1)), '%Y-%m-%d').strftime('%m/%d/%Y')
print("Date 2: " + str(date2))
date_2a = re.split("/", str(date2))

# Open the REP file that contains data to log in
with open("REP.txt", "r") as file:
    data = file.read().splitlines()
file.close()

# LOG IN
login = driver.find_element_by_xpath("//input[@placeholder='Username']")
login.clear()
login.send_keys(data[1] + Keys.TAB + data[2] + Keys.RETURN)
driver.set_page_load_timeout(30)
print("Logged in")

# Click on Reporting/Analytics
repanalytics = driver.find_element_by_link_text("Reporting/Analytics")
repanalytics.click()
driver.implicitly_wait(20)

# Click on the 1st Data Download Link
datadl_1 = driver.find_element_by_link_text("Data Download")
datadl_1.click()
driver.implicitly_wait(20)

# Search through the links until you find the 2nd Data Download Link and click on it
list = datadl_1.find_elements_by_xpath("//*[@href]")
for links in list:
    if "https://home-c16.incontact.com/inContact/Manage/Reports/DataDownload.aspx" in links.get_attribute("href"):
        links.click()
        break
driver.implicitly_wait(20)
time.sleep(10)

# Fill in the date.
date_values = driver.find_element_by_xpath("*//input[@value='" + default_date + " - " + default_date + "']")
date_values.click()
date_values.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
date_values.send_keys(date_1a[0] + date_1a[1] + date_1a[2] + date_2a[0] + date_2a[1] + date_2a[2] + Keys.RETURN)
time.sleep(5)

# Search for the report
searchreport = driver.find_element_by_xpath("//input[@placeholder='Search']")
searchreport.clear()
searchreport.send_keys(data[0] + Keys.RETURN)
time.sleep(5)
driver.implicitly_wait(20)

# Get the Report
driver.find_element_by_xpath("*//tr[@id='ctl00_ctl00_BaseContent_ReportOptions_ddroReportOptions_tcReports_tbpnlReports_agvReports_gridView_ctl02']").click()
time.sleep(5)
driver.implicitly_wait(20)

# Date To Range set up
driver.find_element_by_xpath("//input[@value='" + str(date1) + " - " + str(date2) + "']").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='datePresetPicker-UL']/li[9]/a").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='daterangepicker-ctl00_ctl00_BaseContent_ReportOptions_ctrlDatePicker_txtDate']/div/div/button").click()
driver.implicitly_wait(20)
time.sleep(5)

# Fields and Download
driver.find_element_by_xpath("//input[@id='ctl00_ctl00_BaseContent_ReportOptions_chkHeaderRow']").click()
driver.find_element_by_xpath("//*[@id='ctl00_ctl00_BaseContent_ReportOptions_btnDownload_ShadowButtonSpan']").click()
driver.implicitly_wait(20)

# Close Browser in 5 minutes
time.sleep(300)

os.rename("Data.csv", file_date + ".csv")
driver.close()
driver.quit()

print("DONE")
