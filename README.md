# Codeforces Auto Submitter
This Python script automates the process of uploading and submitting your code for Codeforces problems.

**You simply have to run 
```python3 submit.py <PROBLEM #>``` 
from terminal to have your solution to the problem submitted.**

## Example
**```python3 submit.py 234C```**

The code above will ***automatically*** submit your solution to Problem 234C on the Codeforces website. Read the [**Setup**](https://github.com/ishaanjav/Codeforces-Auto-Submitter#setup-1-minute-or-less) instructions below to get started.

--------- 

## Setup (1 minute or less)
### 1. Install Selenium
Run any of the following commands - *(based on what package manager you have)* - in your terminal to install selenium. 
Selenium is required to do the browser automation.
- ```pip3 install selenium``` **OR**
- ```sudo easy_install selenium``` **OR**
- ```brew install selenium-server-standalone```

### 2. One-time Setup for ```submit.py``` file
Follow the short steps below and you're good to go!
1. On **lines 17-19** uncomment the Web Browser you have.
2. On **lines 36 and 38** enter your username and password. This is so that the program can log into your Codeforces account. 
 - **If you look at the program *(just a single python file)* you'll see that it does not store or send information anywhere and the code has comments for every step in the process.**
3. On **line 51** copy-paste the path/directory where your solution code is stored.

***Optional:***

4. On **line 57** change the file extension based on the language your code is in.
- **EX:** If you are submitting a C++ file, type "cpp". If your solution is in Java type "java", etc.
5. The auto submitter will submit a file starting with the Problem ID *(234C, 1045E, etc)* and ending in the file extension you specified.
- If you name your solution with a different convention, you can modify the condition in **line 61** to select the correct file

#### That's it! You're ready to use the Auto Submitter to have your Codeforces solutions automatically submitted with a single command!
#### Just run ```python3 submit.py PROBLEM_ID``` and hit enter!

----

## Questions
If you have questions or ran into errors, email me at ijapps101@gmail.com

----

## Updates
The Auto Submitter is a super simple, effortless way to submit your Codeforces solutions. 

If you have any features in mind that you would like for the Auto Submitter to have, feel free to email me **ijapps101@gmail.com** or contact me through [**my website**](https://ij-apps.wixsite.com/android).

----

# Learn Android App Development
Do you want to learn how to make your own Android apps?
I have a [**YouTube Channel**](https://www.youtube.com/IJApps) called [**IJ Apps**](https://www.youtube.com/IJApps) for teaching Android app development to programmers of all levels.

For those just starting out, I have a [**Beginner Tutorial Playlist**](https://www.youtube.com/playlist?list=PLLmkb5CTw5rSei_aHOHIUK8gfkJNjWFtn) of 22 videos in sequential order to get you started!

**If you're interested check out the channel!**

**Playlists:**
 - [**Beginner Tutorial Playlist**](https://www.youtube.com/playlist?list=PLLmkb5CTw5rSei_aHOHIUK8gfkJNjWFtn)
 - [**Short Bits Playlist** (32 videos)](https://www.youtube.com/playlist?list=PLLmkb5CTw5rTBoFCUc0AfALPev9wbRSoK)
 - [**Android Studio How To's**](https://www.youtube.com/playlist?list=PLLmkb5CTw5rSmNluqESGN2yq_DY4vgnYt)

**Tutorials:** 
 - [**EditText Tutorials**](https://www.youtube.com/playlist?list=PLLmkb5CTw5rQv0wBLDnHvpAtXdcyIfZpV)
 - [**AlertDialog Tutorials**](https://www.youtube.com/playlist?list=PLLmkb5CTw5rSCT3szl8VLBjKhLC8ttt8B)
 - [**Animations Programatically**](https://www.youtube.com/playlist?list=PLLmkb5CTw5rQoOi3LpxY720Dmd09f7e2_)
 - [**Spinner** *(Dropdown)* **Tutorials**](https://www.youtube.com/playlist?list=PLLmkb5CTw5rTQ4bjWZdOQbrHPsZexcdef)
