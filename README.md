# Project Name: LeetCode Analyser

## Overview

LeetCode Progress Visualizer is a Python project that enables users to monitor and visualize their progress on the LeetCode platform. It scrapes user submission data, creates insightful visualizations, and offers recommendations to improve performance. This README will guide you through the project's features, installation, and usage.

### Features

- **Data Scraping**: The project uses the Selenium library in Python to scrape submission data from the LeetCode website. It navigates through login, submission pages, and question pages to extract essential information, including tags, name, ID, link, difficulty, and submission details.

- **Data Management**: The scraped data is stored in a data frame. On subsequent runs, the program continues from the previous DataFrame and only scrapes new submissions, reducing redundancy.

- **Visualizations**: LeetCode Progress Visualizer offers a Streamlit web application with various visualization options:

Submission Trend 

    - **Accepted Submissions by Year and Status**: A bar plot that shows the count of accepted submissions over the years, with filters for submission status (Accepted, Runtime Error, Time Limit Exceeded).
 
    - ![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/028d44fe-248f-4db1-a20c-e4dc1c0292eb)


    - **Accepted Submissions by Year and Difficulty**: Another bar plot illustrating the count of accepted submissions over the years, categorized by difficulty.
 
    - ![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/a9272670-7939-47b2-90ab-33fcb37a0632)


    - **Topic-wise Analysis**: Users can select specific tags and see the submission trends in a bar plot.

    ![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/2cc56573-28c1-41aa-a875-324b0c9a2e9b)

 
    - 
Improvement Rate 

    - **Improvement Rate per Month**: A line plot that represents the trend of submission counts over time, showing consistency and progress.

    ![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/2d6398c0-46f5-4639-951e-56999eea2f03)


    - **Improvement Rate per Week**: Similar to the monthly plot but with more detailed data at the week level.
    
    ![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/d2d977d9-6409-4a0f-9648-72c06d5ffa07)

    - ** Month-Wise Status**: See the number and submissions in a month with status.
    

    ![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/e8d4d83c-dd73-4d35-b31c-d09fc47d87aa)


**Topic-wise Analysis**: This section includes two plots: a heatmap and a scatter plot. 

    ![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/047abc6b-8ff8-472d-9259-c13b506cc8ff)
    ![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/c236815f-a4c0-4814-aacd-2e44419d0d77)


    - The heatmap displays variations in submissions per topic, while the scatter plot shows the relationship between topic submissions and performance.

