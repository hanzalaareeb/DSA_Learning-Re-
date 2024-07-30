import datetime as date
class Person:
    def __init__(self, name, country, dateofbirth):
        self.name = name
        self.country = country
        #convert dateofbirth string into date object
        self.dateofbirth = date.datetime.strptime(dateofbirth, "%d-%m-%Y").date()
        
    def age(self):
        # calculate age based on date of birth
        today = date.date.today()
        age = today.year - self.dateofbirth.year
        if today.month < self.dateofbirth.month or (today.month == self.dateofbirth.month and today.day < self.dateofbirth.day):
            age -= 1
        return age

firstPerson = Person("karan", "India", "15-06-2002")
print(firstPerson.age())