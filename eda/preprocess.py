import pandas as pd
import pickle
from datetime import date
from datetime import datetime


def Preprocess_dataframe():
    dict_ = pickle.load(open('leet_dict.pkl', 'rb'))
    df = pd.DataFrame(dict_)

    df['DateOfSubmission'] = df['DateOfSubmission'].apply(Date_Conversion)
    df['Diff_encoded'] = df['Difficulty'].apply(difficulty_encoding)
    df['DateOfSubmission'] = pd.to_datetime(df['DateOfSubmission'])
    df['ID'] = df['ID'].astype('int64')
    df['Month'] = df['DateOfSubmission'].apply(get_month_name)
    df['Year'] = df['DateOfSubmission'].apply(get_year)
    df['Month_Year'] = df['Month'] + '-' + df['Year'].astype(str)
    df['Week'] = df['DateOfSubmission'].apply(get_week)
    df['Week_Year'] = df['Week'].astype(str) + '-' + df['Year'].astype(str)
    df['QName'] = df['Name'].apply(name_)

    return df


def process_dp(df, Threshold=30.0):
    dp_df = pd.read_csv('dp_leet.csv')
    dp_df['QName'] = dp_df['Question'].apply(get_name)
    a = dp_df['Category'].value_counts()
    not_done = dp_df[~dp_df['QName'].isin(df['QName'])]
    done = dp_df[dp_df['QName'].isin(df['QName'])]
    b = done['Category'].value_counts()

    dfn = pd.concat([a, b], axis=1)
    dfn = dfn.reset_index()
    dfn.columns = ['Category', 'All', 'Done']
    dfn['Done'] = dfn['Done'].fillna(0).astype(int)
    dfn['Percent'] = (dfn['Done'] / dfn['All']) * 100

    dfn_least_done = dfn.sort_values(by='Percent')
    len_ = dfn.shape[0]
    head_ = min(len_, 5)
    least = dfn_least_done.head(head_)['Category']

    dfn_most_done = dfn.sort_values(by='Percent', ascending=False)
    dfn_most_done = dfn_most_done[dfn_most_done['Percent'] < Threshold]
    most = dfn_most_done.head()['Category']

    least_to_do = not_done[not_done['Category'].isin(list(least))]
    most_to_do = not_done[not_done['Category'].isin(list(most))]

    ans_least = pd.DataFrame()
    ans_least = least_to_do[least_to_do['Category'] == 'a']
    for i in list(least):
        #     i = 'Math'
        cat = not_done[not_done['Category'] == i]
        new_ = cat.sample(3)
        ans_least = pd.concat([ans_least, new_], axis=0)

    ans_most = pd.DataFrame()
    ans_most = most_to_do[most_to_do['Category'] == 'a']
    for i in list(most):
        cat = not_done[not_done['Category'] == i]
        new_ = cat.sample(3)
        ans_most = pd.concat([ans_most, new_], axis=0)

    return a, b, ans_least, ans_most


month_dict = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}


def name_(s):
    s = s.lower()
    s = s.replace(' ', '-')
    return s


def get_name(s):
    t2 = s.split('https://leetcode.com/problems/')[1]
    t = t2.split('/')[0]
    return t


def get_week(s):
    return int(s.strftime("%U"))


def to_month_number(s):
    return month_dict[s]


def get_df_summary(df_status_acc):
    easy = []
    medium = []
    hard = []
    total = []
    month = []
    year = []
    month_year = []
    for u, v in df_status_acc.groupby('Month_Year'):
        mon = v['Month'].unique()[0]
        mon_year = v['Month_Year'].unique()[0]
        eas = v['Easy'].sum()
        med = v['Medium'].sum()
        har = v['Hard'].sum()
        tot = v['Total'].sum()
        yea = v['Year'].unique()[0]
        easy.append(eas)
        medium.append(med)
        hard.append(har)
        total.append(tot)
        month.append(mon)
        year.append(yea)
        month_year.append(mon_year)

    dict = {'Month': month, 'Year': year, 'Month_Year': month_year, 'Easy': easy, 'Medium': medium, 'Hard': hard,
            'Total': total}
    df_imp = pd.DataFrame(dict)
    df_imp['Month_no'] = df_imp['Month'].apply(to_month_number)
    df_imp.sort_values(by=['Year', 'Month_no'], inplace=True)
    return df_imp


