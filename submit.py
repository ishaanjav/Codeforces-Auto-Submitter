import time
import selenium #need to install selenium to run this auto submitter. Check the README setup instructions.
from time import sleep
from selenium import webdriver
import sys, os

# RUNNING THE Codeforces Auto Submitter
# In the terminal, type:    python3 submit.py <PROBLEM #>
# and replace PROBLEM # with the problem you want to submit code for like 234C, 106E, etc

# EXAMPLE:
# python3 submit.py 234C
# This automatically submits code for Codeforces Problem 234C in whichever language I specify.


# STEP 1: Uncomment one of the below based on what Web Browser you below.
# browser = webdriver.Chrome()
# browser = webdriver.Safari()
# browser = webdriver.Firefox()

problem = sys.argv[1]  # Problem ID like 234C
number = problem[:-1]  # Number part of the ID like 234
letter = problem[-1:]  # Problem Letter (A, B, C...)

browser.get("https://codeforces.com/problemset/problem/"+ number+"/" + letter)

# Sign in button
enter = browser.find_element_by_css_selector("#header > div.lang-chooser > div:nth-child(2) > a:nth-child(1)")
enter.click()

# STEP 2: Enter your username and password
username = browser.find_element_by_css_selector("#handleOrEmail")
password = browser.find_element_by_css_selector("#password")
# Enter your username below
username.send_keys("<USERNAME HERE>")
# Enter your password
password.send_keys("<PASSWORD HERE>")

# Login button
login = browser.find_element_by_css_selector("#enterForm > table > tbody > tr:nth-child(4) > td > div:nth-child(1) > input")
login.click()

# The program has to login in before it can upload the file
#  You may decrease or increase this amount based on how fast it logs in
#  Otherwise, you may run into an error, and you can check: https://github.com/ishaanjav/Codeforces-Auto-Submitter/blob/master/README.md
sleep(3)

# Step 3:
# Enter the path/directory where your solution is located.
path = "<FILE PATH HERE>"

file = "";

# Step 4
# Replace cpp with the type of file you want to submit.
file_type = "cpp"
for f_name in os.listdir(path):
	# This assumes that your solution file looks starts with the Problem ID and ends with file_type (variable above) like "123C_Hello__World.cpp"
	#  If your file name is different, you can change the condition below to select the correct file based on how you name your files.
	if f_name.startswith(problem) and f_name.endswith(file_type):
		file = f_name
		break

# Upload your file
browser.find_element_by_xpath('''//*[@id="sidebar"]/div[5]/div[4]/form/table/tbody/tr[3]/td[2]/input''').send_keys(path+"/"+file)

# Submit the solution
submit = browser.find_element_by_xpath('''//*[@id="sidebar"]/div[5]/div[4]/form/table/tbody/tr[4]/td/div/div[2]/input''')
submit.click()
