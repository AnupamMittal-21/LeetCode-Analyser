from analysis.preprocess import LeetAnalysis

with LeetAnalysis() as bot:
    bot.land_first_page()
    bot.login()
    bot.scrap_submission_page()
    bot.scrap_info_from_a_page()
    # bot.create_dataframe()