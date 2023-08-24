from selenium.webdriver.common.by import By
from analysis import constants as const
import os
import time
import pandas as pd
from selenium import webdriver
import pickle


class LeetAnalysis(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\ChromeDrive\chromedriver.exe", teardown=False):

        # All the lists are used to store data and at last used to convert to dataframe
        self.driver_path = driver_path
        self.teardown = teardown
        self.ques_link_list = []
        self.status_list = []
        self.language_list = []
        self.runtime_list = []
        self.memory_list = []
        self.time_list = []
        self.ques_difficulty = []
        self.ques_likes = []
        self.ques_dislike = []
        self.ques_acceptance_rate = []
        self.ques_id = []
        self.ques_name = []
        self.ques_links = []
        self.ques_tags = []
        self.ques_tags_links = []

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

    def land_first_page(self):
        # This functions just open the browser with the given link
        self.get(const.BASE_URL)

    def login(self):
        # I am using try except here because I have 2 options
        # 1 = I need to log in so need to scrap login button and then pass arguments
        # 2 = I am already logged in that browser.
        try:
            time.sleep(4)  # Giving time to load the page, so that the below tags are loaded to be extracted
            login_input = self.find_element(By.CSS_SELECTOR, 'input[name="login"]')  # Accessing username textfield
            pass_input = self.find_element(By.CSS_SELECTOR, 'input[name="password"]')  # Accessing password textfield

            login_input.send_keys(const.username)  # Passing username
            time.sleep(2)
            pass_input.send_keys(const.password)  # Passing password

            login_btn = self.find_element(By.CSS_SELECTOR, 'button#signin_btn')  # Login button
            self.implicitly_wait(10)  # To tackle captcha problem otherwise captcha comes
            time.sleep(2)  # To tackle captcha problem otherwise captcha comes
            login_btn.click()  # Clicking on login button
            time.sleep(3)

        except:
            print("Already Logged In")

        # Now I am at my home page where I now need to go to my profile pic button and then click on submission
        account_btn = self.find_elements(By.CSS_SELECTOR, 'a.ant-dropdown-link')
        # Account button so that we can go to submissions page
        account_btn[-1].click()
        # Since there were many elements with the same class so chosen last one as it is always on the last
        self.implicitly_wait(4)

        submission_btn = self.find_element(By.CSS_SELECTOR, 'a[href="/submissions/"]')
        # Submission button after account tab
        submission_btn.click()
        time.sleep(3)  # Time given to load next page before scraping

        # Now after this function we are at submission page now we have to iterate through all the pages of submission
        # and then go to uniques question pages and then extract more information from there as there only is exact data

    def scrap_submission_page(self):

        # This condition is set to true so that i can traverse in submission page list then in all the pages.
        condition = True
        # To store uniques ques
        ques_list = []
        # To store link pf uniques ques, used to go to each question after scrapping from submission page
        ques_link_list = []

        while condition:
            self.implicitly_wait(10)
            question_table = self.find_element(By.CSS_SELECTOR, 'div#submission-list-app>div>table>thead+tbody')
            # Getting table where all submission are stored of a particular page.
            tr_list = question_table.find_elements(By.CSS_SELECTOR, 'tr')
            for tr in tr_list:  # tr is each row and each row has some td-s
                ques_name = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text  # second child is name of question

                if ques_name not in ques_list:  # To get uniques
                    ques_list.append(ques_name)
                    ques_link = tr.find_element(By.CSS_SELECTOR,'td:nth-child(3)>a')  # Finding link of those uniques only
                    ques_link_list.append(ques_link.get_attribute('href'))

            print(f"length of table on submission page is {len(tr_list)}")
            print(ques_link_list) # this prints the count of all the submission on a page

            if self.find_element(By.XPATH,'//*[@id="submission-list-app"]/div/nav/ul/li[2]').get_attribute('class')=='next disabled':
                condition = False
            # To check if we reached at then end, now no more submissions are left, so stop.

            else:
                next_btn = self.find_element(By.XPATH,'//*[@id="submission-list-app"]/div/nav/ul/li[2]/a/span')
                next_btn.click()


        self.ques_link_list = ques_link_list
        print(f"The total submissions are : {len(self.ques_link_list)}")


        # WORKING TILL HERE

        # Going to each page of questions using the list we created
        for ques_link in self.ques_link_list:
            self.get(ques_link)
            # time.sleep(3)
            self.implicitly_wait(10)
            ques_problem_link = self.find_element(By.CSS_SELECTOR, 'a.inline-wrap')
            ques_problem_link.click()
            # Clicking on ques name as on this page not much data is to scrap

            # time.sleep(5)
            self.implicitly_wait(5)

            # Now we are on question description page, now we are going to extract data from this page and submission page

            # Extracting from description page
            question_id = self.find_element(By.XPATH,'//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/a').text.split('. ')[0]
            question_name = self.find_element(By.XPATH,'//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/a').text.split('. ')[1]
            question_diff = self.find_element(By.XPATH,'//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]').text
            question_likes = self.find_element(By.XPATH,'//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div[2]').text
            question_dislikes = self.find_element(By.XPATH,'//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[2]/div[2]').text
            question_acceptance_rate = self.find_element(By.XPATH,'//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[4]/div/div[5]/div[2]').text
            # ques_tags_list = None
            self.implicitly_wait(5)

            # Extracting related tags and tags link

            # this is div where toggle button and data is present
            question_tag_div = self.find_elements(By.CSS_SELECTOR, 'div.px-5.py-3')[-1]
            # Toggle button is clicked
            question_tag_div.find_element(By.CSS_SELECTOR, 'svg').click()
            # Each anchor tag is listed
            tags_div = self.find_element(By.CSS_SELECTOR, 'div.mt-2.flex.flex-wrap.gap-y-3')
            tag_div_list = tags_div.find_elements(By.CSS_SELECTOR, 'a')

            tag_list_per_question = []
            tags_link_list = []

            # Looping in anchor tags list
            for ques_tag in tag_div_list:
                tag_list_per_question.append(ques_tag.text)
                tags_link_list.append(ques_tag.get_attribute('href'))

            # Now, moving on to submission section of the question.

            submission_nav_bar = self.find_element(By.CSS_SELECTOR, 'div.flex.h-full.flex-row.gap-8') # Top bar
            submission_btn_on_page = submission_nav_bar.find_elements(By.CSS_SELECTOR, 'a')[-1]  # Submission btn
            submission_btn_on_page.click()
            self.implicitly_wait(5)

            # This is table of all the submission on that particular question
            submission_container = self.find_element(By.CSS_SELECTOR,'#qd-content > div.h-full.flex-col.ssg__qd-splitter-primary-w > div > div > div > div.flex.h-full.w-full.overflow-y-auto.rounded-b > div > div.h-full.px-4')
            ques_div_list = submission_container.find_elements(By.CSS_SELECTOR, 'span')
            for i, ques_div in enumerate(ques_div_list):
                if i % 3 == 0:
                    self.status_list.append(ques_div.text)
                elif i%3==1:
                    self.time_list.append(ques_div.text)
                else:
                    self.ques_id.append(question_id)
                    self.ques_name.append(question_name)
                    self.ques_difficulty.append(question_diff)
                    self.ques_likes.append(question_likes)
                    self.ques_dislike.append(question_dislikes)
                    self.ques_acceptance_rate.append(question_acceptance_rate)
                    self.ques_links.append(ques_link)
                    self.ques_tags.append(tag_list_per_question)
                    self.ques_tags_links.append(tags_link_list)


    def create_dataframe(self):
        time.sleep(3)
        #  creating dictionary for easy pickling
        dict = {'Status': self.status_list, 'DateOfSubmission': self.time_list,'Name': self.ques_name, 'ID': self.ques_id,'Link':self.ques_links,'Difficulty': self.ques_difficulty, 'Likes': self.ques_likes,'Dislikes':self.ques_dislike,'Acceptance':self.ques_acceptance_rate,'Tags':self.ques_tags,'Tag_Link':self.ques_tags_links}
        df = pd.DataFrame(dict)
        pickle.dump(df.to_dict(),open('leet_dict.pkl','wb'))
        print(df)
        print(df['Tags'])
        print(df['Link'])
        print(df['ID'])

    # https://youtu.be/3wZ7GRbr91g?si=m80mfcIvQ2xNz-SA == nice video to learn
    def trial(self):
        self.get('https://leetcode.com/problems/search-a-2d-matrix/')
        self.implicitly_wait(4)
        question_dislikes = self.find_elements(By.CSS_SELECTOR,'div.px-5.py-3')[-1]
        question_dislikes.find_element(By.CSS_SELECTOR, 'svg').click()
        tags_div = self.find_element(By.CSS_SELECTOR, 'div.mt-2.flex.flex-wrap.gap-y-3')
        tag_div_list= tags_div.find_elements(By.CSS_SELECTOR,'a')
        print(len(tag_div_list))
        for tags in tag_div_list:
            print(tags.text)
            print(tags.get_attribute('href'))
