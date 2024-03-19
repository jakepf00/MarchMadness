from bs4 import BeautifulSoup
import datetime
import pathlib
import requests

def generateUrls2024():
    begin_2024 = datetime.datetime(2023, 11, 6)
    end_2024 = datetime.datetime.now()
    delta_2024 = end_2024 - begin_2024
    dates_2024 = [begin_2024 + datetime.timedelta(days=x) for x in range(delta_2024.days)]
    return ["https://www.ncaa.com/scoreboard/basketball-men/d1/" + x.strftime("%Y") + "/" + x.strftime("%m") + "/" + x.strftime("%d") + "/all-conf" for x in dates_2024]

games_2024 = generateUrls2024()

pathlib.Path("Games/").mkdir(parents=True, exist_ok=True)
gameFile = open("Games/2024.csv", "w")

for game_url in games_2024:
    r = requests.get(game_url)
    soup = BeautifulSoup(r.content, "html.parser")

    games_list = soup.find('div', class_ = "gamePod_content-pod_container").find_all(class_ = "gamePod gamePod-type-game status-final")

    for game in games_list:
        team1 = game.find_all('li')[0]
        team2 = game.find_all('li')[1]

        team1_name = team1.find('span', class_ = "gamePod-game-team-name").text
        team1_score = team1.find('span', class_ = "gamePod-game-team-score").text
        team2_name = team2.find('span', class_ = "gamePod-game-team-name").text
        team2_score = team2.find('span', class_ = "gamePod-game-team-score").text

        point_diff = str(int(team1_score) - int(team2_score))

        gameFile.write(team1_name.replace(" ", "_") + "," + team2_name.replace(" ", "_") + "," + point_diff + "\n")



