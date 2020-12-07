from vehicle import Vehicle

# This is an example of object inheritance. The Truck class inherits from the Vehicle class so it has all of the same attributes that the Vehicle class does. The Truck class, however, has a new attribute called bed_type.


class Truck(Vehicle):
    # The Truck class uses all of the same parameters but one, and here we create a new parameter called bed_type
    def __init__(self, brand, make, year, bed_type):
        super().__init__(brand, make, year)

        self.bed_type = bed_type

    # This method overrides the original drive_vehicle method by using more gas per mile and putting more wear on the tire because it is a heavier vehicle.
    def drive_vehicle(self, miles):
        self.gas_tank -= miles / 18
        if self.gas_tank > 0 and self.tires.is_flat is not True:
            wear_amount = miles * 0.020
            print(
                f"You have driven {miles} miles and used {miles / 18}% of your gas. You have {self.gas_tank}% left.")
            self.tires.wear_tread(wear_amount)
        else:
            print("You must fix your truck or fill up with gas before that far!")

    # This method simply shows you that you filled up the bed of your truck.
    def load_bed(self):
        print(f"You loaded your {self.bed_type} up!")
