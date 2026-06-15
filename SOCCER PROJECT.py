import sys
import valuation
import potential
import position
import searchit


while True:
    print('KNOW YOUR PLAYER'.center(50,'~'))
    print('''
1 - Highest Valued Players
2 - Search Through Potential
3 - Search Through Positions
4 - Search Through Names
0 - Close       \n\n   
          ''')
    
    choice = input('Enter Your Choice: ')
    if choice == '1':
       valuation.Marketvalue() 
    elif choice == '2':
        potential.Potential()
    elif choice == '3':
        position.Position()
    elif choice == '4':
        searchit.Search()
    elif choice == '0':
        print('Have A Nice Day')
        sys.exit()
    else:
        print('Enter valid Choice//')
        continue