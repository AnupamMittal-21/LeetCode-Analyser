import plotly.graph_objects as go
from eda import preprocess
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")


class Main:

    def __init__(self):
        self.df = preprocess.Preprocess_dataframe()
        self.topic_list = preprocess.get_topics(self.df)
        self.year_list = preprocess.get_years(self.df)
        self.status_list = ['All Categories', 'Accepted', 'Wrong Answer', 'Runtime Error', 'Time Limit Exceeded']
        self.accepted_df = preprocess.accepted_questions(self.df)
        self.diff_list = ['All', 'Easy', 'Medium', 'Hard']
        # self.diff_list = ['All', 'Easy', 'Medium', 'Hard']

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __enter__(self):
        return self

    def your_analysis(self):

        st.subheader("Submission Counts")
        st.info('Filter your submissions based on Year and Status', icon="ℹ️")

        st.sidebar.markdown("""<style><hr></style>""", unsafe_allow_html=True)
        st.sidebar.header("Submission counts")
        selected_year = st.sidebar.selectbox("Select a Year", self.year_list)
        selected_status = st.sidebar.selectbox("Select a Status", self.status_list)

        if selected_status == 'All Categories':
            if selected_year == 'All Years':
                submission_counts_per_day_status = self.df.groupby("DateOfSubmission")['Diff_encoded'].count()
                fig = px.bar(submission_counts_per_day_status,
                             x=submission_counts_per_day_status.index,
                             y=submission_counts_per_day_status.values,
                             color=submission_counts_per_day_status.index.month_name(),
                             text=submission_counts_per_day_status.values)
                fig.update_traces(textposition='outside')
                fig.update_layout(uniformtext_minsize=8)
                fig.update_layout(xaxis_tickangle=-45)
                fig.update_layout(
                    autosize=False,
                    width=1000,
                    height=700,
                    title="Submissions count for all years and all categories",
                    xaxis_title="Date of Submission",
                    yaxis_title="No. of Submissions",
                    legend_title="Months",
                    font=dict(
                        family="Courier New, monospace",
                        size=18,
                        color="RebeccaPurple"
                    )
                )
                st.plotly_chart(fig)
            else:
                new_df = self.df[self.df['Year'] == selected_year]
                submission_counts_per_day_status = new_df.groupby("DateOfSubmission")['Diff_encoded'].count()
                fig = px.bar(submission_counts_per_day_status,
                             x=submission_counts_per_day_status.index,
                             y=submission_counts_per_day_status.values,
                             color=submission_counts_per_day_status.index.month_name(),
                             text=submission_counts_per_day_status.values)
                fig.update_traces(textposition='outside')
                fig.update_layout(uniformtext_minsize=8)
                fig.update_layout(xaxis_tickangle=-45)
                fig.update_layout(
                    autosize=False,
                    width=1000,
                    height=700,
                    title=f"Submissions count for year {selected_year} and all categories",
                    xaxis_title="Date of Submission",
                    yaxis_title=f"No. of Submissions in {selected_year}",
                    legend_title="Months",
                    font=dict(
                        family="Courier New, monospace",
                        size=18,
                        color="RebeccaPurple"
                    )
                )
                st.plotly_chart(fig)

        else:
            new_df = self.df[self.df['Status'] == selected_status]
            if selected_year == 'All Years':
                submission_counts_per_day_status = new_df.groupby("DateOfSubmission")['Diff_encoded'].count()
                fig = px.bar(submission_counts_per_day_status,
                             x=submission_counts_per_day_status.index,
                             y=submission_counts_per_day_status.values,
                             color=submission_counts_per_day_status.index.month_name(),
                             text=submission_counts_per_day_status.values)
                fig.update_traces(textposition='outside')
                fig.update_layout(uniformtext_minsize=8)
                fig.update_layout(xaxis_tickangle=-45)
                fig.update_layout(
                    autosize=False,
                    width=1000,
                    height=700,
                    title=f"Submissions count for all years and {selected_status}",
                    xaxis_title="Date of Submission",
                    yaxis_title="No. of Submissions",
                    legend_title="Months",
                    font=dict(
                        family="Courier New, monospace",
                        size=18,
                        color="RebeccaPurple"
                    )
                )
                st.plotly_chart(fig)
            else:
                new_df = new_df[new_df['Year'] == selected_year]
                submission_counts_per_day_status = new_df.groupby("DateOfSubmission")['Diff_encoded'].count()
                fig = px.bar(submission_counts_per_day_status,
                             x=submission_counts_per_day_status.index,
                             y=submission_counts_per_day_status.values,
                             color=submission_counts_per_day_status.index.month_name(),
                             text=submission_counts_per_day_status.values)
                fig.update_traces(textposition='outside')
                fig.update_layout(uniformtext_minsize=8)
                fig.update_layout(xaxis_tickangle=-45)
                fig.update_layout(
                    autosize=False,
                    width=1000,
                    height=700,
                    title=f"Submissions count for year {selected_year} and {selected_status}",
                    xaxis_title="Date of Submission",
                    yaxis_title=f"No. of Submissions in {selected_year}",
                    legend_title="Months",
                    font=dict(
                        family="Courier New, monospace",
                        size=18,
                        color="RebeccaPurple"
                    )
                )
                st.plotly_chart(fig)

    def display_accepted_submissions(self):

        st.markdown("""<style><br></style>""", unsafe_allow_html=True)

        st.subheader("Submission Trends")
        st.info('Filter your submissions based on Year and Difficulty', icon="ℹ️")
        st.markdown("""<style><hr></style>""", unsafe_allow_html=True)

        st.sidebar.markdown("""<style><hr></style>""", unsafe_allow_html=True)
        st.sidebar.header("Submission Trend")
        selected_year = st.sidebar.selectbox("Select a Year", self.year_list, key="acc")
        selected_diff = st.sidebar.selectbox("Select a Difficulty", self.diff_list)
        new_df = self.accepted_df
        if selected_diff != "All":
            if selected_year != 'All Years':
                new_df = new_df[new_df['Year'] == selected_year]
            fig = px.bar(new_df,
                         x=new_df.Date,
                         y=new_df[selected_diff],
                         text=new_df.Total,
                         hover_data=f'{selected_diff}',
                         color=new_df.Month)
            fig.update_traces(textposition='outside')
            fig.update_layout(uniformtext_minsize=8)
            fig.update_layout(xaxis_tickangle=-45)
            fig.update_layout(
                autosize=False,
                width=1000,
                height=700,
                title=f"Accepted Submission per Day of difficulty : {selected_diff} in {selected_year} ",
                xaxis_title="Date of Submission",
                yaxis_title="No. of accepted Submissions",
                legend_title="Months",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="RebeccaPurple"
                )
            )
            st.plotly_chart(fig)
        else:
            if selected_year != 'All Years':
                new_df = self.accepted_df[self.accepted_df['Year'] == selected_year]
            fig = px.bar(new_df,
                         x=new_df.Date,
                         y=new_df.Total,
                         hover_data=['Easy', 'Medium', 'Hard'],
                         color=new_df.Month)
            fig.update_traces(textposition='outside')
            fig.update_layout(uniformtext_minsize=8)
            fig.update_layout(xaxis_tickangle=-45)
            fig.update_layout(
                autosize=False,
                width=1000,
                height=700,
                title=f"Accepted Submission per Day with all difficulty in {selected_year}",
                xaxis_title="Date of Submission",
                yaxis_title="No. of accepted Submissions",
                legend_title="Months",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="RebeccaPurple"
                )
            )
            st.plotly_chart(fig)

    def display_topic_wise(self):
        st.markdown("""<style><br></style>""", unsafe_allow_html=True)
        st.subheader("Topic-Wise")
        st.info('Filter your submissions based on Topics (Categories)', icon="ℹ️")
        st.markdown("""<style><hr></style>""", unsafe_allow_html=True)
        st.sidebar.markdown("""<style><hr></style>""", unsafe_allow_html=True)
        st.sidebar.header("Topic-Wise")
        selected_tags = st.sidebar.multiselect(
            "Seleect Topics (Atmost 5)",
            self.topic_list,
            max_selections=5,
        )

        def fun(tag_list):
            for tag in tag_list:
                if tag in selected_tags:
                    return True
            return False

        if len(selected_tags) == 0:
            st.warning("Choose Tags to see analysis (Atleast : 1, Atmost : 5)")
        else:
            df_tags = self.df[self.df["Tags"].apply(fun)]
            df_tags = preprocess.accepted_questions(df_tags)

            fig = px.bar(df_tags,
                         x=df_tags['Date'],
                         y=df_tags['Total'],
                         color=df_tags['Month'],
                         hover_data=['Total'],
                         text=df_tags['Total'])
            fig.update_traces(textposition='outside')
            fig.update_layout(uniformtext_minsize=8)
            fig.update_layout(xaxis_tickangle=-45)
            fig.update_layout(
                autosize=False,
                width=1000,
                height=700,
                title="Submissions count for selected topics",
                xaxis_title="Date of Submission",
                yaxis_title="No. of Submissions",
                legend_title="Months",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="RebeccaPurple"
                )
            )
            st.plotly_chart(fig)

    def improvement_rate_per_month(self):
        st.subheader("Improvement rate per month")
        st.info('This plot represents the submissions trend over time grouped by month', icon="ℹ️")
        st.markdown("""<style><hr></style>""", unsafe_allow_html=True)
        st.sidebar.markdown("""<style><hr></style>""", unsafe_allow_html=True)

        st.sidebar.header('Improvement Rate (Month)')
        # This has a slight problem of shifting of x-axis elements.
        selected_year = st.sidebar.selectbox('Select a Year', self.year_list, key="month")

        fig = go.Figure()
        new_df = self.df
        if selected_year != 'All Years':
            new_df = new_df[new_df['Year'] == selected_year]
        for status in self.status_list[1:-1]:
            df_status_acc = preprocess.status_question(new_df, status)
            df_imp_acc = preprocess.get_df_summary(df_status_acc)
            fig.add_trace(go.Scatter(x=df_imp_acc.Month_Year, y=df_imp_acc.Total, mode='lines+markers', name=status))

        fig.update_layout(
            autosize=False,
            width=1000,
            height=600,
            title=f'Improvement Rate per month in {selected_year}',
            xaxis_title='Timeline',
            yaxis_title='Status Count',
            legend_title="Status",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
            )
        )
        st.plotly_chart(fig)

    def improvement_rate_per_week(self):

        st.markdown("""<style><br></style>""", unsafe_allow_html=True)
        st.markdown("""<style><br></style>""", unsafe_allow_html=True)
        st.subheader("Improvement rate per week")
        st.info('This plot represents the submissions trend over time grouped by week', icon="ℹ️")
        st.markdown("""<style><hr></style>""", unsafe_allow_html=True)
        st.sidebar.markdown("""<style><hr></style>""", unsafe_allow_html=True)

        st.sidebar.header('Improvement Rate (Week)')
        selected_year = st.sidebar.selectbox('Select a Year', self.year_list, key="Week")
        fig = go.Figure()
        new_df = self.df
        if selected_year != 'All Years':
            new_df = new_df[new_df['Year'] == selected_year]
        for status in self.status_list[1:-1]:
            df_status_acc = preprocess.status_question(new_df, status)
            df_imp_acc = preprocess.get_df_week_summary(df_status_acc)
            fig.add_trace(go.Scatter(x=df_imp_acc.Week_Year, y=df_imp_acc.Total, mode='lines+markers', name=status))
        fig.update_layout(
            autosize=False,
            width=1000,
            height=600,
            title=f'Improvement Rate per Week in {selected_year}',
            xaxis_title='Timeline',
            yaxis_title='Status Count',
            legend_title="Status",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
            )
        )
        st.plotly_chart(fig)

    def monthwise_status(self):

        st.markdown("""<style><br></style>""", unsafe_allow_html=True)
        st.markdown("""<style><br></style>""", unsafe_allow_html=True)
        st.subheader("Month-Wise Status")
        st.info('This plot represents the count of types of submissions over time grouped by month', icon="ℹ️")
        st.markdown("""<style><hr></style>""", unsafe_allow_html=True)
        st.sidebar.markdown("""<style><hr></style>""", unsafe_allow_html=True)

        # Same problem of not having ordered x-axis
        st.sidebar.header("Month-Wise Status")

        name = "IDK"
        selected_year = st.sidebar.selectbox(
            'Select a Year',
            self.year_list, key=f"{name}",
        )
        if selected_year == 'All Years':
            fig = px.bar(self.df, x='Month_Year', y='Diff_encoded', color='Status',
                         title='Month-wise count of questions status.')
            fig.update_layout(
                autosize=False,
                width=1000,
                height=600,
                title=f'Improvement Rate per Week in {selected_year}',
                xaxis_title='Timeline',
                yaxis_title='Status Count',
                legend_title="Status",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="RebeccaPurple"
                )
            )
            st.plotly_chart(fig)
        else:
            df_2023 = self.df[self.df['Year'] == selected_year]
            fig = px.bar(df_2023, x='Month', y='Diff_encoded', color='Status',
                         title='Month-wise count of questions status.')
            fig.update_layout(
                autosize=False,
                width=1000,
                height=600,
                title=f'Improvement Rate per Week in {selected_year}',
                xaxis_title='Timeline',
                yaxis_title='Status Count',
                legend_title="Status",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="RebeccaPurple"
                )
            )
            st.plotly_chart(fig)

    def topics_heatmap(self):
        st.subheader("Topic-Wise Analysis (HeatMap)")
        st.info('This plot represents the date,Topic, No. of submissions of that topic on that date over time',
                icon="ℹ️")
        st.markdown("""<style><hr></style>""", unsafe_allow_html=True)
        st.sidebar.markdown("""<style><hr></style>""", unsafe_allow_html=True)

        st.sidebar.header("Topic-Analysis (HeatMap)")

        x_, for_each = preprocess.get_per_date(self.df)
        data = for_each

        # Create the heatmap trace
        heatmap_trace = go.Heatmap(z=data, x=x_, y=self.topic_list, colorscale='Blackbody')

        # Create a figure with the trace and layout
        fig = go.Figure(data=[heatmap_trace])
        fig.update_layout(
            autosize=False,
            width=1000,
            height=700,
            title=f'Topic-Wise per day submission count(HeatMap)',
            xaxis_title='Timeline',
            legend_title="Colorscale",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
            )
        )
        st.plotly_chart(fig)

    def topics_scatter(self):

        # Years are not getting modified
        st.subheader("Topic-Wise Analysis (ScatterPlot)")
        st.info('This plot represents the date,Topic, No. of submissions of that topic on that date over time',
                icon="ℹ️")
        st.markdown("""<style><hr></style>""", unsafe_allow_html=True)
        st.sidebar.markdown("""<style><hr></style>""", unsafe_allow_html=True)

        st.sidebar.header("Topic-Analysis (ScatterPlot)")
        new_df = self.df

        x_, for_each = preprocess.get_per_date(new_df)
        data = for_each

        fig = go.Figure()
        for i, j in enumerate(self.topic_list):
            a = [i] * len(x_)
            fig.add_trace(go.Scatter(
                x=x_,
                y=a,
                mode='markers',
                marker={'size': [size * 2 for size in for_each[i]]},
                name=self.topic_list[i],
            ))

        fig.update_layout(
            autosize=False,
            width=1000,
            height=830,
            title=f'Topic-Wise per day submission count(Scatter Plot)',
            xaxis_title='Timeline',
            legend_title="Topics",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
            )
        )
        st.plotly_chart(fig)

    def get_ok_and_weak_topics(self):

        st.subheader("Questions Recommendation")
        st.markdown("""<style><hr></style>""", unsafe_allow_html=True)
        st.sidebar.markdown("""<style><hr></style>""", unsafe_allow_html=True)

        st.sidebar.header("Questions you should practice")
        st.sidebar.write("Weakest topics and weak topics ")

        selected_thres = st.sidebar.slider("Enter Threshold value", 1, 100, 30)
        st.sidebar.info('Threshold means percent of questions you want to do.', icon="ℹ️")

        a, b, ans_least, ans_most = preprocess.process_dp(self.df, selected_thres)

        st.subheader("Weakest-Topics")
        st.info('Weakest topics means those topics which you have done the least.', icon="ℹ️")
        ans_least = ans_least.reset_index()
        ans_least = ans_least[['QName', 'Category', 'Question']]
        st.write(ans_least)

        st.markdown("""<style><hr></style>""", unsafe_allow_html=True)
        st.sidebar.markdown("""<style><hr></style>""", unsafe_allow_html=True)

        st.subheader("Weak-Topics")
        st.info('Weak topics means those topics which you have done the most but not upto the threshold limit.',
                icon="ℹ️")
        ans_most = ans_most.reset_index()
        ans_most = ans_most[['QName', 'Category', 'Question']]
        st.write(ans_most)

        st.subheader("Question-Categories Count of Done/Not done")
        col1, col2 = st.columns(2)
        with col1:
            st.info('You have not done these many questions of this particular category.', icon="ℹ️")
            st.write(a)
        with col2:
            st.info('You have done these many questions of this particular category.', icon="ℹ️")
            st.write(b)

        st.info(
            "Threshold value determine the percent which you think is enough for practice that determines the weak topics")

    def compare_profiles(self):
        pass

    def initial_options(self):
        st.sidebar.header("Welcome to LeetAnalyser...")
        # st.sidebar.file_uploader(label = 'Upload CSV file', type = ['csv','xsl'])
        # st.sidebar.warning('Either Enter Login Credentials or drag and drop csv file')
        # username = st.sidebar.text_input("Username")
        # password = st.sidebar.text_input("Password", type="password")
        selected_option = st.sidebar.radio("Select an option...\n",
                                           ["Submission Trend", "Improvement Rate", "Topic-Wise "
                                                                                    "Analysis",
                                            "Question Recommendation"])

        if selected_option == "Submission Trend":
            self.your_analysis()
            self.display_accepted_submissions()
            self.display_topic_wise()

        if selected_option == "Improvement Rate":
            self.improvement_rate_per_month()
            self.improvement_rate_per_week()
            self.monthwise_status()

        if selected_option == "Topic-Wise Analysis":
            selected_option_2 = st.sidebar.selectbox("Choose a plot", ["Both", "HeatMap", "ScatterPlot"])

            if selected_option_2 == "Both":
                self.topics_heatmap()
                self.topics_scatter()

            if selected_option_2 == "HeatMap":
                self.topics_heatmap()

            if selected_option_2 == "ScatterPlot":
                self.topics_scatter()

        if selected_option == "Question Recommendation":
            self.get_ok_and_weak_topics()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with Main() as bot:
        bot.initial_options()
