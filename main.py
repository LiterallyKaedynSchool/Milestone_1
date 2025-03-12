# Variable Setting
INT_LIMIT = 101
STR_SPEEDQUESTION = "How fast were you going (KM/H)? "
STR_NAMEQUESTION = "What is your name? "
int_userSpeed = 0
str_userName = ''
INT_FINE = 250
STR_GOOD = "Alright {}. You are good to go!"
STR_BAD = "Alright {}. You are being fined ${} for speeding."

# Main
print("Hello there, you have been pulled over for speeding.")
str_userName = input(STR_NAMEQUESTION)
str_userSpeed = int(input(STR_SPEEDQUESTION))

if str_userSpeed < INT_LIMIT:
    print(STR_GOOD.format(str_userName))
else:
    print(STR_BAD.format(str_userName, INT_FINE))
