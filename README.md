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

![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/028d44fe-248f-4db1-a20c-e4dc1c0292eb)

A bar plot that shows the count of accepted submissions over the years, with filters for submission status (Accepted, Runtime Error, Time Limit Exceeded) and year of submission.

 - **Accepted Submissions by Year and Difficulty**:

![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/a9272670-7939-47b2-90ab-33fcb37a0632)

Another bar plot illustrating the count of accepted submissions over the years, categorized by difficulty and year of submission.

 - **Topic-wise Analysis**:

![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/2cc56573-28c1-41aa-a875-324b0c9a2e9b)

Users can select specific tags and see the submission trends in a bar plot.


### Improvement Rate

 - **Improvement Rate per Month**:

![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/2d6398c0-46f5-4639-951e-56999eea2f03)

A line plot that represents the trend of submission counts over time, showing consistency and progress.

 - **Improvement Rate per Week**:

![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/d2d977d9-6409-4a0f-9648-72c06d5ffa07)

Similar to the monthly plot but with more detailed data at the weekly level.

 - **Month-Wise Status**: 

![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/e8d4d83c-dd73-4d35-b31c-d09fc47d87aa)

See the number and submissions in a month with status.


### Topic-Wise Analysis

 - **Topic-wise Analysis(HeatMap)**: 

![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/047abc6b-8ff8-472d-9259-c13b506cc8ff)

Heatmap shows submission on a particular day of each topic. 

 - **Topic-wise Analysis(ScatterPlot)**:

![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/c236815f-a4c0-4814-aacd-2e44419d0d77)

The scatterplot shows submissions on a particular day for each topic, the larger the circle, the more submissions of that topic. 


### Question Recommendations

**Weakest Topics**:

![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/8a696abc-e3dd-4af0-a433-0c09cbde188b)

Recommendations for the weakest topics in Dynamic Programming, based on accepted questions from the dataset.

 - **Weak Topics**:

![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/60eff03a-1140-4e03-8d9d-6c54dd3db9d4)

Recommendations for weak topics based on user-defined threshold values.

 - **Question category counts Done/ Not Done**:

![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/981dcb76-04da-4d3a-9c36-463a5712c0a4)

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
