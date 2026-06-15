import pandas as pd
import numpy as np
import matplotlib as plt
from rapidfuzz import fuzz,process

folder = pd.read_csv(r"D:\python\fifa_players.csv")

class Marketvalue:
    def __init__(self):
        print('''
        1 FOR HIGHEST VALUE PLAYER
        2 FOR TOP 10 HIGHEST VALUE PLAYER
        3 FOR MEDIAN VALUE
        4 FOR HIGHEST VALUE FOR (selected) Nation
        (Other Keys) To Quit\n
''')
        self.choice = input("Enter Valid No. To Choose: ")
        if self.choice == '1':
            self.hvalue = folder['value_euro'].max()
            self.nameofhvalue = folder[folder['value_euro'] == self.hvalue]
            print(self.nameofhvalue[['name','value_euro']])
        elif self.choice == '2':
            self.top10value= folder[['name','value_euro']].nlargest(10,'value_euro')
            self.top10value_names = self.top10value.to_numpy()
            print(self.top10value_names)
        elif self.choice == '3':
            self.median = folder['value_euro'].median()
            print(f'The Median Market Value is {self.median}')
        elif self.choice == '4':
            self.nation = input('Enter Name of the Nation: ').capitalize()
            self.all_nation = folder['national_team'].dropna().unique().tolist()
            self.best_matches = process.extractOne(self.nation,self.all_nation,scorer= fuzz.WRatio)
            if self.best_matches and self.best_matches[1] >= 60:
                self.matched_country = self.best_matches[0]
                self.country = folder[folder['national_team'] == self.matched_country]
                self.hvnp = self.country[['name','national_team','value_euro','positions']].nlargest(11,'value_euro')
                print(self.hvnp)
            else:
                print("Nation not found or match score too low.")
        elif self.choice.lower() == 'x':
            print('RETURNING TO MAIN MENU')
        else:
            print('Invalid Choice,RETURNING TO MAIN MENU')
        

# Marketvalue()