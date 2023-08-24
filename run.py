from analysis.preprocess import LeetAnalysis
from EDA.functions import Processing_class
with LeetAnalysis() as bot:
    bot.land_first_page()
    bot.login()
    bot.scrap_submission_page()
    bot.create_dataframe()

    # bot.trial()
