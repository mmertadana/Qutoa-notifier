from selenium import webdriver
from pushbullet import PushBullet
import time
import os

def sleep_minutes(minutes):
    time.sleep(minutes*60)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

print ("ITU undergraduate course quota program")
print ("Program uses Google Chrome as default.\nIt checks increasements every 15 mins.\nWhen capacity of a course is higher than its enrolls it sends a notification to your mobilephone one time.\nProgram has to be active to send notifications.\nYou can activate auto course selector by entering your ITU Mail and password.\nlinkedin.com/in/mmertadana/")

selector = input ("Do you want to activate auto course adder, you need to enter your ITU mail and password for this? (Y/N) \nPs: I have no idea how to steal them./n"

while upper (selector) != "Y" or "N" "YES" or "NO":
    selector = input ("You entered invalid answer (Y/N): "
                      
if upper (selector) == "Y":
    username = input("ITU Mail: ")
    password = input("Password: ")
                      
access_token = input("Write your Pushbullet access token: ")

course_code = input ("Write your course code(END, ISL etc.): ")

courses = int(input("How many courses you want to check: "))

course_list = []

error = True

for i in range(courses):
    append_crn = input("Write your {}. CRN: ".format(i+1))
    course_list.append(append_crn)
        
driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'))

driver.get("https://www.sis.itu.edu.tr/TR/ogrenci/ders-programi/ders-programi.php?seviye=LS")

while error:

    try:
        
        pb = PushBullet(access_token)

        code = driver.find_element_by_xpath ("//*[contains(text(), '{}')]".format (course_code.upper()))
        code.click()

        show = driver.find_element_by_xpath ("/html/body/div/div[2]/div/div[1]/form/input")
        show.click()    

        for i in range(len(course_list)):
            crn = driver.find_element_by_xpath ("//*[contains(text(), '{}')]".format (course_list[i]))
            capacity = crn.find_element_by_xpath ("./../td[10]")
            enroll = crn.find_element_by_xpath ("./../td[11]")
            course_name = crn.find_element_by_xpath ("./../td[3]")
            if (int(capacity.text) > int(enroll.text)):
                push = pb.push_note (course_name.text, "{}'s has quota".format(course_name.text))
                if upper (selector) == "Y":
                    browser.get("https://kepler-beta.itu.edu.tr/ogrenci/DersKayitIslemleri/DersKayit")
                    username_path = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_tbUserName']")
                    password_path = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_tbPassword']")
                    login_path = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_btnLogin']")
                    username.send_keys ("adana18")
                    password.send_keys ("Mandalina0.")
                    login.click()

                    
                    crn1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-wrapper']/div[2]/div/div/div[3]/div/form/div[1]/div/div[1]/div/input"))
                    )
                    crn1.send_keys(course_list.pop(i))
                    enter = browser.find_element_by_xpath ("//*[@id='page-wrapper']/div[2]/div/div/div[3]/div/form/button")
                    enter.click()

                    another_enter = browser.find_element_by_xpath ("//*[@id='modals-container']/div/div[2]/div/div[3]/button[2]")
                    another_enter.click()
                course_list.pop(i)
                    
                                            
        sleep_minutes (15)
        driver.refresh()

    except IOError:
        error = True


    
