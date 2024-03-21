import csv
import pathlib

# Dictionary to convert between team names on ncaa.com and teamrankings.com
nameConversion = {
    "Ark._Baptist": "AR_Lit_Rock",
    "Abilene_Christian": "Abl_Christian",
    "Air_Force": "Air_Force",
    "Akron": "Akron",
    "Alabama_A&M": "Alab_A&M",
    "Alabama": "Alabama",
    "Alabama_St.": "Alabama_St",
    "Albany_St._(GA)": "Albany",
    "Alcorn": "Alcorn_St",
    "American": "American",
    "App_State": "App_State",
    "Arizona": "Arizona",
    "Arizona_St.": "Arizona_St",
    "Ark.-Pine_Bluff": "Ark_Pine_Bl",
    "Arkansas": "Arkansas",
    "Arkansas_St.": "Arkansas_St",
    "Army_West_Point": "Army",
    "Auburn": "Auburn",
    "Austin_Peay": "Austin_Peay",
    "BYU": "BYU",
    "Ball_St.": "Ball_St",
    "Baylor": "Baylor",
    "Bellarmine": "Bellarmine",
    "Belmont": "Belmont",
    "Bethune-Cookman": "Beth-Cook",
    "Binghamton": "Binghamton",
    "Boise_St.": "Boise_St",
    "Boston_College": "Boston_Col",
    "Boston_U.": "Boston_U",
    "Bowling_Green": "Bowling_Grn",
    "Bradley": "Bradley",
    "Brown": "Brown",
    "Bryant": "Bryant",
    "Bucknell": "Bucknell",
    "Buffalo": "Buffalo",
    "Butler": "Butler",
    "Cal_St._Fullerton": "CS_Fullerton",
    "California_Baptist": "Cal_Baptist",
    "Cal_Poly": "Cal_Poly",
    "California": "California",
    "Campbell": "Campbell",
    "Canisius": "Canisius",
    "Central_Ark.": "Central_Ark",
    "Central_Conn._St.": "Central_Conn",
    "Central_Mich.": "Central_Mich",
    "Charleston_So.": "Charl_South",
    "Charlotte": "Charlotte",
    "Chattanooga": "Chattanooga",
    "Chicago_St.": "Chicago_St",
    "Cincinnati": "Cincinnati",
    "Clemson": "Clemson",
    "Cleveland_St.": "Cleveland_St",
    "Coastal_Carolina": "Coastal_Car",
    "Col._of_Charleston": "Col_Charlestn",
    "Colgate": "Colgate",
    "Colorado": "Colorado",
    "Colorado_St.": "Colorado_St",
    "Columbia": "Columbia",
    "UConn": "Connecticut",
    "Coppin_St.": "Coppin_St",
    "Cornell": "Cornell",
    "Creighton": "Creighton",
    "Dartmouth": "Dartmouth",
    "Davidson": "Davidson",
    "Dayton": "Dayton",
    "DePaul": "DePaul",
    "Delaware": "Delaware",
    "Delaware_St.": "Delaware_St",
    "Denver": "Denver",
    "Detroit_Mercy": "Detroit",
    "Drake": "Drake",
    "Drexel": "Drexel",
    "Duke": "Duke",
    "Duquesne": "Duquesne",
    "East_Carolina": "E_Carolina",
    "Eastern_Ill.": "E_Illinois",
    "Eastern_Ky.": "E_Kentucky",
    "Eastern_Mich.": "E_Michigan",
    "ETSU": "E_Tenn_St",
    "Eastern_Wash.": "E_Washingtn",
    "Elon": "Elon",
    "Evansville": "Evansville",
    "FDU": "F_Dickinson",
    "Fairfield": "Fairfield",
    "Fla._Atlantic": "Fla_Atlantic",
    "Florida": "Florida",
    "Florida_A&M": "Florida_A&M",
    "Florida_St.": "Florida_St",
    "Fordham": "Fordham",
    "Fresno_St.": "Fresno_St",
    "Furman": "Furman",
    "Ga._Southern": "GA_Southern",
    "Georgia_Tech": "GA_Tech",
    "Gardner-Webb": "Gard-Webb",
    "George_Mason": "Geo_Mason",
    "George_Washington": "Geo_Wshgtn",
    "Georgetown": "Georgetown",
    "Georgia": "Georgia",
    "Georgia_St.": "Georgia_St",
    "Gonzaga": "Gonzaga",
    "Grambling": "Grambling_St",
    "Grand_Canyon": "Grd_Canyon",
    "Hampton": "Hampton",
    "Harvard": "Harvard",
    "Hawaii": "Hawaii",
    "High_Point": "High_Point",
    "Hofstra": "Hofstra",
    "Holy_Cross": "Holy_Cross",
    "Houston": "Houston",
    "Howard": "Howard",
    "Houston_Christian": "Hsn_Christian",
    "IUPUI": "IUPUI",
    "Idaho": "Idaho",
    "Idaho_St.": "Idaho_St",
    "Illinois": "Illinois",
    "Illinois_St.": "Illinois_St",
    "UIW": "Incar_Word",
    "Indiana": "Indiana",
    "Indiana_St.": "Indiana_St",
    "Iona": "Iona",
    "Iowa": "Iowa",
    "Iowa_St.": "Iowa_St",
    "Jackson_St.": "Jackson_St",
    "Jacksonville": "Jacksonville",
    "James_Madison": "James_Mad",
    "Jacksonville_St.": "Jksnville_St",
    "Kansas": "Kansas",
    "Kansas_City": "Kansas_City",
    "Kansas_St.": "Kansas_St",
    "Kennesaw_St.": "Kennesaw_St",
    "Kent_St.": "Kent_St",
    "Kentucky": "Kentucky",
    "LIU": "LIU",
    "LSU": "LSU",
    "La_Salle": "La_Salle",
    "Lafayette": "Lafayette",
    "Lamar_University": "Lamar",
    "LeMoyne-Owen": "Le_Moyne",
    "Lehigh": "Lehigh",
    "Long_Beach_St.": "Lg_Beach_St",
    "Liberty": "Liberty",
    "Lindenwood": "Lindenwood",
    "Lipscomb": "Lipscomb",
    "Longwood": "Longwood",
    "Louisiana": "Louisiana",
    "Louisville": "Louisville",
    "Loyola_Chicago": "Loyola-Chi",
    "Loyola_Maryland": "Loyola-MD",
    "Loyola_(LA)": "Loyola_Mymt",
    "Maine": "Maine",
    "Manhattan": "Manhattan",
    "Marist": "Marist",
    "Marquette": "Marquette",
    "Marshall": "Marshall",
    "Maryland": "Maryland",
    "UMBC": "Maryland_BC",
    "UMES": "Maryland_ES",
    "McNeese": "McNeese_St",
    "Memphis": "Memphis",
    "Mercer": "Mercer",
    "Merrimack": "Merrimack",
    "Miami_(FL)": "Miami",
    "Miami_(OH)": "Miami_(OH)",
    "Michigan": "Michigan",
    "Michigan_St.": "Michigan_St",
    "Middle_Tenn.": "Middle_Tenn",
    "Minnesota": "Minnesota",
    "Mississippi_St.": "Miss_State",
    "Mississippi_Val.": "Miss_Val_St",
    "Mississippi_Col.": "Mississippi",
    "Missouri": "Missouri",
    "Missouri_St.": "Missouri_St",
    "Monmouth": "Monmouth",
    "Montana": "Montana",
    "Montana_St.": "Montana_St",
    "Morehead_St.": "Morehead_St",
    "Morgan_St.": "Morgan_St",
    "Mount_St._Mary's": "Mt_St_Marys",
    "Murray_St.": "Murray_St",
    "N.C._A&T": "NC_A&T",
    "N.C._Central": "NC_Central",
    "NC_State": "NC_State",
    "NJIT": "NJIT",
    "Northwestern_St.": "NW_State",
    "North_Ala.": "N_Alabama",
    "Northern_Ariz.": "N_Arizona",
    "North_Carolina": "N_Carolina",
    "Northern_Colo.": "N_Colorado",
    "North_Dakota_St.": "N_Dakota_St",
    "North_Florida": "N_Florida",
    "New_Hampshire": "N_Hampshire",
    "NIU": "N_Illinois",
    "UNI": "N_Iowa",
    "Northern_Ky.": "N_Kentucky",
    "New_Mexico_St.": "N_Mex_State",
    "Navy": "Navy",
    "Omaha": "Neb_Omaha",
    "Nebraska": "Nebraska",
    "Nevada": "Nevada",
    "New_Mexico": "New_Mexico",
    "New_Orleans": "New_Orleans",
    "Niagara": "Niagara",
    "Nicholls": "Nicholls",
    "Norfolk_St.": "Norfolk_St",
    "North_Dakota": "North_Dakota",
    "North_Texas": "North_Texas",
    "Northeastern": "Northeastrn",
    "Northwestern": "Northwestern",
    "Notre_Dame": "Notre_Dame",
    "Oakland": "Oakland",
    "Ohio": "Ohio",
    "Ohio_St": "Ohio_St",
    "Oklahoma": "Oklahoma",
    "Oklahoma_St.": "Oklahoma_St",
    "Old_Dominion": "Old_Dominion",
    "Oral_Roberts": "Oral_Roberts",
    "Oregon": "Oregon",
    "Oregon_St.": "Oregon_St",
    "Pacific": "Pacific",
    "Penn_St.": "Penn_St",
    "Pepperdine": "Pepperdine",
    "Pittsburgh": "Pittsburgh",
    "Portland": "Portland",
    "Portland_St.": "Portland_St",
    "Prairie_View": "Prairie_View",
    "Presbyterian": "Presbyterian",
    "Princeton": "Princeton",
    "Providence": "Providence",
    "Purdue": "Purdue",
    "Queens_(NC)": "Queens",
    "Quinnipiac": "Quinnipiac",
    "Radford": "Radford",
    "Rhode_Island": "Rhode_Island",
    "Rice": "Rice",
    "Richmond": "Richmond",
    "Rider": "Rider",
    "Robert_Morris": "Rob_Morris",
    "Rutgers": "Rutgers",
    "Southeastern_La.": "SE_Louisiana",
    "Southeast_Mo._St.": "SE_Missouri",
    "SIUE": "SIU_Edward",
    "South_Alabama": "S_Alabama",
    "South_Carolina_St.": "S_Car_State",
    "South_Carolina": "S_Carolina",
    "South_Dakota_St.": "S_Dakota_St",
    "South_Fla.": "S_Florida",
    "Southern_Ill.": "S_Illinois",
    "Southern_Miss.": "S_Mississippi",
    "Southern_Utah": "S_Utah",
    "Sacramento_St.": "Sac_State",
    "Sacred_Heart": "Sacred_Hrt",
    "Saint_Louis": "Saint_Louis",
    "Sam_Houston": "Sam_Hous_St",
    "Samford": "Samford",
    "San_Diego": "San_Diego",
    "San_Diego_St.": "San_Diego_St",
    "San_Francisco": "San_Francisco",
    "San_Jose_St.": "San_Jose_St",
    "Santa_Clara": "Santa_Clara",
    "Seattle_U": "Seattle",
    "Seton_Hall": "Seton_Hall",
    "Siena": "Siena",
    "South_Dakota": "South_Dakota",
    "St._Thomas_(MN)": "St._Thomas",
    "St._Bonaventure": "St_Bonavent",
    "Saint_Francis_(PA)": "St_Fran_(PA)",
    "St._John's_(NY)": "St_Johns",
    "St._Joseph's_(L.I.)": "St_Josephs",
    "Saint_Mary's_(CA)": "St_Marys",
    "Saint_Peter's": "St_Peters",
    "Stanford": "Stanford",
    "SFA": "Ste_F_Austin",
    "Stetson": "Stetson",
    "Stonehill": "Stonehill",
    "Stony_Brook": "Stony_Brook",
    "Syracuse": "Syracuse",
    "Tennessee_St.": "TN_State",
    "Tennessee_Tech": "TN_Tech",
    "UT_Arlington": "TX-Arlington",
    "Tex._A&M-Commerce": "TX_A&M-Com",
    "TCU": "TX_Christian",
    "UTEP": "TX_El_Paso",
    "Texas_Southern": "TX_Southern",
    "Tarleton_St.": "Tarleton_St",
    "Temple": "Temple",
    "Tennessee": "Tennessee",
    "Texas": "Texas",
    "Texas_A&M": "Texas_A&M",
    "Texas_St.": "Texas_St",
    "Texas_Tech": "Texas_Tech",
    "Toledo": "Toledo",
    "Towson": "Towson",
    "Troy": "Troy",
    "Tulane": "Tulane",
    "Tulsa": "Tulsa",
    "UAB": "UAB",
    "UCF": "UCF",
    "UCLA": "UCLA",
    "UC_Santa_Barbara": "UCSB",
    "UC_San_Diego": "UCSD",
    "UC_Davis": "UC_Davis",
    "UC_Irvine": "UC_Irvine",
    "UC_Riverside": "UC_Riverside",
    "ULM": "UL_Monroe",
    "UNLV": "UNLV",
    "Southern_California": "USC",
    "UTSA": "UTSA",
    "Massachusetts": "U_Mass",
    "Penn": "U_Penn",
    "Utah": "Utah",
    "Utah_St.": "Utah_St",
    "Utah_Tech": "Utah_Tech",
    "Utah_Valley": "Utah_Valley",
    "Virginia_Tech": "VA_Tech",
    "VCU": "VCU",
    "VMI": "VMI",
    "Valparaiso": "Valparaiso",
    "Vanderbilt": "Vanderbilt",
    "Vermont": "Vermont",
    "Villanova": "Villanova",
    "Virginia": "Virginia",
    "Western_Caro.": "W_Carolina",
    "Western_Ill.": "W_Illinois",
    "Western_Ky.": "W_Kentucky",
    "Western_Mich.": "W_Michigan",
    "West_Virginia": "W_Virginia",
    "Wagner": "Wagner",
    "Wake_Forest": "Wake_Forest",
    "Washington_St.": "Wash_State",
    "Washington": "Washington",
    "Weber_St.": "Weber_St",
    "Wichita_St.": "Wichita_St",
    "Winthrop": "Winthrop",
    "Wisconsin": "Wisconsin",
    "William_&_Mary": "Wm_&_Mary",
    "Wofford": "Wofford",
    "Wright_St.": "Wright_St",
    "Wyoming": "Wyoming",
    "Xavier": "Xavier",
    "Yale": "Yale",
    "Youngstown_St.": "Youngs_St",
}

