from analysis.preprocess import LeetAnalysis
with LeetAnalysis() as bot:
    bot.load_df()
    bot.land_first_page()
    bot.login()
    bot.scrap_submission_page()
    bot.scrap_each_page()
    bot.create_dataframe()
    bot.show_visuals()