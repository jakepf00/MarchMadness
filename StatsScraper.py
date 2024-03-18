from bs4 import BeautifulSoup
import pathlib
import requests

statsToCollect = ["points-per-game", "opponent-points-per-game"]
statDates = {
    2000: "2000-04-04",
    2001: "2001-04-03",
    2002: "2002-04-02",
    2003: "2003-04-08",
    2004: "2004-04-06",
    2005: "2005-04-05",
    2006: "2006-04-04",
    2007: "2007-04-03",
    2008: "2008-04-08",
    2009: "2009-04-07",
    2010: "2010-04-06",
    2011: "2011-04-04",
    2012: "2012-04-02",
    2013: "2013-04-08",
    2014: "2014-04-07",
    2015: "2015-04-06",
    2016: "2016-04-05",
    2017: "2017-04-04",
    2018: "2018-04-03",
    2019: "2019-04-09",
    2020: "2020-03-12",
    2021: "2021-04-06",
    2022: "2022-04-05",
    2023: "2023-04-04",
    2024: "2024-03-19",
}


pathlib.Path("Stats/").mkdir(parents=True, exist_ok=True)

for year in range(2000, 2025):
    currentStats = {}

    # Collect stats for current year
    for statToCollect in statsToCollect:
        url = "https://www.teamrankings.com/ncaa-basketball/stat/" + statToCollect + "?date=" + statDates[year]
        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')
        for tableRow in soup.find_all('tr'):
            tableData = tableRow.find_all('td')
            if tableData: # If not in the table header
                school = tableData[1].attrs['data-sort']
                stat = tableData[2].attrs['data-sort']

                if school not in currentStats:
                    currentStats[school] = {}
                currentStats[school][statToCollect] = stat

    # Write current year stats to file
    statsFile = open("Stats/" + str(year) + ".txt", "w")
    for team in currentStats:
        statsFile.write(team.replace(" ", "") + " ")
        for stat in currentStats[team]:
            statsFile.write(str(currentStats[team][stat]) + " ")
        statsFile.write("\n")
    statsFile.close()