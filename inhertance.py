class employee:
    def __init__(self, name, id):
        self.name =  name
        self.id =  id
    
    def showDetails(self):
        print(f"Employee details are id {self.id} , name {self.name}")

    def saveDetails(self):
        fileobj =  open("EmployeeDetails.txt", "a")
        fileobj.write(f"Employee details are id {self.id} , name {self.name} \n")
        fileobj.close()



e1 =  employee('divya', '123')
e1.saveDetails()
e2 =  employee('Anil', '1234')
e2.saveDetails()


class programmer(employee):
    def language(self, language):
        #language =  *language
        self.language =  language
        print(f"language specializations is {self.language}")


e3 =  programmer("Sharul", "345")
e3.language("python")
e3.showDetails()