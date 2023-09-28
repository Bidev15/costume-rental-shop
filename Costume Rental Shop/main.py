def user_interface():
    print("\n")
    print("******************Welcome to the HiFy's Costume Rental Shop*********************")
    print("\n")
    print("(1)  Click 1 to rent a Costume")
    print("(2)  Click 2 to return a Costume")
    print("(3)  Click 3 to exit")

    hify = int(input("Select a desirable option:"))

    return hify
#To show available costumes in table 
def show_cos():
    file = open("costume.txt","r")
    count = 1

    print("----------------------------------------------------------------------------------")
    print("Id\t","Name\t\t","Brand\t ","\tPrice\t\t", "Quantity")
    print("----------------------------------------------------------------------------------")
    for line in file:
        print(count,"\t",line.replace(",","\t\t"))
        count+= 1

    file.close()

def cos_dic():
    file = open('costume.txt',"r")
    count = 0
    cosdic = {}
    for line in file:
        count += 1
        a = line.replace("\n","")
        x = a.split(",")
        cosdic[count] = x
    file.close()
    return cosdic

# Renting costume 
def info_cos(dic):
    info_costumeId = 0
    while True:
        try:
            print("\n")
            info_costumeId = int(input("Enter the Id of the costume you want to rent:"))
            while info_costumeId <= 0 or info_costumeId > len(cos_dic()):
                if info_costumeId <= 0 or info_costumeId > len(cos_dic()):
                    print("Invalid Costume Id,Please enter a valid ID:")
                    show_cos()
                    info_costumeId = int(input("Enter the Id of the costume you want to rent:"))

            while dic[info_costumeId][3] == "0":
                print("Sorry,this item is not available\nPlease choose another one")
                show_cos()
                info_costumeId = int(input("Enter the Id of the costume you want to rent:"))

            print("Costume having ID ", info_costumeId, " is available.")

            break

        except Exception as e:
            print(e)
            continue

    return info_costumeId

def return_cos():
    info_costumeId = 0
    while True:
        try:
            info_costumeId = int(input("Enter the Id of the costume you want to return:"))

            while info_costumeId <=0 or info_costumeId > len(cos_dic()):
                print("Invalid CostumeId.Please enter a valid id :")
                show_cos()
                v_costumeId = int(input("Enter the Id of the costume you want to return:"))
            break
        except Exception as e:
            print("The exception is ",e)
            continue
    return info_costumeId

def avai_quantity(available_quantity):

    av_quantity = 0
    while True:
        try:
            print("\n")
            av_quantity = int(input("How many quantity do you want to rent?:"))
            while av_quantity > available_quantity or av_quantity <= 0:
                if av_quantity > available_quantity:
                    print("Please select a smaller value.")
                    av_quantity = int(input("Enter the quantity of the costume you want to rent:"))

                elif av_quantity <= 0:
                    print("Quantity can't be negative or Zero")
                    av_quantity = int(input("Enter the quantity of the costume you want to rent:"))

            print(av_quantity," Costumes have been rented Successfully.")
            break
        except Exception as e:
            print("The exception is ",e)
            continue

    return av_quantity
#value update in dictionary
def edit_docu(c_dictionary):

    file = open("costume.txt","w")
    for i in c_dictionary.values():
        new_line=  str(i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]))

        file.write(new_line)
        file.write("\n")

    file.close()


def total_price(quantity_rented,costume_id,dictionary):

    price = float(dictionary[costume_id][2].replace("$",""))
    total_price = quantity_rented * price
    return total_price

#for renting the costume
def rent_again():
    my_dictionary = cos_dic()

    print("Rent a costume")
    show_cos()
    print("------------------------------------------------------------")
    costume_id = info_cos(my_dictionary)



    quantity_rented = avai_quantity(int(my_dictionary[costume_id][3]))


    my_dictionary[costume_id][3] = int(my_dictionary[costume_id][3]) - quantity_rented
    
    edit_docu(my_dictionary)

    return list, costume_id, quantity_rented

#for returning costume 
def costume_return():  
    show_cos()
    print("------------------------------------------------------------")
    c_id = return_cos()
    a = 0
    dictionary2 = cos_dic()
    while True:
        try:
            av_quantity = int(input("Enter the quantity of the costume you want to return:"))


            dictionary2[c_id][3] = int(dictionary2[c_id][3]) + av_quantity
            
            edit_docu(dictionary2)
            print("\n")
            days_kept = int(input("How many days did you keep the costume for ?"))
            print("\n")

            if days_kept <= 5:
                a = 0

            else:

                a = (days_kept - 5) * av_quantity * 5
            break

        except Exception as e:
            print("The exception is ",e)
            continue

    return c_id,a
