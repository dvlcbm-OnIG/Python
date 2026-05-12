

def introduceOne():
    name = input("Enter you name: ")
    age = int(input("Enter your age: "))

    print(f"Name: {name}")
    print(f"Age: {age}")

    age_next_yr = age + 1

    print(f"{name}, your age on your next birthday will be {age_next_yr}")

def introduceTwo():

    number = int(input("guess the number from 1-10: "))    
    secretNum = 8

    if(number == secretNum):
        result = f"{number} is correct! You got the right number! "

    elif(number > secretNum):
         result = f"{number} is a bit higher! You got the wrong number! "

    else:
        result = f"{number} is a bit lower! You got the wrong number! "
    print(result)    



introduceTwo()