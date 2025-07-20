user_req = int(input("Please enter the number of your requests."))
i = 0

while i != user_req :

    user_input = input("Please enter the desired mathematical operation.(+, -, *, /, **)")
    first_user_input = int(input("Please enter the first number."))
    second_user_input = int(input("Please enter the second number."))
 

    if user_input == '+' :
        print(first_user_input + second_user_input)
    elif user_input == '/' and first_user_input or second_user_input == 0 :
        print("Please enter a number other than zero.")
        i - 1
    elif user_input == '-' :
        print(first_user_input - second_user_input)
    elif user_input == '*' :
        print(first_user_input * second_user_input)
    elif user_input == '/' :
        print(first_user_input / second_user_input)
    elif user_input == '**' : 
        print(first_user_input ** second_user_input)
    else :
        print("Please enter a defined operator.")
    i+=1