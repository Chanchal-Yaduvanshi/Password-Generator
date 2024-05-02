import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would u like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

level = input("Enter the level of your password: easy or hard\n")
if(level=="easy") :
    password = ""
    for char in range(1,nr_letters+1) :
        password = password + random.choice(letters);           

    for num in range(1,nr_numbers+1) :
        password=password+random.choice(numbers);

    for sym in range(1,nr_symbols+1) :
        password = password + random.choice(symbols);
    print(f"Your password is : {password}")

elif (level == "hard") :
    password_list=[]
    for char in range(1,nr_letters+1) :
        password_list.append(random.choice(letters))                  
    
    for num in range(1,nr_numbers+1) :
        password_list.append(random.choice(numbers))

    for sym in range(1,nr_symbols+1) :
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    
    #Converting list into string
    password2=""
    for n in password_list :
        password2 = password2 + n
    print(f"Your password is : {password2}")

else :
    print("You've entered wrong input.")

