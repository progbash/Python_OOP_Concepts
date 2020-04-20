from rent_a_car import BikeRent, CarRent, Customer

bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

main_menu = True
while True:
    
    if main_menu:
        print('''
              ***** Rent A Car Guneshli *****
              A. Bike Menu
              B. Car Menu
              Q. Quit
              ''')
        
        main_menu = False
        
        choice = input("Choice : ")
        
    if choice == "A" or choice == "a":
        print('''
        ***** Bike Menu *****
        1. Show all bikes
        2. Request bike on hourly
        3. Request bike on daily
        4. Return a bike
        5. Back to main menu
        6. Exit
        ''')
        choice = input("Choice : ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("Choice is not correct !")
            continue
        
        if choice == 1:
            bike.displayStock()
            choice = "A"
            main_menu = True
        elif choice == 2:
            customer.rentalBasis_b = 1
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            main_menu = True            
        elif choice == 3:
            customer.rentalBasis_b = 2
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            main_menu = True           
            print("------------------")
        elif choice == 4:
            bike.returnVehicle(customer.returnVehicle("bike"), "bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0, 0, 0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("What the choice is this, maaan ?!")
            main_menu = True
            
    elif choice == "B" or choice == "b":
        print('''
        ***** Car Menu *****
        1. Show all cars
        2. Request car on hourly
        3. Request car on daily
        4. Return a car
        5. Back to main menu
        6. Exit
        ''')
        choice = input("Choice : ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("Choice is not correct !")
            continue
        
        if choice == 1:
            car.displayStock()
            choice = "B"
            main_menu = True
        elif choice == 2:
            customer.rentalBasis_c = 1
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car"))
            main_menu = True            
        elif choice == 3:
            customer.rentalBasis_c = 2
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
            main_menu = True           
            print("------------------")
        elif choice == 4:
            car.returnVehicle(customer.returnVehicle("car"), "car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0, 0, 0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("What the choice is this, maaan ?!")
            main_menu = True
            
    elif choice == "Q" or choice == "q":
        break
    
    else:
        print("Invalid input !")
        main_menu = True
        
print("Thank you for using my fucked up shop.")