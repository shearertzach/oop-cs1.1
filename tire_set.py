class TireSet:
    # We create a tire with 4 require attributes. When used in the Vehicle class there are default values, but they can be changed with a new instantiation.
    def __init__(self, tire_type, width, ratio, speed_rating):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.speed_rating = speed_rating
        self.tread_percent = 100
        self.is_flat = False

    # If your tire is popped after driving you can simply use this method to fix the tire and be on your way.
    def fix_tire(self):
        self.is_flat = False
        self.tread_percent = 100
        print("Your tire has been fixed.")

    # If your tires seem a bit weird when driving fast, you can use this method to check if they are rated for the speed you are going.
    def check_speed(self, speed):
        if speed > self.speed_rating:
            print("You are going to fast for your wheels!!")
        else:
            print("Go faster!")

    # This method is explicitly called only whenever you drive the vehicle because it would be kinda dumb otherwise.
    def wear_tread(self, amount):
        self.tread_percent -= amount
        print(
            f"You wore {amount}% of your tread. You have {self.tread_percent}% left.")
        if self.tread_percent <= 0:
            self.is_flat = True
            print("Your tire has popped.")
