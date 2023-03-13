#Public,Procter,Private
class student:
    def __init__(self,name,age):
        self.studentname=name
        self.studentage=age
    def displayAge(self):
        print("Age:",self.studentage)
obj=student("Rahul",20)
print("Name:",obj.studentname)
obj.displayAge()