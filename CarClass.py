class CarClass:
    make = None                         # initializing class attributes
    model = None
    color = None
    year = 0
    mileage = 0
    inventory = []

    def __init__(self, *args):          # default and parameterized constructors
        if len(args) < 2:               # if length of args is 1 or less, use default
            # default constructor
            self.make = "default"
            self.model = "default"
            self.color = "default"
            self.year = 0
            self.mileage = 0

        elif len(args) > 1:             # if length of args is 2 or more, use index of each arg
            self.make = args[0]
            self.model = args[1]
            self.color = args[2]
            self.year = args[3]
            self.mileage = args[4]

    def removeVehicle(self, make, model, color, year, mileage):  # remove vehicle method searches inventory for match
        i = 0
        while i < len(self.inventory):
            if (self.inventory[i].make == make and self.inventory[i].model == model and self.inventory[i].color
                    == color and self.inventory[i].year == year and self.inventory[i].mileage == mileage):
                del self.inventory[i]
                return "The " + str(year) + " " + model + " was removed successfully"
            i += 1

    def addVehicle(self, make, model, color, year, mileage):    # add vehicle method uses the parameterized constructor
        # add vehicle method
        car = CarClass(make, model, color, year, mileage)
        self.inventory.append(car)
        return "The " + str(year) + " " + model + " was added successfully\n"

    def updateVehicle(self, make, model, color, year, mileage):
        self.removeVehicle(make, model, color, year, mileage)  # removes original, then adds a new vehicle
        print("Now enter the updated values the same way,", end="")
        make, model, color, year, mileage = input(" with each value separated only by a comma and space: ").split(", ")
        self.addVehicle(make, model, color, year, mileage)
        return "The " + str(year) + " " + model + " was updated successfully\n"

    def saveToFile(self):
        with open('DealershipInventory.txt', 'w+') as inventory_file:  # saves to name file, creates if not exist
            inventory_file.write(self.printInfo())
        return 'Success! Saved to \'DealershipInventory.txt\''

    def printInfo(self):  # print info iterates through inventory and each attribute into a clean output
        output = ""
        i = 0
        while i < len(self.inventory):
            output += ("Car #" + str((i + 1)) + " - Make: " + self.inventory[i].make + ", Model: " + self.inventory[
                i].model + ", Color: " + self.inventory[i].color + ", Year: " + str(
                self.inventory[i].year) + ", Mileage: " + str(self.inventory[i].mileage) + " \n")
            i += 1
        return output


if __name__ == "__main__":
    Cars = CarClass()                                                       # creates a CarClass to use
    print("Welcome to the Dealership Inventory Program...\n")
    print("There are currently no vehicles in the system...\n")

    temp = 0
    while temp != 1:
        print('To add a new vehicle, enter 1\n'
              'To remove a vehicle, enter 2\n'
              'To update a vehicle, enter 3\n'
              'To save the data to DealershipInventory.txt, enter 4\n'
              'To print the current inventory, enter 5\n'
              'To quit, enter 6\n')
        check = int(input())

        if check == 1:
            tempMake, tempModel, tempColor, tempYear, tempMileage = \
                (input("Enter the vehicle you want to add exactly as such \n"
                       "\'Make, Model, Color, Year, Mileage\', with each value separated only by a comma and space: ").
                 split(", "))
            print(Cars.addVehicle(tempMake, tempModel, tempColor, tempYear, tempMileage))
            temp = 0
        elif check == 2:
            tempMake, tempModel, tempColor, tempYear, tempMileage = \
                (input("Enter the vehicle you want to remove exactly as such \n"
                       "\'Make, Model, Color, Year, Mileage\' with each value separated only by a comma and space: ").
                    split(", "))
            print(Cars.removeVehicle(tempMake, tempModel, tempColor, tempYear, tempMileage))
            temp = 0
        elif check == 3:
            tempMake, tempModel, tempColor, tempYear, tempMileage = \
                (input("Enter the info of the vehicle you want to update exactly as such\n"
                       "\'Make, Model, Color, Year, Mileage\', with each value separated only by a " 
                       "comma and space: ").split(", "))
            print(Cars.updateVehicle(tempMake, tempModel, tempColor, tempYear, tempMileage))
            temp = 0
        elif check == 4:                                    # saves to DealershipInventory.txt with saveToFile function
            print(Cars.saveToFile())
            temp = 0
        elif check == 5:
            print(Cars.printInfo())                         # prints inventory
            temp = 0
        elif check == 6:                                  # if 6, terminates
            print("Goodbye")
            temp = 1
