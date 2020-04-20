import datetime 

# parent class

class VehicleRent:
    
    def __init__(self, stock):
        self.stock = stock
        self.now = 0
    
    def displayStock(self):
        print(f'{self.stock} vehicle available to rent.')
        return self.stock
    
    def rentHourly(self, n):
        if n < 0:
            print("Number should be positive !")
            return None
        elif n > self.stock:
            print(f'Sorry ! We have only {self.stock} cars in stock.')
            return None
        else: 
            self.now = datetime.datetime.now()
            print(f'Rented {n} car(s) at {self.now.hour}')
            self.stock = self.stock - n
            return self.now
            
    def rentDaily(self, n):
        if n < 0:
            print("Number should be positive !")
            return None
        elif n > self.stock:
            print(f'Sorry ! We have only {self.stock} cars in stock.')
            return None
        else: 
            self.now = datetime.datetime.now()
            print(f'Rented {n} car(s) at {self.now.hour}')
            self.stock = self.stock - n
            return self.now
        
    def returnVehicle(self, request, brand):
        
        car_h_price = 10
        car_d_price = car_h_price * 24
        bike_h_price = 2
        bike_d_price = bike_h_price * 24
        
        rentalTime, rentalBasis, numberOfVehicle = request
        bill = 0
        
        if brand == "car":
            if rentalTime and rentalBasis and numberOfVehicle:
                self.stock += numberOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                if rentalBasis  == 1: # hourly
                    bill = rentalPeriod.seconds/3600*car_h_price*numberOfVehicle
                elif rentalBasis  == 1: # daily
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numberOfVehicle
                if (numberOfVehicle > 2):
                    print("You have extra 20% discount")
                    bill *= 0.8
                print(f'Thank you for returning your car(s)')
                print(f'Price: ${bill}')
                return bill
            
        elif brand == "bike":
            if rentalTime and rentalBasis and numberOfVehicle:
                self.stock += numberOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                if rentalBasis  == 1: # hourly
                    bill = rentalPeriod.seconds/3600*bike_h_price*numberOfVehicle
                elif rentalBasis  == 1: # daily
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numberOfVehicle
                if (numberOfVehicle > 4):
                    print("You have extra 20% discount")
                    bill *= 0.8
                print(f'Thank you for returning your bike(s)')
                print(f'Price: ${bill}')
                return bill
        else:
            print("You didn't rent a vehicle.")
            return None
    
class CarRent(VehicleRent):
    
    global discount_rate
    discount_rate = 15
    
    def __init__(self, stock):
        super().__init__(stock)
    
    def discount(self, b):
        bill = b - (b * discount_rate)/100
        return bill  
    
class BikeRent(VehicleRent):
    
    def __init__(self, stock):
        super().__init__(stock)
    
class Customer:
    
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0
        
        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0
    
    def requestVehicle(self, brand):
        if brand == "bike":
            bikes = input("How many bike(s) would you like to rent ?")
            
            try:
                bikes = int(bikes)
            except ValueError:
                print("Number should be number ))")
                return -1
            if bikes < 1:
                print("Number of Bikes should be greated than 0 !")
                return -1
            else: 
                self.bikes = bikes
            return self.bikes
        
        
        if brand == "car":
            if brand == "car":
                cars = input("How many car(s) would you like to rent ?")
            
                try:
                    cars = int(cars)
                except ValueError:
                    print("Number should be number ))")
                    return -1
                if cars < 1:
                    print("Number of Bikes should be greated than 0 !")
                    return -1
                else: 
                    self.cars = cars
                return self.cars
            
        else:
            print("Some error happened.")
    
    def returnVehicle(self, brand):
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0, 0, 0
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0, 0, 0
        else:
            print("Return vehicle Error")