- **Topic Recommendations**: The project offers recommendations for weak and weakest topics in Dynamic Programming, based on accepted questions from the dataset. It identifies the weakest topics with the lowest percentage and weak topics below user-defined threshold values.
    - Weakest Topics -
    - ![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/8a696abc-e3dd-4af0-a433-0c09cbde188b)

    - Weak Topics
    - ![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/60eff03a-1140-4e03-8d9d-6c54dd3db9d4)

    - Question category counts Done/ Not Done
    -
    - ![image](https://github.com/AnupamMittal-21/LeetAnalyser_1/assets/96871662/981dcb76-04da-4d3a-9c36-463a5712c0a4)

- **Demo Video**: You can watch a demo video of the project [here](https://example.com).

- **Live Demo**: The project is deployed as a Streamlit app, and you can interact with it [here](https://example.com).

## Installation

To get started with LeetCode Progress Visualizer, follow these steps:

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/yourusername/leetcode-progress-visualizer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd leetcode-progress-visualizer
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the scraper script to collect LeetCode submission data:

   ```bash
   python scraper.py
   ```

2. Once you have collected the data, start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Visit the app in your web browser (by default, it runs on `http://localhost:8501`).

4. Use the various visualization options and recommendations to track and improve your LeetCode performance.

## Demo

You can watch a video demonstration of the project [here](https://example.com). Additionally, interact with the live demo of the project [here](https://example.com).

Feel free to explore and enhance your LeetCode journey with data-driven insights using LeetCode Progress Visualizer.

## Contributors

- Your Name (YourGitHubProfile)
- Collaborator 1 (Collaborator1GitHubProfile)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




# LeetCode Progress Visualizer - Installation and Setup Guide

LeetCode Progress Visualizer is a powerful tool to track your LeetCode progress. To use this project, you need to set up a few prerequisites. This guide will walk you through the necessary steps.

## Prerequisites

Before using the LeetCode Progress Visualizer, make sure you have the following prerequisites in place:

1. **Web Driver Installation**: You will need a web driver, preferably the Chrome WebDriver. Ensure that it matches the version of your Google Chrome browser.

    - Download the Chrome WebDriver from [here](https://sites.google.com/chromium.org/driver/).

    - Save the downloaded driver (usually a `.exe` file) to your computer. It is recommended to save it as `C:\ChromeDriver\chromedriver.exe`.

2. **Default Browser Configuration**: Set the browser for which you installed the WebDriver as your default browser. This is crucial because the LeetCode Progress Visualizer interacts with your default browser.

3. **Login Information**: You will need your LeetCode username and password for the script to log in securely. The login information is only used for authentication purposes and is not stored or shared.

4. **Manual Login Option**: Alternatively, you can choose to manually log in to your LeetCode account in the browser where the WebDriver is configured. This will skip the need for entering login information in the script.

## Installation Steps

Follow these steps to set up LeetCode Progress Visualizer:

1. **Clone the Repository**: If you haven't already, clone the project's repository from GitHub:

   ```bash
   git clone https://github.com/yourusername/leetcode-progress-visualizer.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd leetcode-progress-visualizer
   ```

3. **Install Dependencies**: Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up WebDriver**:

    - Ensure that the Chrome WebDriver is downloaded and saved as `C:\ChromeDriver\chromedriver.exe` (or your preferred location).

5. **Configure Login Credentials**:

    - Open the `scraper.py` file.

    - Edit the `USERNAME` and `PASSWORD` variables with your LeetCode username and password. If you choose manual login, you can leave these fields empty.

6. **Run the Scraper**:

    - Run the scraper script to collect your LeetCode submission data:

   ```bash
   python scraper.py
   ```

7. **Start the Streamlit App**:

    - Once you have collected your data, start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

8. **Access the App**:

    - Open your web browser, and the app should be available at the URL `http://localhost:8501`.
    - 
















# LeetCode Analyser

## Overview

LeetCode Analyser is a Python project that empowers users to monitor and visualize their progress on the LeetCode platform. It scrapes user submission data, creates insightful visualizations, and offers recommendations to enhance performance. This README will guide you through the project's features, installation, and usage.

### Features

#### Data Scraping

The project uses the Selenium library in Python to scrape submission data from the LeetCode website. It navigates through login, submission pages, and question pages to extract essential information, including tags, name, ID, link, difficulty, and submission details.

#### Data Management

The scraped data is stored in a DataFrame. On subsequent runs, the program continues from the previous DataFrame and only scrapes new submissions, reducing redundancy.

#### Visualizations

**Accepted Submissions by Year and Status**:

![Accepted Submissions by Year and Status](https://example.com/accepted_submissions_status.png)

A bar plot that shows the count of accepted submissions over the years, with filters for submission status (Accepted, Runtime Error, Time Limit Exceeded).

**Accepted Submissions by Year and Difficulty**:

![Accepted Submissions by Year and Difficulty](https://example.com/accepted_submissions_difficulty.png)

Another bar plot illustrating the count of accepted submissions over the years, categorized by difficulty.

**Topic-wise Analysis**:

![Topic-wise Analysis](https://example.com/topic_wise_analysis.png)

Users can select specific tags and see the submission trends in a bar plot.

**Improvement Rate per Month**:

![Improvement Rate per Month](https://example.com/improvement_rate_monthly.png)

A line plot that represents the trend of submission counts over time, showing consistency and progress.

**Improvement Rate per Week**:

![Improvement Rate per Week](https://example.com/improvement_rate_weekly.png)

Similar to the monthly plot but with more detailed data at the week level.

#### Topic Recommendations

**Weakest Topics**:

![Weakest Topics](https://example.com/weakest_topics.png)

Recommendations for the weakest topics in Dynamic Programming, based on accepted questions from the dataset.

**Weak Topics**:

![Weak Topics](https://example.com/weak_topics.png)

Recommendations for weak topics based on user-defined threshold values.

### Demo

You can watch a video demonstration of the project [here](https://example.com).

Interact with the live demo of the project [here](https://example.com).

## Installation

To get started with LeetCode Analyser, follow these steps:

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/yourusername/leetcode-analyser.git
2. Navigate to the project directory:

   ```bash
   cd leetcode-analyser
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the scraper script to collect LeetCode submission data:

   ```bash
   python scraper.py
   ```

2. Once you have collected the data, start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Visit the app in your web browser (by default, it runs on `http://localhost:8501`).

4. Use the various visualization options and recommendations to track and improve your LeetCode performance.

## Contributors

- Your Name (YourGitHubProfile)
- Collaborator 1 (Collaborator1GitHubProfile)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Please replace the image URLs (`https://example.com/...`) with the actual URLs of your images, and it should render correctly in your README on GitHub.

9. **Interact and Visualize**:

    - Use the various visualization options and recommendations to monitor and enhance your LeetCode performance.

By following these steps, you'll have LeetCode Progress Visualizer up and running, allowing you to track your LeetCode journey with valuable insights.
