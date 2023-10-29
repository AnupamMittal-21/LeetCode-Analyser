from selenium.webdriver.common.by import By
from analysis import constants as const
import os
import time
import pandas as pd
from selenium import webdriver
import pickle
import re
import subprocess

class LeetAnalysis(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\ChromeDrive\chromedriver.exe", teardown=False):

        # All the lists are used to store data and at last used to convert to dataframe
        self.dp_df_ = None
        self.driver_path = driver_path
        self.teardown = teardown
        self.ques_id = []
        self.ques_name = []
        self.ques_difficulty = []
        self.date_list = []
        self.status_list = []
        self.ques_description = []
        self.ques_tags = []
        self.ques_link = []
        self.sub_link = []
        self.ques_link_list = []
        self.df = None


        #  Setting path of chrome driver from local directory
        os.environ['PATH'] += r"C:\ChromeDriver\chromedriver.exe"
        options = webdriver.ChromeOptions()
        # Setting our default browser as dummy browser so that captcha problem is solved
        options.add_argument(r'--user-data-dir=C:\Users\anupa\AppData\Local\Google\Chrome\User Data\Default')

        super(LeetAnalysis, self).__init__(options=options)

        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def load_df(self):
        if os.path.exists('leet_dict.pkl'):
            # If the CSV file exists, load it into a DataFrame
            print("CSV File exists...\nloading file...")
            leet_dict = pickle.load(open('leet_dict.pkl', 'rb'))
            self.df = pd.DataFrame(leet_dict)
        else:
            dict = {'Status': self.status_list, 'DateOfSubmission': self.date_list, 'Name': self.ques_name,
                    'ID': self.ques_id, 'Link': self.ques_link, 'Difficulty': self.ques_difficulty,
                    'Tags': self.ques_tags, 'Description': self.ques_description, 'Sub_Link': self.sub_link}

            self.df = pd.DataFrame(dict)
            print("CSV File not found...\nCreating empty dataframe")
            print(self.df)

    def land_ques_page(self):
        # This functions just open the browser with the given link
        self.get(const.QUES_URL)
    # Working...
    # Id, Name, Description, Difficulty, Tags, link of question, Submission status and date.
    # I also tried to get the submission link and the time but it is not working well.

    # Working
    def land_first_page(self):
        # This functions just open the browser with the given link
        self.get(const.BASE_URL)

    # Without login part is working...
    def login(self):
        # I am using try except here because I have 2 options
        # 1 = I need to log in so need to scrap login button and then pass arguments
        # 2 = I am already logged in that browser.
        try:
            self.implicitly_wait(10)  # Giving time to load the page, so that the below tags are loaded to be extracted
            login_input = self.find_element(By.CSS_SELECTOR, 'input[name="login"]')  # Accessing username textfield
            pass_input = self.find_element(By.CSS_SELECTOR, 'input[name="password"]')  # Accessing password textfield

            login_input.send_keys(const.username)  # Passing username
            self.implicitly_wait(10)
            pass_input.send_keys(const.password)  # Passing password

            login_btn = self.find_element(By.CSS_SELECTOR, 'button#signin_btn')  # Login button
            self.implicitly_wait(10)  # To tackle captcha problem otherwise captcha comes
            time.sleep(2)  # To tackle captcha problem otherwise captcha comes
            login_btn.click()  # Clicking on login button
            self.implicitly_wait(10)

        except:
            print("Already Logged In")

        # Now I am at my home page where I now need to go to my profile pic button and then click on submission
        # account_btn = self.find_elements(By.CSS_SELECTOR, 'a.ant-dropdown-link')
        # # Account button so that we can go to submissions page
        # account_btn[-1].click()  ## --> For previous version

        account_btn = self.find_element(By.CSS_SELECTOR, 'button#headlessui-menu-button-5')
        account_btn.click()
        # Since there were many elements with the same class so chosen last one as it is always on the last
        self.implicitly_wait(10)

        submission_btn = self.find_element(By.CSS_SELECTOR, 'a[href="/submissions/"]')
        # Submission button after account tab
        submission_btn.click()
        time.sleep(3)  # Time given to load next page before scraping
        self.implicitly_wait(10)
        # Now after this function we are at submission page now we have to iterate through all the pages of submission
        # and then go to uniques question pages and then extract more information from there as there only is exact data


    # Working
    def scrap_submission_page(self):

        # This condition is set to true so that I can traverse in submission page list then in all the pages.
        condition = True

        # To store uniques ques
        ques_list = []

        # To store link pf uniques ques, used to go to each question after scrapping from submission page
        ques_link_list = []
        cnt = 0

        while condition:
            cnt += 1
            if cnt % 10 == 0:
                time.sleep(10)
            print(f'Page No : {cnt}')
            self.implicitly_wait(15)

            url_ = f'https://leetcode.com/submissions/#/{cnt}'
            self.get(url_)
            try:
                # Page number 31 - Error (DEBUG)
                question_table = self.find_element(By.CSS_SELECTOR,
                                                   'table.table.table-striped.table-bordered.table-hover>tbody')
            except:
                self.implicitly_wait(10)
                # url_ = f'https://leetcode.com/submissions/#/{cnt}'
                self.get(self.current_url)
                self.implicitly_wait(5)
                # question_table = self.find_element(By.CSS_SELECTOR, 'div#submission-list-app>div>table>thead+tbody')
                question_table = self.find_element(By.CSS_SELECTOR,
                                                   'table.table.table-striped.table-bordered.table-hover>tbody')

            # Getting table where all submission are stored of a particular page.
            tr_list = question_table.find_elements(By.CSS_SELECTOR, 'tr')

            # Print for Debugging
            # print(tr_list[0].text)
            # ques_name = tr_list[0].find_element(By.CSS_SELECTOR, 'td:nth-child(2)')
            # print(ques_name.text

            for tr in tr_list:  # tr is each row and each row has some td-s
                ques_name = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text  # second child is name of question

                if ques_name not in ques_list:  # To get uniques
                    ques_list.append(ques_name)
                    ques_link = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(3)>a')

                    if self.df.shape[0]>0:
                        print("Shape is >0.")

                        result = self.df['Sub_Link'].str.contains(ques_link.get_attribute('href'))  # The 'case' parameter makes the search case-insensitive

                        # 'result' is a Boolean Series where each element is True if 'string_to_check' is found in the corresponding row of 'column_name', False otherwise.
                        # You can print the rows where the string is found:
                        if (len(self.df[result]) > 0):
                            print(len(self.df[result]))
                            print("Found")
                            print("Braking Loop...")
                            condition = False
                            break
                    # Finding link of those uniques only
                    ques_link_list.append(ques_link.get_attribute('href'))

            print(f"length of table on submission page is {len(tr_list)}")
            print(ques_link_list)  # this prints the count of all the submission on a page

            if self.find_element(By.XPATH, '//*[@id="submission-list-app"]/div/nav/ul/li[2]').get_attribute(
                    'class') == 'next disabled':
                condition = False
            # To check if we reached at then end, now no more submissions are left, so stop.
            else:
                next_btn = self.find_element(By.XPATH, '//*[@id="submission-list-app"]/div/nav/ul/li[2]/a/span')
                next_btn.click()

        self.ques_link_list = ques_link_list
        print(f"The total submissions are : {len(self.ques_link_list)}")

        print("Traversed all the submission pages")
        return

    def scrap_each_page(self):
        # Going to each page of questions using the list we created
        cnt = 0

        for ques_link in self.ques_link_list:
            try:
                cnt += 1
                if cnt % 10 == 0:
                    time.sleep(5)
                self.get(ques_link)

                print(ques_link)

                self.implicitly_wait(10)

                ques_problem_link = self.find_element(By.CSS_SELECTOR, 'a.inline-wrap')
                ques_problem_link.click()
                # Clicking on ques name as on this page not much data is to scrap

                self.implicitly_wait(10)

                # This is used because there are contest submission pages too and they have different page when we hit submission
                curr_url = self.current_url
                if 'contest' in curr_url:
                    curr_url = re.sub(r'contest/(bi)?weekly-contest-(\d)*/', '', curr_url)
                    self.get(curr_url)

                self.implicitly_wait(10)

                # Now we are on question description page, now we are going to extract data from this page and submission page
                try:
                    # Extracting from description page
                    try:
                        name_column = self.find_element(By.CSS_SELECTOR,
                                                        "div.flex.items-start.justify-between.gap-4>div>div")
                    except:
                        self.get(self.current_url)
                        self.implicitly_wait(10)
                        name_column = self.find_element(By.CSS_SELECTOR,
                                                        "div.flex.items-start.justify-between.gap-4>div>div")

                    id_ = name_column.text.split('. ')[0]
                    name = name_column.text.split('. ')[1]

                    description = self.find_element(By.CSS_SELECTOR, 'div[data-track-load="description_content"]').text

                    # Extracting Tags and difficulty is a lot of work to do...
                    parent_div = self.find_element(By.CSS_SELECTOR,
                                                   'div.flex.w-full.flex-1.flex-col.gap-4.overflow-y-auto.px-4.py-5')

                    tag_col = parent_div.find_elements(By.CSS_SELECTOR, 'div.flex.gap-1')[1]
                    tag_col_list = tag_col.find_elements(By.CSS_SELECTOR, '*')

                    diff = tag_col_list[0].text

                    topic = tag_col_list[1]
                    topic.click()
                    time.sleep(2)

                    topic_list = self.find_element(By.CSS_SELECTOR, 'div.mb-4.flex.flex-wrap.gap-3').text
                    topics = topic_list.split('\n')

                    # Now, moving on to submission section of the question.

                    # Updating link itself rather than searching the submission button and clicking on it.
                    url_ = self.current_url
                    link = url_
                    url_ = url_ + 'submissions/'
                    self.get(url_)
                    time.sleep(3)

                    submission_cont = self.find_element(By.CSS_SELECTOR, 'div.h-full.overflow-auto')
                    submissions_list = submission_cont.find_elements(By.CSS_SELECTOR,
                                                                     'div.group.flex.cursor-pointer.items-center.justify-between')

                    for submission in submissions_list:
                        status_ = submission.find_element(By.CSS_SELECTOR,
                                                          "div.flex.flex-shrink-0.flex-col.justify-between").text
                        status_list = status_.split('\n')
                        status = status_list[0]
                        date = status_list[1]
                        self.ques_id.append(id_)
                        self.ques_name.append(name)
                        self.ques_description.append(description)
                        self.ques_difficulty.append(diff)
                        self.status_list.append(status)
                        self.date_list.append(date)
                        self.ques_tags.append(topics)
                        self.ques_link.append(link)
                        self.sub_link.append(ques_link)
                except:
                    print("Some exception")

            except:
                print("SOME EXCEPTION")


   # Working...
    def create_dataframe(self):
        time.sleep(3)
        #  creating dictionary for easy pickling
        dict = {'Status': self.status_list, 'DateOfSubmission': self.date_list, 'Name': self.ques_name,
                'ID': self.ques_id, 'Link': self.ques_link, 'Difficulty': self.ques_difficulty,
                'Tags': self.ques_tags, 'Description': self.ques_description,'Sub_Link': self.sub_link}

        temp_df = pd.DataFrame(dict)
        self.df = pd.concat([temp_df,self.df],axis=0)
        pickle.dump(self.df.to_dict(), open('leet_dict.pkl', 'wb'))
        print(self.df)
        print('#######################################################################################################')
        print(self.df['Tags'])
        print('#######################################################################################################')
        print(self.df['Link'])
        print('#######################################################################################################')
        print(self.df['ID'])
        print('#######################################################################################################')
        print(self.df['DateOfSubmission'])
        print('#######################################################################################################')
        print('Completed Successfully')


    def show_visuals(self):
        # This is to run the streamlit file using function call automatically, rather than manually by writting streamlit run file.py
        streamlit_app_file = "analysis/visualisation.py"
        subprocess.call(["streamlit", "run", streamlit_app_file])
    # With this the scope of this file ends...
    # It was great, building this project...

    # ...Jai Shree Ram...