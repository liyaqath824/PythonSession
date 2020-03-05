print("Hello World!")

userInput = input("Please enter your name: ")
print("Hello ", userInput)


try:
    userAge = int(input("Please enter your age: "))
    print("You are ", userAge, " years Old")
except Exception:
    print("It seems, the given age value isn't in a right format")
    