pathlib.Path("TrainingData/").mkdir(parents=True, exist_ok=True)
trainingFileX = open("TrainingData/2024x.csv", "w")
trainingFileY = open("TrainingData/2024y.csv", "w")
gameFile = open("Games/2024.csv", "r")
statsFile = open("Stats/2024.csv", "r")

teamStats = {}

statsReader = csv.reader(statsFile)
for row in statsReader:
    stats = []
    for i in range(1, len(row)):
        stats.append(row[i])
    teamStats[row[0]] = stats

gameReader = csv.reader(gameFile)
for row in gameReader:
    if row[0] in nameConversion and row[1] in nameConversion:
        # Get team stats and write them in row of trainingFileX
        statsToWrite = teamStats[nameConversion[row[0]]] + teamStats[nameConversion[row[1]]]
        for i in range(0, len(statsToWrite)):
            trainingFileX.write(statsToWrite[i])
            if i != len(statsToWrite) - 1:
                trainingFileX.write(",")
        trainingFileX.write("\n")

        # Write point_diff into trainingFileY as correct answer
        # trainingFileY.write(row[2] + "\n")
        # TODO: actually use point differential somehow. For now, just doing winner and loser
        if row[2][0] == "-":
            trainingFileY.write("-1\n")
        else:
            trainingFileY.write("1\n")

