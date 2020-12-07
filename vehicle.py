from tire_set import TireSet
from engine import Engine


class Vehicle:
    # Here we setting the require attributes needed to be given when instantiating a vehicle object. 3 attributes are require and the last 3 are option, but have a default setting.
    def __init__(self, brand, make, model):
        self.brand = brand
        self.make = make
        self.model = model
        self.engine = Engine(6, 280)
        self.tires = TireSet('Summer', 215, 65, 110)
        self.gas_tank = 100

    # This method takes in miles as a parameter, does some math and figures out how much gas to use and how much tread to take off the tires. If the tire is popped or you have less than 0% gas then you cannot drive.
    def drive_vehicle(self, miles):
        self.gas_tank -= miles / 30
        if self.gas_tank > 0 and self.tires.is_flat is not True:
            wear_amount = miles * 0.015
            print(
                f"You have driven {miles} miles and used {miles / 30}% of your gas. You have {self.gas_tank}% left.")
            self.tires.wear_tread(wear_amount)
        else:
            print("You must fix your car or fill up with gas before driving that far!")

    # This method changed the tires on your car using the same parameters that are required to make a new tireset. Resets to default settings so the tires aren't popped and the tread is 100%
    def change_tires(self, new_type, new_width, new_ratio, new_speed_rating):
        self.tires = TireSet(new_type, new_width, new_ratio, new_speed_rating)
        print(f"You now have {new_type} tires on your vehicle.")

    # This method changes the engine in your car using the same parameters that are require to create an engine object. Again, all settings are restored and if you want to change any of the values you will have to do that through the engine object.
    def change_engine(self, cylinders, horsepower):
        self.engine = Engine(cylinders, horsepower)
        print(
            f"You now have a {cylinders} cylinder engine with {horsepower} horsepower in your car.")

    # This method fills your car up with gas. That is all.
    def fill_gas(self):
        self.gas_tank = 100
        print("You have filled up your gas tank")
