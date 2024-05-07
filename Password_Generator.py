import random
import string

def Generate_Password(Min_Len , Num = True, Special_Char = True ):
    Letters = string.ascii_letters
    Digits = string.digits
    Special = string.punctuation

    Charecters = Letters
    if Num:
        Charecters += Digits
    if Special_Char:
        Charecters += Special

    Pwd = " "
    Condition = False
    Has_Num = False
    Has_Special = False

    while not Condition or len(Pwd) < Min_Len:
        New_Char = random.choice(Charecters)
        Pwd += New_Char

        if New_Char in Digits:
            Has_Num = True
        elif New_Char in Special:
            Has_Special = True 

        Condition = True 
        if Num :
            Condition = Has_Num 
        if Special : 
            Condition = Condition and Has_Special

    return Pwd
  
Pwd_Len = int(input("Enetr the Length of Password to be generated "))
Want_Num = input("Do you want Numbers (y/n) ? ").lower() == "y"
Want_Special = input("Do you want Special Characters (y/n) ? ").lower() == "y"
Generate_Password(Pwd_Len , Want_Num , Want_Special)
print(Pwd)