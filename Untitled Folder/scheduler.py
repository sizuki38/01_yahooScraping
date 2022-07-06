from get_Scraping import *

schedule.every().day.at("13:30").do(get_list)
schedule.every().day.at("14:30").do(get_news)
schedule.every().day.at("23:30").do(get_comment)

while True:
    schedule.run_pending()
    time.sleep(1)
