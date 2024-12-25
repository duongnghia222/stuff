from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def auto_gen_data():
    # Initialize Chrome driver
    import csv
    import random
    data_rows = []
    with open('Data2.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_rows.append(row)
    for i, row in enumerate(data_rows):
        if i == 0 or int(row[-1]) == 1: 
            print("skip:", i)
            continue
        if row[1] != "Thành phố Hồ Chí Minh":
            print("skip:", i)
            continue
        driver = webdriver.Chrome()
        print("process:", i)
        success = gen_for_each_row(driver, row)
        if success:
            print("success:", i)
            row[-1] = 1
        else:
            row[-1] = 0
        with open('Data2.csv', 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data_rows)
        driver.quit()

    




def gen_for_each_row(driver, row):
    print(row)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSep3u-XDgaNp-3p4jZVIJaBIaV1wP9c-b8ioiGM_qz4MrT3wg/viewform")
    try:
        # Wait for elements with reduced timeout to speed up execution
        wait = WebDriverWait(driver, 10)
        
        # Page 1 - Initial question
        radio_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='radio']")))
        if row[0] == "Có":
            radio_buttons[0].click()
        else:
            radio_buttons[1].click()
        
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button']")))
        next_button.click()

        if row[0] != "Có":
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][jsname='M2UYVd']")))
            submit_button.click()
            return True

        # Page 2 - Location and screening questions
        if row[1] == "Thành phố Hồ Chí Minh":
            location_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='i6']")))
            location_option.click()
        else:
            location_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='i9']")))
            location_option.click()

        # Question about using social media
        if row[2] == "Có":
            social_media_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='i17']")))
            social_media_option.click()
        else:
            social_media_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='i20']")))
            social_media_option.click()

        # Question about using e-commerce
        if row[3] == "Có":
            ecommerce_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='i28']")))
            ecommerce_option.click()
        else:
            ecommerce_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='i31']")))
            ecommerce_option.click()

        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][jsname='OCpkoe']")))
        next_button.click()

        if row[1] != "Thành phố Hồ Chí Minh":
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][jsname='M2UYVd']")))
            submit_button.click()
            return True

        # Page 3 - Demographics
        # Gender
        print(row[4])
        if row[4] == "Nam":
            gender_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='i6']")))
            gender_option.click()
        else:
            gender_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='i9']")))
            gender_option.click()

        # Income
        income_mapping = {
            "0 - 5 triệu": "i17",
            "5 - 10 triệu": "i20",
            "10 - 20 triệu": "i23",
            "Trên 20 triệu": "i26"
        }
        income_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"div[id='{income_mapping[row[5]]}']")))
        income_option.click()

        # Education
        education_mapping = {
            "Cấp 3": "i34",
            "Đại học": "i37",
            "Thạc sĩ": "i40",
            "Tiến sĩ": "i43"
        }
        education_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"div[id='{education_mapping[row[6]]}']")))
        education_option.click()

        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][jsname='OCpkoe']")))
        next_button.click()

        # Page 4 - Survey questions (indices 7-23 in row)
        all_questions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[jsmodel='CP1oW']")))
        for i, question in enumerate(all_questions):
            if row[i + 7]:  # Check if there's a value
                value = int(float(row[i + 7]))  # Convert to int, handling potential decimals
                if value > 5:
                    value = 5
                radio = question.find_element(By.CSS_SELECTOR, f"div[data-value='{value}']")
                radio.click()

        # Submit form
        finish_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][jsname='OCpkoe']")))
        finish_button.click()

        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][jsname='M2UYVd']")))
        # return False
        submit_button.click()
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        # driver.quit()
        return False

if __name__ == "__main__":
    auto_gen_data()
