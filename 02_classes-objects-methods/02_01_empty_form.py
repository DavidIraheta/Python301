# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.
class Blueprint :
    def __init__ (self, name, age, gender, address, phone_number, email, height, weight, medical_history, emergency_contact):
        self.name = name
        self.age = age
        self.gender= gender
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.height = height
        self.weight = weight
        self.medical_history = medical_history
        self.emergency_contact = emergency_contact

    def medical_form (self) :
        return(
        f"Name: {self.name}\n"
        f"Age: {self.age}\n"
        f"gender: {self.gender}\n"
        f"Address: {self.address}\n"
        f"Phone Number: {self.phone_number}\n"
        f"Email: {self.email}\n"
        f"Height: {self.height}\n"
        f"Weight: {self.weight}\n"
        f"Medical History: {self.medical_history}\n"
        f"Emergency Contact: {self.emergency_contact}\n"
        )
patient1 = Blueprint(
    name = "Joe Spaghetti",
    age = "25",
    gender = "M",
    address = "1234 Main St, San Francisco, CA 94102",
    phone_number = "415-555-1234",
    email = "jspaghetti@hotmail.com",
    height = "6'0",
    weight = "180 lbs",
    medical_history = "None",
    emergency_contact = "Jane Spaghetti"
)
patient2 = Blueprint(
    name= "Tina Tortellini",
    age = "30",
    gender= "F",
    address = "5678 Market St, New York, NY 12550",
    phone_number = "212-555-5678",
    email = "ttortellini@aol.com",
    height = "5'5",
    weight = "140 lbs",
    medical_history = "Allergies to peanuts",
    emergency_contact = "Tony Tortellini"
)
patient3 = Blueprint(
    name = "Ravioli Ricci",
    age = "35",
    gender= "M",
    address = "9101 Broadway, Los Angeles, CA 90210",
    phone_number = "310-555-9101",
    email = "pastaboy/2gmail.com",
    height = "5'10",
    weight = "160 lbs",
    medical_history = "High blood pressure",
    emergency_contact = "Rita Ricci"
)
print(patient1.medical_form())
print(patient2.medical_form())
print(patient3.medical_form())

