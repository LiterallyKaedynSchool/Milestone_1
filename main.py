# Variable Setting
INT_LIMIT = 100
STR_SPEEDQUESTION = "How fast were you going (KM/H)? "
int_userSpeed = 0
INT_FINE = 250
STR_GOOD = "You are good to go!"
STR_BAD = "You are being fined ${} for speeding.".format(INT_FINE)

# Start
print("Hello there, you have been pulled over for speeding.")
str_userSpeed = int(input(STR_SPEEDQUESTION))

if str_userSpeed < INT_LIMIT:
    print(STR_GOOD)
else:
    print(STR_BAD)


# This code is copyrighted by Kaedyn Eastall and may not be copied or distributed without permission.