# March Madness testing data
pathlib.Path("MarchMadnessData/").mkdir(parents=True, exist_ok=True)
testFile = open("MarchMadnessData/2024.csv", "w")
statsToWrite = [
    # East
    teamStats["Connecticut"] + teamStats["Stetson"],
    teamStats["Fla_Atlantic"] + teamStats["Northwestern"],
    teamStats["San_Diego_St"] + teamStats["UAB"],
    teamStats["Auburn"] + teamStats["Yale"],
    teamStats["BYU"] + teamStats["Duquesne"],
    teamStats["Illinois"] + teamStats["Morehead_St"],
    teamStats["Wash_State"] + teamStats["Drake"],
    teamStats["Iowa_St"] + teamStats["S_Dakota_St"],

    # West
    teamStats["N_Carolina"] + teamStats["Wagner"],
    teamStats["Miss_State"] + teamStats["Michigan_St"],
    teamStats["St_Marys"] + teamStats["Grd_Canyon"],
    teamStats["Alabama"] + teamStats["Col_Charlestn"],
    teamStats["Clemson"] + teamStats["New_Mexico"],
    teamStats["Baylor"] + teamStats["Colgate"],
    teamStats["Dayton"] + teamStats["Nevada"],
    teamStats["Arizona"] + teamStats["Lg_Beach_St"],

    # South
    teamStats["Houston"] + teamStats["Longwood"],
    teamStats["Nebraska"] + teamStats["Texas_A&M"],
    teamStats["Wisconsin"] + teamStats["James_Mad"],
    teamStats["Duke"] + teamStats["Vermont"],
    teamStats["Texas_Tech"] + teamStats["NC_State"],
    teamStats["Kentucky"] + teamStats["Oakland"],
    teamStats["Florida"] + teamStats["Colorado"],
    teamStats["Marquette"] + teamStats["W_Kentucky"],

    # Midwest
    teamStats["Purdue"] + teamStats["Grambling_St"],
    teamStats["Utah_St"] + teamStats["TX_Christian"],
    teamStats["Gonzaga"] + teamStats["McNeese_St"],
    teamStats["Kansas"] + teamStats["Samford"],
    teamStats["S_Carolina"] + teamStats["Oregon"],
    teamStats["Creighton"] + teamStats["Akron"],
    teamStats["Texas"] + teamStats["Colorado_St"],
    teamStats["Tennessee"] + teamStats["St_Peters"],
]
for row in statsToWrite:
    for i in range(0, len(row)):
        testFile.write(row[i])
        if i != len(row) - 1:
            testFile.write(",")
    testFile.write("\n")