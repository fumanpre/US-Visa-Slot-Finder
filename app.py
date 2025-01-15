from flask import Flask, render_template, url_for, request, redirect
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Capture the form data
        email = request.form['email']
        password = request.form['password']
        hours = request.form['hours']
        minutes = request.form['minutes']
        am_pm = request.form['am-pm']

        # Call the Selenium function with the captured data
        run_selenium_script(email, password, hours, minutes, am_pm)
        
        return redirect(url_for('index'))  # Redirect to the index page after form submission
    
    return render_template('index.html')

def run_selenium_script(email, password, hours, minutes, am_pm):
    while True:
        # Get the current time
        current_time = datetime.datetime.now()

        # Convert time to 24-hour format
        target_hour = int(hours) if am_pm == 'AM' else int(hours) + 12
        target_minute = int(minutes)
        
        # Check if the current time is past the target time
        if current_time.hour > target_hour or (current_time.hour == target_hour and current_time.minute >= target_minute):
            print("It's past operating time defined by user.")
            break
        
        # # Perform your task here (replace this with your actual task)
        # f.write(f"Current time: {current_time.strftime('%H:%M:%S')}. Running task...\n")


        driver = webdriver.Chrome()
        driver.get("https://ais.usvisa-info.com/en-ca/niv/users/sign_in")
        time.sleep(1)
        # assert "Sign in" in driver.title

        elem_user = driver.find_element(By.ID, "user_email")
        elem_user.clear()
        elem_user.send_keys(email)

        elem_pass = driver.find_element(By.ID, "user_password")
        elem_pass.clear()
        elem_pass.send_keys(password)

        elem_policy = driver.find_element(By.ID, "policy_confirmed")
        elem_policy.send_keys(Keys.SPACE)


        elem_policy.send_keys(Keys.RETURN)

        time.sleep(4)

        elem_reschedule = driver.find_element(By.CLASS_NAME, "button")
        elem_reschedule.click()

        time.sleep(2)

        elem_reschedule_link = driver.find_element(By.CLASS_NAME, "fa-calendar-minus")
        elem_reschedule_link.click()

        time.sleep(2)

        driver.get("https://ais.usvisa-info.com/en-ca/niv/schedule/56778191/appointment")

        time.sleep(5)


        all_available_dates = -1

        month_dict = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }



        elem_No_date = driver.find_element(By.ID, "consulate_date_time_not_available")

        if elem_No_date.is_displayed():
            print(f"No date available in Calgary")
        else:
            print(f"Date available in Calgary")

        elem_date = driver.find_element(By.ID, "consulate_date_time")

        if elem_date.is_displayed():
            print(f"Date available in Calgary")
        else:
            print(f"No date available in Calgary")

        if elem_date.is_displayed():
            # f.write("Searching in Calgary.....\n")
            print(f"Searching in Calgary.....")
            elem_date_field = driver.find_element(By.ID, "appointments_consulate_appointment_date")
            elem_date_field.click()
            time.sleep(1)


            while all_available_dates == -1:
                year_on_calendar = driver.find_element(By.CSS_SELECTOR, 'span.ui-datepicker-year')
                year_value_int = year_on_calendar.text.strip()

                # print("year_value_int", year_value_int)

                time.sleep(1)

                if int(year_value_int) >= 2027:
                    break

                # if int((driver.find_element(By.CSS_SELECTOR, 'span.ui-datepicker-year')).text) < 2027 and 
                if int(year_value_int) < 2026:
                    elem_present_month = driver.find_elements(By.CLASS_NAME, "undefined")

                    # print(elem_present_month)
                    # print(len(elem_present_month))

                    for each_date in range(len(elem_present_month)):
                        # print("In general ", elem_present_month[each_date].find_element(By.CSS_SELECTOR, 'a.ui-state-default'))
                        # time.sleep(1)

                        if elem_present_month[each_date].get_attribute("data-handler") == "selectDay":
                            # f.write("< 2026\n")
                            print("< 2026\n")
                            print(elem_present_month[each_date])
                            # f.write(f"{elem_present_month[each_date].find_element(By.CSS_SELECTOR, 'a.ui-state-default').text}\n\n")
                            print(elem_present_month[each_date].find_element(By.CSS_SELECTOR, 'a.ui-state-default'))
                            all_available_dates = elem_present_month[each_date]
                            break
                
                elif int(year_value_int) == 2026:
                    if month_dict[driver.find_element(By.CSS_SELECTOR, 'span.ui-datepicker-month').text] < month_dict["December"]:
                        elem_present_month = driver.find_elements(By.CLASS_NAME, "undefined")
                        # time.sleep(1)

                        for each_date in range(len(elem_present_month)):
                            if elem_present_month[each_date].get_attribute("data-handler") == "selectDay":
                                # f.write("== 2026\n")
                                print("== 2026\n")
                                print(elem_present_month[each_date])
                                # f.write(f"{elem_present_month[each_date].find_element(By.CSS_SELECTOR, 'a.ui-state-default').text}\n\n")
                                print(elem_present_month[each_date].find_element(By.CSS_SELECTOR, 'a.ui-state-default').text)
                                all_available_dates = elem_present_month[each_date]
                                break

                driver.find_element(By.CLASS_NAME, "ui-datepicker-next").click()
                time.sleep(0.2)

            # print("all", all_pavailable_dates)
            # print(all_available_dates.find_element(By.CSS_SELECTOR, 'a.ui-state-default'))

            time.sleep(1)

        else:
            print(f"Found none in Calgary")



        time.sleep(.2)
        elem_reschedule_city = driver.find_element(By.ID, "appointments_consulate_appointment_facility_id")
        driver.find_element(By.ID, "appointments_consulate_appointment_facility_id").click()
        
        time.sleep(.1)
        elem_reschedule_city.send_keys("V")
        elem_reschedule_city.send_keys(Keys.RETURN)


        time.sleep(5)

        if elem_No_date.is_displayed():
            print(f"No date available in Vancouver")
        else:
            print(f"Date available in Vancouver")

        elem_date = driver.find_element(By.ID, "consulate_date_time")


        all_available_dates = -1


        if elem_date.is_displayed():
            # f.write("Searching in Vancouver....\n")
            print(f"Searching in Vancouver....")
            elem_date_field = driver.find_element(By.ID, "appointments_consulate_appointment_date")
            elem_date_field.click()
            time.sleep(1)


            while all_available_dates == -1:
                year_on_calendar = driver.find_element(By.CSS_SELECTOR, 'span.ui-datepicker-year')
                year_value_int = year_on_calendar.text.strip()

                print("year_value_int", year_value_int)

                time.sleep(1)

                if int(year_value_int) >= 2027:
                    break

                # if int((driver.find_element(By.CSS_SELECTOR, 'span.ui-datepicker-year')).text) < 2027 and 
                if int(year_value_int) < 2026:
                    elem_present_month = driver.find_elements(By.CLASS_NAME, "undefined")

                    # print(elem_present_month)
                    # print(len(elem_present_month))

                    for each_date in range(len(elem_present_month)):
                        # print("In general ", elem_present_month[each_date].find_element(By.CSS_SELECTOR, 'a.ui-state-default'))
                        # time.sleep(1)

                        if elem_present_month[each_date].get_attribute("data-handler") == "selectDay":
                            # f.write("< 2026\n")
                            print("< 2026\n")
                            print(elem_present_month[each_date])
                            # f.write(f"{elem_present_month[each_date].find_element(By.CSS_SELECTOR, 'a.ui-state-default').text}\n\n")
                            print(elem_present_month[each_date].find_element(By.CSS_SELECTOR, 'a.ui-state-default'))
                            all_available_dates = elem_present_month[each_date]
                            break
                
                elif int(year_value_int) == 2026:
                    if month_dict[driver.find_element(By.CSS_SELECTOR, 'span.ui-datepicker-month').text] < month_dict["December"]:
                        elem_present_month = driver.find_elements(By.CLASS_NAME, "undefined")
                        # time.sleep(1)

                        for each_date in range(len(elem_present_month)):
                            if elem_present_month[each_date].get_attribute("data-handler") == "selectDay":
                                # f.write("== 2026\n")
                                print("== 2026\n")
                                print(elem_present_month[each_date])
                                # f.write(f"{elem_present_month[each_date].find_element(By.CSS_SELECTOR, 'a.ui-state-default').text}\n\n")
                                print(elem_present_month[each_date].find_element(By.CSS_SELECTOR, 'a.ui-state-default').text)
                                all_available_dates = elem_present_month[each_date]
                                break

                driver.find_element(By.CLASS_NAME, "ui-datepicker-next").click()
                time.sleep(0.2)

            print("all", all_available_dates)

            time.sleep(.5)

        else:
            print(f"Found none in Vancouver....")


        time.sleep(.5)
        driver.close()

        
        # Sleep for a while before checking the time again
        time.sleep(1)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    app.run(debug=True)