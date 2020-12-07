import os
import time
from datetime import datetime
import subprocess
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def CalTime():
    start = time.time()
    startDisplay = datetime.now()
    print('Start: ', startDisplay.strftime("%H:%M:%S"))
    input()
    end = round(time.time() - start,2)
    endDisplay = datetime.now()
    print('End: ', endDisplay.strftime("%H:%M:%S"))
    time.sleep(1)
    if(end>60):
        end=round(end/60,2)
        print('\n\nTotal time: %s minutes' %end)
    else:    
        print('\n\nTotal time: %s seconds' %end)
    time.sleep(4)
        

def VSCode():
    file = open('main.cpp', 'w')
    file.write('//automation by devilssnare')
    file.write('\n#include <bits/stdc++.h>')
    file.write('\nusing namespace std;')
    file.write('\nint main() {')
    file.write('\n  return 0;')
    file.write('\n}')
    subprocess.Popen(['C:\\Users\\cheta\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe', 'main.cpp'])
    
def CodeChef():
    driver = webdriver.Edge('msedgedriver.exe')
    driver.get('https://www.codechef.com/')

    username = 'devilssnare'
    password = 'My1id@uk'

    driver.find_element_by_id('edit-name').send_keys(username)
    driver.find_element_by_id('edit-pass').send_keys(password)
    driver.find_element_by_id('edit-submit').click()

VSCode()
CodeChef()
CalTime()

