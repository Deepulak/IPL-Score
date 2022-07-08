from tkinter import *
import requests
from bs4 import BeautifulSoup

# Create instance for window
root = Tk()

# set title for window
root.title("Indian Premire League")
# set background size
root.geometry("380x200")
root.configure(bg="#00bfff")

# cricbuzz url to get score updates
url = 'https://www.cricbuzz.com/'

def get_score():
    # request data from cricbuzz
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    # name of first team
    team_1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
    # name of the second team
    team_2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
    # Score of first team
    team_1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
    # score of second team
    team_2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()
    # configure the team names to teams label
    teams.config(text=f"{team_1}\t\t{team_2}")
    # configure the team score to teams label
    scores.config(text=f"{team_1_score}\t{team_2_score}")
    # call the get_score() function
    # after every 5000 milliseconds
    # and update scores
    scores.after(5000, get_score)

# label to display IPL 2021 title
title = Label(root, text="IPL 2021", font=("Helvetica 30 bold"))
title.grid(row=0, pady=5)
# label for team names
teams = Label(root, font=("Helvetica 20 bold"))
teams.grid(row=1, padx=5)
# label for team scores
scores = Label(root, font=("Helvetica 20 bold"))
scores.grid(row=2, padx=5)
# call function
get_score()
root.mainloop()
