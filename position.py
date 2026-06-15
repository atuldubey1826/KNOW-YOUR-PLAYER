import pandas as pd
import numpy as np
import matplotlib as plt

folder = pd.read_csv(r"D:\python\fifa_players.csv")

class Position():
    def __init__(self):
        self.choice = input('Enter a valid Position: (ALL CAPS): ')
        self.pos()

    def pos(self):
        print(f'''
1 For Top Rated Players at {self.choice}
2 For Highest Value Player at {self.choice}
(Other Keys) to Return
''')
        self.choice2 = input('Choose Accordingly: ')
        if self.choice2 == '1':
            self.position2 = folder[folder['positions'].str.contains(self.choice, na=False)]
            self.top5positionplayer = self.position2[['name','positions','overall_rating']].nlargest(5,'overall_rating')
            print(self.top5positionplayer.to_numpy())
        elif self.choice2 == '2':
            self.highvalue = folder[folder['positions'].str.contains(self.choice, na=False)]
            self.highvalueplayer = self.highvalue[['name','positions','value_euro']].nlargest(5,'value_euro')
            print(self.highvalueplayer)
        else:
            print('RETURNING TO MAIN MENU')
        

# Position()

