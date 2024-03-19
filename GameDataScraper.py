import datetime

def generateUrls2024():
    begin_2024 = datetime.datetime(2023, 11, 6)
    end_2024 = datetime.datetime.now()
    delta_2024 = end_2024 - begin_2024
    dates_2024 = [begin_2024 + datetime.timedelta(days=x) for x in range(delta_2024.days)]
    return ["https://www.ncaa.com/scoreboard/basketball-men/d1/" + x.strftime("%Y") + "/" + x.strftime("%m") + "/" + x.strftime("%d") + "/all-conf" for x in dates_2024]

games2024 = generateUrls2024()
print(games2024)