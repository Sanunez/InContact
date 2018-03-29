InContact version 1.0 02/22/2018

GENERAL USAGE NOTES
--------------------
-This program is built to log in to InContact with an extracted username and password
to download a specified report, pre-written in a text file.

REQUIREMENTS
-------------
-For this program, you will need the following installed:
 * Google Chrome
 * Chromedriver 
 * Python 2.7
 * Pip (Already comes with Python 2.7, but need to set up Path Variables.)
 * Selenium
 * Microsoft Excel (this is not needed, but it is used for file verification)
-The download links will be provided in below the Procedure To Set Up section.
-------------
PROCEDURE TO SET UP
--------------------
After you download the exe file, you will need to download Google Chrome if you haven't already. 

Next, you will install selenium through pip, go to your command prompt, and change to the 
directory "C:\Python27" type in the command "pip install -U selenium". After installment ensure you 
have selenium installed by going to your Python27 directory and look for the selenium folder.

After downloading, you will also require that you download chromedriver.exe. 

NOTE: Download the chromedriver.exe on a location you can remember, set up your Path 
Environment Variables to the location of the chromedriver.exe, it is recommended 
to copy within your Python Folder inside either or selenium directories 
e.g. "C:\Python27\selenium\webdriver" or  "C:\Python27\Lib\site-packages\selenium\webdriver\chrome"

Next, you will need to download Python 2.7 and install it, during installation, make sure you click 
the "Add Python to PATH" during installation, when you're done installing, open up your 
command prompt and type in "python", exit python using exit(), and then type in the command
prompt "pip". If both "python" and/or "pip" were not successful in the command prompt, you will 
have to add them manually to your Path Environment Variables.

When everything has been setup, launch the exe application.
---------------------
DOWNLOAD LINKS
---------------------
Google Chrome: https://www.google.com/chrome/
Chromedriver: https://sites.google.com/a/chromium.org/chromedriver/
Python 2.7: https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi
Pip will come included with the Python 2.7 installer.
Selenium: Can be installed with "pip install -U selenium"
---------------------
Email: sergio.nunez@ipacc.com