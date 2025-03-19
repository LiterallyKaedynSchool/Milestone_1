'''

Author: Kaedyn Eastall
Date (Last Edit): 18/03/25
License: JSS GENERAL PUBLIC LICENSE 001 - Version 1 (https://github.com/Jester-Software-Systems/JSS_LICENSE_DIRECTORY/blob/2025-Licenses/MARCH/JSS-GPL1)

'''

# Variable Setting
INT_LIMIT = 56
STR_SPEEDQUESTION = "How fast were you going (KM/H)? "
STR_NAMEQUESTION = "What is your name? (Input \"END\" to end loop) "
STR_MONEYQUESTION = "How much money do you have? $"
int_userSpeed = 0
int_userMoney = 0
str_userName = ""
INT_FINE = 250
STR_GOOD = "Alright {}. You are good to go!"
STR_BAD = "Alright {}. You are being fined ${} for speeding.\nYou now have ${}."
bool_again = True

# Main
while bool_again == True:
    print("Hello there, you have been pulled over for speeding.")
    str_userName = input(STR_NAMEQUESTION)
    int_userMoney = int(input(STR_MONEYQUESTION))
    
    if str_userName == "END":
        bool_again = False
        continue
    else:
        int_userSpeed = int(input(STR_SPEEDQUESTION))
    if int_userSpeed < INT_LIMIT:
        print(STR_GOOD.format(str_userName))
    else:
        int_userMoney = int_userMoney - 250
        print(STR_BAD.format(str_userName, INT_FINE, int_userMoney))
    
print("Bye!")
