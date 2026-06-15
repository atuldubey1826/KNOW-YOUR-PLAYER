import pandas as pd
import numpy as np
import matplotlib as plt
from rapidfuzz import fuzz,process

folder = pd.read_csv(r"D:\python\fifa_players.csv")

class Potential():
    def __init__(self):
        print('''
        1 FOR HIGHEST POTENTIAL PLAYER
        2 FOR TOP 10 HIGHEST POTENTIAL HAVING PLAYER
        3 FOR MEDIAN POTENTIAL
        4 FOR HIGHEST POTENTIAL FOR (selected) Nation
        X To Quit\n
''')
        self.choice = input('Enter Your Choice: ')
        if self.choice == '1':
            self.hpotential = folder['potential'].max()
            self.hpotentialname = folder[folder['potential'] == self.hpotential]
            print(self.hpotentialname[['name','potential']])
        elif self.choice == '2':
            self.top10pot = folder[['name','potential']].nlargest(10,'potential')
            self.top10pot_names = self.top10pot.to_numpy()
            print(self.top10pot_names)
        elif self.choice == '3':
            self.medianpotential = folder['potential'].median()
            print(f'The Average Youth Potential is {int(self.medianpotential)}')
        elif self.choice == '4':
            self.nation = input('Enter name of the Nation: ').capitalize()
            self.allnation = folder['national_team'].dropna().unique().tolist()
            self.best_matches = process.extractOne(self.nation,self.allnation,scorer= fuzz.WRatio)
            if self.best_matches and self.best_matches[1] >= 60:
                self.matchednation = self.best_matches[0]
                self.country = folder[folder['national_team'] == self.matchednation]
                self.hpnp = self.country[['name','national_team','potential','positions']].nlargest(11,'potential')
                print(self.hpnp)
            else:
                print("Nation not found or match score too low.")
        elif self.choice.lower() == 'x':
            print('Returning To Main Menu')
        else:
            print('Invalid Choice,RETURNING TO MAIN MENU')

# Potential()