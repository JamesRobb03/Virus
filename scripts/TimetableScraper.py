#imports
import urllib2
import time
from bs4 import BeautifulSoup
from selenium import webdriver

def findTimetable(studentID):
    
    strStudent = str(studentID)
    browser = webdriver.Chrome('C:/Users/ADMIN/Downloads/chromedriver.exe')
    nextID = False
    error = "400  Bad Request"

    browser.get('https://timetable.dundee.ac.uk:8084/reporting/textspreadsheet?objectclass=student+set&idtype=id&identifier='+strStudent+'/1&t=SWSCUST+student+set+textspreadsheet&days=1-7&weeks=13-23&periods=1-28&template=SWSCUST+student+set+textspreadsheet')
    while nextID == False:
        try:
            page = urllib2.urlopen('https://timetable.dundee.ac.uk:8084/reporting/textspreadsheet?objectclass=student+set&idtype=id&identifier='+strStudent+'/1&t=SWSCUST+student+set+textspreadsheet&days=1-7&weeks=13-23&periods=1-28&template=SWSCUST+student+set+textspreadsheet')
            soup = BeautifulSoup(page, 'html.parser')
            is404 = soup.find('h1')

            if is404 == error:
                studentID = studentID+1
                strStudent = str(studentID)
            else:
                viewNext = raw_input(":")
                if viewNext == ".":
                    browser.get('https://timetable.dundee.ac.uk:8084/reporting/textspreadsheet?objectclass=student+set&idtype=id&identifier='+strStudent+'/1&t=SWSCUST+student+set+textspreadsheet&days=1-7&weeks=13-23&periods=1-28&template=SWSCUST+student+set+textspreadsheet')
                    studentID = studentID+1
                    strStudent = str(studentID)
                elif viewNext == "quit":
                    nextID = True
        except:
            studentID = studentID+1
            strStudent = str(studentID)

findTimetable(180010702)



