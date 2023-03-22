
#Partner


#Function to display the menu
def display_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

#function to encode password by adding 3 to each integer in the password string
def encoder(password):
    encoded_password = ''
    for i in password:
        i = int(i)
        i += 3
        encoded_password += str(i)
    return encoded_password

def decoder(password):
    encoded_password = ''
    for i in password:
        i = int(i)
        i -= 3
        encoded_password += str(i)
    return encoded_password

#Main function that initializes a loop, displays menu, then prompts user to insert password from list of options, options to decode also
if __name__ == '__main__':
    decoder = True
    while decoder:
        display_menu()
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoded = encoder(password)
        if option == 2:
            print(f'The encoded password is {encoded}, and the original password is {password}.')
        if option == 3:
            decoder = False