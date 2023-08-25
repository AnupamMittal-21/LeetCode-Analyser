from analysis.preprocess import LeetAnalysis
with LeetAnalysis() as bot:
    bot.land_first_page()
    bot.login()
    bot.scrap_submission_page()
    bot.create_dataframe()

    # bot.trial()
