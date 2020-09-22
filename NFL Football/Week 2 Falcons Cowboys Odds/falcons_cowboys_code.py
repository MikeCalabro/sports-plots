import pandas as pd
from matplotlib import pyplot as plt

#*#*#*#*#*#*#*##
#**# SET-UP #**#
#*#*#*#*#*#*#*##

# Reads in the csv file I downloaded via nflfastR
data = pd.read_csv('play_by_play_2020.csv', low_memory=False)

# Selects the data needed from the 2020 week 2 Cowboys Falcons game
new_data = (data[["week", "home_team", "away_team", "game_seconds_remaining", "vegas_home_wp"]]
                [data["week"] == 2]
                [data["home_team"] == "DAL"]
                .dropna())

#*#*#*#*#*#*#*##
#*# PLOTTING #*#
#*#*#*#*#*#*#*##

# Creates the plot
fig, ax = plt.subplots()

# Creates vertical grid lines
ax.grid(axis='x', alpha=0.9)

# Creates the red fill below the 50% tick, indicating the Falcons odds to win the game
ax.fill_between(-1*new_data["game_seconds_remaining"],
                new_data["vegas_home_wp"],
                0.5,
                where=(new_data["vegas_home_wp"] < 0.5),
                alpha=0.5,
                color="red")

# Creates the blue fill above the 50% tick, indicating the Cowboys odds to win the game
ax.fill_between(-1*new_data["game_seconds_remaining"],
                new_data["vegas_home_wp"],
                0.5,
                where=(new_data["vegas_home_wp"] > 0.5),
                alpha=0.5,
                color="blue")

# Creates the x tick labels
plt.xticks((-3600, -2700, -1800, -900, 0),
           ("START\nGAME", "END\nQ1", "END\nHALF", "END\nQ3", "END\nGAME"),
           weight="bold")

# Creates the y tick labels
plt.yticks((0, .25, .5, .75, 1),
           ("100%", "75%", "50%", "75%", "100%"),
           weight="bold")

# Colors the y-axis ticks appropriately
colors = ["red", "red", "gray", "blue", "blue"]
for ytick, color in zip(ax.get_yticklabels(), colors):
    ytick.set_color(color)

# Adds the text to the plot
plt.annotate("COWBOYS WIN PROBABILITY", (-2686, .98), color="blue", fontweight="bold")
plt.annotate("FALCONS WIN PROBABILITY", (-2670, .02), color="red", fontweight="bold")

# Creates the title
plt.title("NFL Week 2 Falcons @ Cowboys Vegas Live Odds", weight="bold")

# Shows the plot
plt.show()
