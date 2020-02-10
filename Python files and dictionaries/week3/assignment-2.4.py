# Define a function called info with five parameters: name, gender, age, bday_month, and hometown. The function should then return a tuple with all five parameters in that order.
def info(name,gender,age,bday_month,hometown):
    return(name,gender,age,bday_month,hometown)
if __name__=="__main__":
    name=input()
    gender=input()
    age=int(input())
    bday_month=input()
    hometown=input()
    print(info(name,gender,age,bday_month,hometown))
