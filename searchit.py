import pandas as pd
from rapidfuzz import fuzz,process

folder = pd.read_csv(r"D:\python\fifa_players.csv")

class Search():
    def __init__(self):
        self.player= input('Enter Name of The Player: ').capitalize()
        self.allplayer = folder['name'].dropna().tolist()
        self.bestmatch = process.extract(self.player,self.allplayer,scorer= fuzz.WRatio,limit= 5)
        self.match_indices = [match[2] for match in self.bestmatch if match[1] >= 60]
        if self.match_indices:
            self.matched_p = folder.iloc[self.match_indices][['name','positions','value_euro','overall_rating','potential','wage_euro']]
            print(self.matched_p)
        else:
            print('No MATCH FOUND!!')
            print('RETURNING TO MAIN MENU')

# Search()