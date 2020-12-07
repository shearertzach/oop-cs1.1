class Engine():
    # Here we create an engine with two require attributes: cylinders and horsepower.
    def __init__(self, cylinders, horsepower):
        self.cylinders = cylinders
        self.horsepower = horsepower
        self.air_intake_type = 'Naturally Aspirated'
        self.is_tuned = False

    # This method will set your engine to a tuned engine and you will recieve 50 more horsepower.
    def tune_engine(self):
        self.is_tuned = True
        self.horsepower += 50
        print("You tuned your car and gained 50 horsepower!")

    # This method takes in one parameter and changed the air_intake_type to that new parameter. You also gain 200 horsepower.
    def change_intake(self, new_intake):
        self.air_intake_type = new_intake
        self.horsepower += 200
        print(
            f"You changed your car to: '{new_intake}' and gained 200 horsepower")
