from main import *
from datetime import datetime, date


kidding = True
while kidding:
    user_choice = 0
    try:
        user_choice = user_interface()
    except:
        print("\n")
        print("Invalid input!!, Please enter a valid number!!!")
        #Takes user input
    dictionary = cos_dic()

    # store info of rented and returned costumes
    rented_costumes = []
    returned_costumes = []
    rent_brand = []
    return_brand = []

    if user_choice == 1:                                             
        print("\n")
        print("Renting a costume") 
        show_cos()                  
        print("----------------------------------------------------------------------------------")
        print("\n")
    

        costume_id = info_cos(dictionary)



        # to store integer value in varialbe quantity_rented from avai_quantity.
        
        quantity_rented = avai_quantity(int(dictionary[costume_id][3]))


        rented_costumes.append(dictionary[costume_id][0])
        rent_brand.append(dictionary[costume_id][1])
        print("\n")
        
        name = input("Enter your name: ")
        number = 0
        while True:
            try:
                number = int(input("Enter your number:"))
                break
            except:
                print("Invalid Input!!")
                # continue

        # updating dictionary by reducting rented costumes
        dictionary[costume_id][3] = int(dictionary[costume_id][3])- quantity_rented

        print("\n")

        # updating text file 
        edit_docu(dictionary)


        # Printing the total price
        totalPrice = total_price(quantity_rented,costume_id,dictionary)

        print("Do you want to rent another costume ??")
        re_rent = input("Please enter 'y' for yes and 'n' for no:").lower()

        while re_rent == "y":
           list1 =  rent_again()
           rented_costumes.append(dictionary[list1[1]][0])
           rent_brand.append(dictionary[list1[1]][1])

           totalPrice = totalPrice + total_price(list1[2],list1[1],dictionary)

           print("\n")
           print("Do you want to rent another costume ??")
           re_rent = input("Please enter 'y' for yes and 'n' for no:").lower()


        print("\n")
        print("==================================================")
        print("\t\t\t\tBill Details")
        print("==================================================")
        print("Name of the Customer: ",name )
        print("Date and Time of Borrow: ", datetime.now())
        print("Contact Number of the Customer: ",number )
        print("--------------------------------------------------")

        for i in range(len(rented_costumes)):
            print("Costume rented: ",rented_costumes[i] )
            print("Brands rented: ", rent_brand[i])
            print("---------------------------------------------------")
        print("Total price of all the rented Costumes is: $", totalPrice)
        print(f"Thank you for choosing our store {name}. Please receive your bill.")

        #printing the bill 

        file1 = open(f"{name}.txt","w")
        file1.write("\t\tBill Details\t\t\n\n")
        file1.write(f"Name of the Customer: {name}\n")
        file1.write(f"Date and Time of Borrow: {date.today()}\n")
        file1.write(f"Contact Number of the Customer: {number}\n")
        file1.write("---------------------------------------------------\n")
        for i in range(len(rented_costumes)):
            file1.write(f"Costumes rented are: {rented_costumes[i]}\n")
            file1.write(f"Brands rented are: {rent_brand[i]}\n")
            file1.write("---------------------------------------------------\n")


        file1.write(f"Total price of all the rented costumes is ${totalPrice}\n")
        file1.write(f"Thank you for choosing our store {name}. Please receive your bill.")

        file1.close()


    elif user_choice == 2:

        print("\n")
        print("Return a costume")
        show_cos()
        print("------------------------------------------------------------")
        c_id = return_cos()
        price = 0
        av_quantity = 0
        name = ""
        number1 = 0
        while True:
            try:

                av_quantity = int(input("Enter the quantity of the costume you want to return:"))
                while av_quantity <= 0:
                    print("Invalid Input!!, Please Enter a valid quantity")
                    av_quantity = int(input("Enter the quantity of the costume you want to return:"))

                returned_costumes.append(dictionary[c_id][0])
                return_brand.append(dictionary[c_id][1])

                dictionary[c_id][3] = int(dictionary[c_id][3]) + av_quantity

                print("\n")
                edit_docu(dictionary)


                name = input("Enter your name: ")
                while True:
                    try:

                        number1 = int(input("Enter your number:"))
                        break
                    except:
                        print("You entered an Invalid Number")
                        continue
                break


            except:
                print("Invalid Input, Please Try again!!")
                continue

        price = 0
        while True:
            try:
                print("\n")
                days_kept = int(input("How many days did you keep the costume for ?"))

                if days_kept <= 5:
                    price = 0

                else:

                    price = (days_kept - 5) * av_quantity * 5
                break
            except Exception as e:
                print("Invalid Input, Please Try again!!")
                continue





        print("\n")
        print("Do you want to return another custome ??")
        re_return = input("Please enter 'y' for yes and 'n' for no:").lower()

        while re_return == "y":


          list2 = costume_return()
          returned_costumes.append(dictionary[list2[0]][0])
          return_brand.append(dictionary[list2[0]][1])

          price = price + list2[1]



          print("Do you want to return another custome too ??")
          re_return = input("Please enter 'y' for yes and 'n' for no:").lower()

        print("\n")
        print("==================================================")
        print("\t\t\t\tBill Details")
        print("==================================================")
        print("Name of the Customer: ",name )
        print("Date and Time of Return: ", datetime.now())
        print("Contact Number of the Customer: ", number1)
        print("--------------------------------------------------")

        for i in range(len(returned_costumes)):

            print("Costume returned: ",returned_costumes[i] )
            print("Brands returned: ", return_brand[i])
            print("---------------------------------------------------")
        print("Total fine of all the returned Costumes is: $", price)
        print(f"Thank you for choosing our store {name}. Please receive your bill.")

        file1 = open(f"{name}.txt", "w")
        file1.write("\t\tBill Details\t\t\n\n")
        file1.write(f"Name of the Customer: {name}\n")
        file1.write(f"Date and Time of Return: {date.today()}\n")
        file1.write(f"Contact Number of the Customer: {number1}\n")

        file1.write("---------------------------------------------------\n")
        for i in range(len(returned_costumes)):
            file1.write(f"Costumes returned are: {returned_costumes[i]}\n")
            file1.write(f"Brands returned are: {return_brand[i]}\n")
            file1.write("---------------------------------------------------\n")

        file1.write(f"Total price of all the rented costumes is ${price}\n")
        file1.write(f"Thank you for choosing our store {name}. Please receive your bill.")

        file1.close()


    elif user_choice == 3:
        print("\n")
        print("Thank you for choosing our shop,\n Hope to see you here again!")
        running = False

    else:
        print("Invalid Input!!,Please try again with valid id")