def status_question(df, status='Accepted'):
    a_df = df[df['Status'] == status]
    easy = []
    medium = []
    hard = []
    dos_ = a_df.groupby('DateOfSubmission')
    dates = []
    for x, y in dos_:
        dates.append(x)
        dos = dos_.get_group(x)
        try:
            eas = dos.groupby('Difficulty').get_group('Easy')['Status'].count()
        except:
            eas = 0
        try:
            med = dos.groupby('Difficulty').get_group('Medium')['Status'].count()
        except:
            med = 0
        try:
            har = dos.groupby('Difficulty').get_group('Hard')['Status'].count()
        except:
            har = 0
        easy.append(eas)
        medium.append(med)
        hard.append(har)

    dict = {'Date': dates, 'Easy': easy, 'Medium': medium, 'Hard': hard}
    df_accepted = pd.DataFrame(dict)
    df_accepted['Total'] = df_accepted['Easy'] + df_accepted['Medium'] + df_accepted['Hard']
    df_accepted['Month'] = df_accepted['Date'].apply(get_month_name)
    df_accepted['Year'] = df_accepted['Date'].apply(get_year)
    df_accepted['Month_Year'] = df_accepted['Month'] + '-' + df_accepted['Year'].astype(str)
    df_accepted['Week'] = df_accepted['Date'].apply(get_week)
    df_accepted['Week_Year'] = df_accepted['Week'].astype(str) + '-' + df_accepted['Year'].astype(str)
    return df_accepted


def Date_Conversion(s):
    if 'hours' in s:
        return date.today()
    else:
        date_str_de_DE = s
        datetime_object = datetime.strptime(date_str_de_DE, '%b %d, %Y')
        return datetime_object.date()


def difficulty_encoding(s):
    if s == 'Hard':
        return 3
    elif s == 'Medium':
        return 2
    else:
        return 1


def get_month_name(s):
    return s.month_name()


def get_year(s):
    return s.year


def get_topics(df):
    topics = []
    for topic_list in df['Tags']:
        for topic in topic_list:
            if topic not in topics:
                topics.append(topic)
    return topics


def get_years(df):
    a = ['All Years']
    b = df['Year'].value_counts().index
    for i in b:
        a.append(i)
    return a


def get_df_week_summary(df_status_acc):
    easy = []
    medium = []
    hard = []
    total = []
    month = []
    week_year = []
    year = []
    month_year = []
    week = []
    for u, v in df_status_acc.groupby('Week_Year'):
        mon = v['Month'].unique()[0]
        wee_year = v['Week_Year'].unique()[0]
        mon_year = v['Month_Year'].unique()[0]
        eas = v['Easy'].sum()
        med = v['Medium'].sum()
        har = v['Hard'].sum()
        tot = v['Total'].sum()
        yea = v['Year'].unique()[0]
        wee = v['Week'].unique()[0]
        easy.append(eas)
        medium.append(med)
        hard.append(har)
        total.append(tot)
        month.append(mon)
        year.append(yea)
        month_year.append(mon_year)
        week_year.append(wee_year)
        week.append(wee)

    dict = {'Month': month, 'Year': year, 'Month_Year': month_year, 'Week_Year': week_year, 'Week': week, 'Easy': easy,
            'Medium': medium, 'Hard': hard, 'Total': total}
    df_imp = pd.DataFrame(dict)
    df_imp['Month_no'] = df_imp['Month'].apply(to_month_number)
    df_imp.sort_values(by=['Year', 'Week'], inplace=True)
    return df_imp


def accepted_questions(df, status='Accepted'):
    a_df = df[df['Status'] == status]
    easy = []
    medium = []
    hard = []
    dos_ = a_df.groupby('DateOfSubmission')
    dates = []
    for x, y in dos_:
        dates.append(x)
        dos = dos_.get_group(x)
        try:
            eas = dos.groupby('Difficulty').get_group('Easy')['Status'].count()
        except:
            eas = 0
        try:
            med = dos.groupby('Difficulty').get_group('Medium')['Status'].count()
        except:
            med = 0
        try:
            har = dos.groupby('Difficulty').get_group('Hard')['Status'].count()
        except:
            har = 0
        easy.append(eas)
        medium.append(med)
        hard.append(har)

    dict = {'Date': dates, 'Easy': easy, 'Medium': medium, 'Hard': hard}
    df_accepted = pd.DataFrame(dict)
    df_accepted['Total'] = df_accepted['Easy'] + df_accepted['Medium'] + df_accepted['Hard']
    df_accepted['Month'] = df_accepted['Date'].apply(get_month_name)
    df_accepted['Year'] = df_accepted['Date'].apply(get_year)
    return df_accepted


def get_per_date(df):
    tag_list = get_topics(df)
    cols = ['Status', 'DateOfSubmission', 'Difficulty', 'Tags', 'Month', 'Year']
    plot_df = df[cols]
    date_df = plot_df.groupby('DateOfSubmission')
    ans = []
    x_ = []
    for i, j in date_df:
        x_.append(i)
        dict = {}
        for i in tag_list:
            dict[i] = 0
        for x in j['Tags']:
            for k in x:
                dict[k] = dict[k] + 1
        ans.append(dict)

    for_each = []
    for topic in tag_list:
        tp = []
        for day, y in enumerate(x_):
            tp.append(ans[day][topic])
        for_each.append(tp)
    return x_, for_each