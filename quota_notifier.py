from selenium import webdriver
from pushbullet import PushBullet
import numpy as np
import time

def sleep_minutes(minutes):
    time.sleep(minutes*60)

print ("ITU undergraduate course quota program")
print ("Program uses Google Chrome as default.\nIt checks increasements every 15 mins.\nWhen capacity of a course is higher than its enrolls it sends a notification to your mobilephone one time.\nProgram has to be active to send notifications.")

access_token = input("Write your Pushbullet access token: ")

course_code = input ("Write your course code(END, ISL etc.): ")

print (course_code.upper())

courses = int(input("How many courses you want to check: "))

course_list = []

error = True

for i in range(courses):
    append_crn = input("Write your {}. CRN: ".format(i+1))
    course_list.append(append_crn)
    
driver = webdriver.Chrome()

driver.get("https://www.sis.itu.edu.tr/TR/ogrenci/ders-programi/ders-programi.php?seviye=LS")

while error:

    try:
        
        pb = PushBullet(access_token)

        end = driver.find_element_by_xpath ("//*[contains(text(), '{}')]".format (course_code))
        end.click()

        show = driver.find_element_by_xpath ("/html/body/div/div[2]/div/div[1]/form/input")
        show.click()    

        for i in range(len(course_list)):
            crn = driver.find_element_by_xpath ("//*[contains(text(), '{}')]".format (course_list[i]))
            capacity = crn.find_element_by_xpath ("./../td[10]")
            enroll = crn.find_element_by_xpath ("./../td[11]")
            course_name = crn.find_element_by_xpath ("./../td[3]")
            if (int(capacity.text) > int(enroll.text)):
                push = pb.push_note (course_name.text, "{}'s has quota".format(course_name.text))
                course_list.pop(i)
                            
        sleep_minutes (15)
        driver.refresh()

    except OSError:
        error = True
