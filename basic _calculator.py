# calculator

def calculatar():
    while True:
        try:  
            menu = int(input("Hello I am a Calculator !!\nChoose the Mathmatical operation you want to perform: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. To exit \nEnter your choice: "))
            if menu == 1:
                num1 = float(input("Enter number : "))
                num2 = float(input("Enter number : "))
                sum1 = num1 + num2
                print("Sum: ", sum1)
                while True:
                    c = input("If you want to add more number type 'y' else 'n' : ").lower()
                    if c == 'y':
                        num1 = float(input("Enter number : "))
                        sum1 = sum1+num1
                        print("Recent Sum: ",sum1)
                    elif c == 'n':
                        print("Addition is completed\nUpdated Sum: ",sum1)
                        break
                    else:
                        print("Invalid input")
            elif menu == 2:
                num1 = float(input("Enter number : "))
                num2 = float(input("Enter number : "))
                dif1 = num1 - num2
                print("difference: ", dif1)
                while True:
                    c = input("If you want to subtract more number type 'y' else 'n' : ").lower()
                    if c == 'y':
                        num1 = float(input("Enter number : "))
                        dif1 = dif1-num1
                        print("Recent difference: ",dif1)
                    elif c == 'n':
                        print("Subtraction is completed\nUpdated difference: ",dif1)
                        break
                    else:
                        print("Invalid input")
            elif menu == 3:
                num1 = float(input("Enter number : "))
                num2 = float(input("Enter number : "))
                mul1 = num1 * num2
                print("Product: ", mul1)
                while True:
                    c = input("If you want to Multiply more number type 'y' else 'n' : ").lower()
                    if c == 'y':
                        num1 = float(input("Enter number : "))
                        mul1 = mul1*num1
                        print("Recent Product: ",mul1)
                    elif c == 'n':
                        print("Multiplication is completed\nUpdated Product: ",mul1)
                        break
                    else:
                        print("Invalid input")
            elif menu == 4:
                num1 = float(input("Enter number : "))
                num2 = float(input("Enter number : "))
                quo1 = num1 / num2
                if num2 == 0:
                    print("Can not divide by zero!!")
                    continue
                print("Product: ", quo1)
                while True:
                    c = input("If you want to Multiply more number type 'y' else 'n' : ").lower()
                    if c == 'y':
                        num1 = float(input("Enter number : "))
                        if num2 == 0:
                            print("Can not divide by zero!!")
                            continue
                        quo1 = quo1/num1
                        print("Recent Product: ",quo1)
                    elif c == 'n':
                        print("Multiplication is completed\nUpdated Product: ",quo1)
                        break
                    else:
                        print("Invalid input")
            elif menu == 5:
                print("Thank You for Using the Calculator !")
                break
            else:
                print("Invalid Input")
        except ZeroDivisionError:
            print("Can not divide by Zero!")
        except ValueError:
             print("Invalid Value!")


calculatar()
