# LeetCode Analyser

## Overview

LeetCode Analyser is a Python project that empowers users to monitor and visualize their progress on the LeetCode platform. It scrapes user submission data, creates insightful visualizations, and offers recommendations to enhance performance. This README will guide you through the project's features, installation, and usage.

## Prerequisites

Before using the LeetCode Progress Visualizer, make sure you have the following prerequisites in place:

1. **Web Driver Installation**: You will need a web driver, preferably the Chrome WebDriver. Ensure that it matches the version of your Google Chrome browser.

    - Download the Chrome WebDriver from [here](https://sites.google.com/chromium.org/driver/).

    - Save the downloaded driver (usually a `.exe` file) to your computer. It is recommended to save it as `C:\ChromeDriver\chromedriver.exe`.

2. **Default Browser Configuration**: Set the browser for which you installed the WebDriver as your default browser. This is crucial because the LeetCode Progress Visualizer interacts with your default browser.

3. **Login Information**: You will need your LeetCode username and password for the script to log in on the LeetCode site only if not logged in.
    - Open the `analysis/constants.py` file.

    - Edit the `USERNAME` and `PASSWORD` variables with your LeetCode username and password. If you choose manual login, you can leave these fields unchanged.

5. **Manual Login Option**: Alternatively, you can choose to manually log in to your LeetCode account in the browser where the WebDriver is configured. This will skip the need for entering login information in the script.


## Features

### Data Scraping

The project uses the Selenium library in Python to scrape submission data from the LeetCode website. It navigates through login, submission pages, and question pages to extract essential information, including tags, name, ID, link, difficulty, and submission details.

### Data Management

The scraped data is stored in a data frame. On subsequent runs, the program continues from the previous DataFrame and only scrapes new submissions, reducing redundancy.

### Visualizations

### Submission Trend


 - **Accepted Submissions by Year and Status**:

![image](https://github.com/AnupamMittal-21/LeetCode-Analyser/assets/96871662/932f4ff4-74b5-4e66-948a-66baad00736e)

A bar plot that shows the count of accepted submissions over the years, with filters for submission status (Accepted, Runtime Error, Time Limit Exceeded) and year of submission.


 - **Accepted Submissions by Year and Difficulty**:

![image](https://github.com/AnupamMittal-21/LeetCode-Analyser/assets/96871662/099c37b5-d731-42a9-9bc5-a132f5511257)

Another bar plot illustrating the count of accepted submissions over the years, categorized by difficulty and year of submission.


 - **Topic-wise Analysis**:

![image](https://github.com/AnupamMittal-21/LeetCode-Analyser/assets/96871662/8006404f-2a85-4346-b5d3-89cc4dc3e777)

Users can select specific tags and see the submission trends in a bar plot.



### Improvement Rate


 - **Improvement Rate per Month**:

![image](https://github.com/AnupamMittal-21/LeetCode-Analyser/assets/96871662/dcca304d-00aa-4b0e-9932-d0a28d1b1357)

A line plot that represents the trend of submission counts over time, showing consistency and progress.


 - **Improvement Rate per Week**:

![image](https://github.com/AnupamMittal-21/LeetCode-Analyser/assets/96871662/29bca585-b742-4ea6-92c2-b41af5858aef)

Similar to the monthly plot but with more detailed data at the weekly level.


 - **Month-Wise Status**: 

![image](https://github.com/AnupamMittal-21/LeetCode-Analyser/assets/96871662/4c197c6e-0009-4cbc-9f23-250baa87a1e2)

See the number and submissions in a month with status.



### Topic-Wise Analysis

 - **Topic-wise Analysis(HeatMap)**: 

![image](https://github.com/AnupamMittal-21/LeetCode-Analyser/assets/96871662/3bd283db-8e30-49ad-83f0-9d7c00f1c970)

Heatmap shows submission on a particular day of each topic. 


 - **Topic-wise Analysis(ScatterPlot)**:

![image](https://github.com/AnupamMittal-21/LeetCode-Analyser/assets/96871662/cd826a2d-d660-46cf-aa35-650857dee90e)

The scatterplot shows submissions on a particular day for each topic, the larger the circle, the more submissions of that topic. 



### Question Recommendations


**Weakest Topics**:

![image](https://github.com/AnupamMittal-21/LeetCode-Analyser/assets/96871662/fda8771d-cc82-4632-bb33-3165b32f7955)

Recommendations for the weakest topics in Dynamic Programming, based on accepted questions from the dataset.


 - **Weak Topics**:

![image](https://github.com/AnupamMittal-21/LeetCode-Analyser/assets/96871662/892e0517-4470-437a-ab29-3049fea16b1f)

Recommendations for weak topics based on user-defined threshold values.


 - **Question category counts Done/ Not Done**:

![image](https://github.com/AnupamMittal-21/LeetCode-Analyser/assets/96871662/db794443-02ff-46a9-9133-c81f93ba83ea)



### Demo

You can watch a video demonstration of the project [here](https://youtu.be/ztgmpjuMULE).

Interact with the live demo of the project [here](https://leet-analyzer.streamlit.app/).

## Installation

To get started with LeetCode Analyser, follow these steps:

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/AnupamMittal-21/LeetCode-Analyser.git

2. Navigate to the project directory:

   ```bash
   cd LeetCode-Analyser
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the scraper script to collect LeetCode submission data:

   ```bash
   python run.py
   ```

2. Once you have collected the data, start the Streamlit app (If you want to run it without scraping):

   ```bash
   streamlit run analysis/visualisation.py
   ```

3. Visit the app in your web browser (by default, it runs on `http://localhost:8501`).

4. Use the various visualization options and recommendations to track and improve your LeetCode performance.

## Contributors

- Anupam Mittal (https://github.com/AnupamMittal-21)


9. **Interact and Visualize**:

    - Use the various visualization options and recommendations to monitor and enhance your LeetCode performance.

By following these steps, you'll have LeetCode Progress Visualizer up and running, allowing you to track your LeetCode journey with valuable insights.

Thank You.
