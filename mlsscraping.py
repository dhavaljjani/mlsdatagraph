import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

listURL = "https://www.mlssoccer.com/stats/alltime";
response = requests.get(listURL)
soup = BeautifulSoup(response.text, "html.parser")
element = soup.find(class_="responsive no-more-tables season_stats")
elementRows = element.find_all("tr")
xLabels = []
yLabels = []
goalsList = []
assistsList = []
for tr in elementRows:
    player = []
    td = tr.find_all("td")
    index = 0
    for elem in td:
        data = elem.get_text()
        player.append(data)
    if len(player) != 0:
        name = player[0]
        xLabels.append(name)
        pos = player[1]
        gp = player[2]
        gs = player[3]
        mins = player[4]
        goals = player[5]
        assists = player[6]
        goalsList.append(int(goals))
        assistsList.append(int(assists))
        yLabels.append((int(goals) + int(assists)) / int(gp))
        shots = player[7]
        sog = player[8]
        print(name, ": shots to goals -->", int(shots) / int(goals))
plt.figure(1)

contributions = []
for i in range(len(goalsList)):
    contributions.append(goalsList[i] + assistsList[i])
plt.scatter(goalsList, assistsList, s=contributions, c=contributions)
for i, text in enumerate(xLabels):
    print(text + " (" + str(goalsList[i]) + "G, " + str(assistsList[i]) + "A)")
    plt.text(goalsList[i]+1, assistsList[i]+1, text + " (" + str(goalsList[i]) + "G, " + str(assistsList[i]) + "A)", fontsize=7)
plt.ylabel("Assists")
plt.xlabel("Goals")
plt.title("Top MLS Contributors")

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.show()

