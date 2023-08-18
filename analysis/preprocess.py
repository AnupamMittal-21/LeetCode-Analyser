from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from analysis import constants as const
import os
import time
import pandas as pd
from selenium import webdriver
class LeetAnalysis(webdriver.Chrome):
    def __init__(self,driver_path = r"C:\ChromeDriver\chrome-win64",teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        self.ques_link_list = []
        self.status_list = []
        self.language_list = []
        self.runtime_list = []
        self.memory_list = []
        self.time_list = []

        os.environ['PATH'] += r"C:\ChromeDriver\chrome-win64"
        options = webdriver.ChromeOptions()

        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        options.add_argument("user-agent="+user_agent)


        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')


        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(LeetAnalysis, self).__init__(options=options)

        self.implicitly_wait(15)
        self.maximize_window()  # This maximises the driver window


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        # login_url = "https://leetcode.com/accounts/login/" which is imported from constant file
        self.get(const.BASE_URL)

    def login(self):
        time.sleep(4)  # Giving time to load the page, so that the below tags are loaded to be extracted
        login_input = self.find_element(By.CSS_SELECTOR, 'input[name="login"]')  # Accessing username textfield
        pass_input = self.find_element(By.CSS_SELECTOR, 'input[name="password"]')  # Accessing password textfield

        login_input.send_keys(const.username)  # Passing username
        time.sleep(1)
        pass_input.send_keys(const.password)   # Passing password


        login_btn = self.find_element(By.CSS_SELECTOR, 'button#signin_btn')  # Login button
        self.implicitly_wait(10)  # To tackle captcha problem otherwise captcha comes
        time.sleep(3)  # To tackle captcha problem otherwise captcha comes
        login_btn.click()  # Clicking on login button
        time.sleep(2)

        account_btn = self.find_elements(By.CSS_SELECTOR,'a.ant-dropdown-link')
        # Account button so that we can go to submissions page
        account_btn[-1].click()
        # Since there were many elements with the same class so chosen last one as it is always on the last
        self.implicitly_wait(4)

        submission_btn = self.find_element(By.CSS_SELECTOR,'a[href="/submissions/"]')
        # Submission button after account tab
        submission_btn.click()
        time.sleep(2)  # Time given to load next page before scraping

        # Now after this function we are at submission page now we have to iterate through all the pages of submission
        # and then go to uniques question pages and then extract more information from there as there only is exact data

        # Full Captcha = //*[@id="rc-anchor-container"]
    def scrap_submission_page(self):
        ques_list = []  # Motive of this list is to store the unique names of all the question so that i can get
        # unique url of questions then scrap it further
        ques_link_list = []  # This is just to store the list of link of submitted unique questions

        question_table = self.find_element(By.CSS_SELECTOR,'div#submission-list-app>div>table>thead+tbody')
        tr_list = question_table.find_elements(By.CSS_SELECTOR,'tr')
        # this is the table where all the list of question is there, so I have taken the tableData and then selected all
        # the table rows by findElements

        for tr in tr_list:  # tr is each row and each row has some td-s
            ques_name = tr.find_element(By.CSS_SELECTOR,'td:nth-child(2)').text  # second child is name of question

            if ques_name not in ques_list:  # To get uniques
                ques_list.append(ques_name)
                ques_link = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(3)>a')  # Finding link of those uniques only
                ques_link_list.append(ques_link)
                # ques_link_list.append(ques_link.get_attribute("href"))

        # print(len(tr_list))
        print(ques_link_list)
        self.ques_link_list = ques_link_list
        # In order to use this list in other functions I have assigned it as a data member

        # As of now it is only for one page and now i have list of all the unique question

    def scrap_info_from_a_page(self):
        time.sleep(5)
        for ques_link_elem in self.ques_link_list:
            time.sleep(3)
            ques_link_elem.click()  # Here I have clicked on link, and now I am at submission page
            time.sleep(3)
            ques_problem_link = self.find_element(By.CSS_SELECTOR,'a.inline-wrap')
            ques_problem_link.click()
            # Clicking on ques name as on this page not much data is to scrap

            time.sleep(3)
            # time.sleep(1000)


            submission_nav_bar = self.find_element(By.CSS_SELECTOR,'div.flex.h-full.flex-row.gap-8')
            submission_btn_on_page = submission_nav_bar.find_elements(By.CSS_SELECTOR,'a')[-1]
            submission_btn_on_page.click()
            # Clicking on submissions on problem description page
            time.sleep(2)
            # ✨✨...CORRRECT UPTO HERE...✨✨



            submission_container = self.find_element(By.XPATH,'//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div[2]')
            ques_div_list = submission_container.find_elements(By.CSS_SELECTOR,'div')
            print(len(ques_div_list))


            








            #
            #
            #
            # submission_box = self.find_element(By.CSS_SELECTOR,'div.h-full.px-4')
            # submission_list = submission_box.find_elements(By.CSS_SELECTOR,'div')
            # # print(submission_list)
            # # Getting all the submission of that particular page
            # status_elem_list = self.find_elements(By.CSS_SELECTOR,'div.truncate.text-red-s.dark:text-dark-red-s')
            # for i in status_elem_list:
            #     print(i.text)
            # # text-sm text-label-2 dark:text-dark-label-2
            # date_elem_list = self.find_elements(By.CSS_SELECTOR, 'span.text-sm.text-label-2.dark:text-dark-label-2')
            # for i in date_elem_list:
            #     print(i.text)
            # # for i,submission in enumerate(submission_list):
            # #     print(submission.get_attribute('class'))
            # # #
            # #     flex items-center gap-1.5
            # #     here comes the problem
            # #     submission is a div that has 1 - status, language, runtime, memory, time
            #     # status = submission.find_element(By.CSS_SELECTOR,'div:nth-child(1)>div>div>span')
            #     # print(status.get_attribute('class'),"INSIDE LOOP")
            #     # print(status.text,i)
            #
            #
            #
            #












                # language = submission.find_element(By.CSS_SELECTOR, 'div:nth-child(2)')
                # print(language,i)
                # runtime = submission.find_element(By.CSS_SELECTOR, 'div:nth-child(3)').text
                # print(runtime,i)
                # memory = submission.find_element(By.CSS_SELECTOR, 'div:nth-child(4)').text
                # print(memory,i)
                # date_submission = submission.find_element(By.CSS_SELECTOR, 'div:nth-child(5)').text
                # print(date_submission,i)

                # self.status_list.append(status)
                # self.language_list.append(language)
                # self.runtime_list.append(runtime)
                # self.memory_list.append(memory)
                # self.time_list.append(date_submission)

                # div.class="flex h-full w-full flex-row gap-6" - for submission button on problem pafe
                # div.class="h-full px-4" for multiple submiossion of question
                # div have all the divs so use select divs

    def create_dataframe(self):
        dict = {'Status': self.status_list, 'Language': self.language_list, 'Runtime': self.runtime_list,
                'Memory': self.memory_list, 'DateOfSubmission': self.time_list}
        df = pd.DataFrame(dict)
        print(df)








