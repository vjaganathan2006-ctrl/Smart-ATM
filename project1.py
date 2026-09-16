balance = 10000#creating balance for variable to store the amount
correct_pin = 1234#creating correct_pin variable for store the pin
print("==========SMART ATM==========")#displaying the project title
pin = int(input("enter your PIN:"))#asking the user to enter pin
if pin == correct_pin:#checking entered PIN is correct
    print("\nLogin successful!")#display login successful message
else:
    print("\nincorrect pin")#displaying incorrect message

print("\n1.Check Balance\n2.deposit Money\n3.Withdraw Money\n4.Exit")#displaying all ATM menus

choice = int(input("\nenter your choice:"))#asking the user to enter your choice
if choice == 1:#checking you correct entered choice1
    print("current balance $:",balance)#displaying current balance
    print("\nThank you for using Smart ATM")#thanking for user
    
elif choice == 2:#checking you correct entered choice2
    try:
        amount = int(input("enter deposit amount $:"))#asking the user to enter deposit amount
        if amount>0:# if amount was greathan zero then run the condition
            balance += amount#amount added to the balance
            print("deposit successful")#displaying deposit successful
            print("updated your bank balance",balance)#displaying atfer deposit amount updated the balance
            print("\nThank you for using Smart ATM")#thanking for user
    
        else:
            print("invalid amount")#displaying invalid amount
    except ValueError:
            print("please enter a valid number.")#displaying user to enter valid number
elif choice == 3:#checking you correct entered choice3
    try:
        amount = int(input("enter withdrawal amount:"))#asking the user to enter withdrawl amount
        if amount>0:#if amount was greathan zero then run the condition
            balance -= amount#amount subtrations to the balance
            print("withdrawal successful!")#displaying withdrawal successful
            print("remaining balance amount $:",balance)#displaying atfer withdrawl amount updated the balance
            print("\nThank you for using Smart ATM")#thanking for user
    
        else:
            print("invaild amount")#displaying invalid amount
    except ValueError:
            print("please enter a valid number.")#displaying user to enter valid number
elif choice == 4:#checking you correct entered choice4
    print("Thank you for using Smart ATM")#thanking for user
else:
    print("invaild choice please select 1 to 4")#displaying user to invaild choice please select 1 to 4 number





















































    
