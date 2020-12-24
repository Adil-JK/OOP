# Inheritance is used when we are working on a class which has not only new instance variables but also contain those which are alreaady
# defined in the previous class. So we inherit those instance variables from the previous class and only define those instances which are new.
# This comply with the DRY (Don't Repeat Yourself) principle of coding

class Phone: # Base class or Parent class
    def __init__(self, Brand, Model, Price):
        self.Brand = Brand
        self.Model = Model
        self.Price = max(Price, 0)

    def make_a_call(self, phone_number):
        print(f"Calling {phone_number} ")

    def full_name(self):
        return f"{self.Brand} {self.Model}"

class SmartPhone(Phone): # Derived class or Child class
    def __init__(self, Brand, Model, Price, RAM, Internal_memory, Rear_camera):
        # Phone.__init__(self, Brand, Model, Price) ----------> 1st way (Uncommon way)
        super().__init__(Brand, Model, Price)       # ----------> 2nd way (Common way)   
        # Remember! After using super, we not only inherit the instances of class "Phone" but also its methods that are make_a_call and
        # full_name, thats why we don't need to mention it again in the derived class
        self.RAM = RAM
        self.Internal_memory = Internal_memory
        self.Rear_camera = Rear_camera

phone = Phone("Nokia", "1100", 2000)
smartphone = SmartPhone("Samsung", "Galaxy S8", 60000, "4 GB", "64 GB", "12 MP")
print(phone.full_name())
print(smartphone.full_name() + f" Price: {smartphone.Price}" + f" RAM: {smartphone.RAM}")