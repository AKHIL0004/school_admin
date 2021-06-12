class student():
    college_name = 'AKTU'


    def __init__(self,name,age,dob,marks):
        self.student_name = name
        self.student_age  = age
        self.student_dob  = dob
        self.student_marks = marks
    def  update_marks(self,new_marks):
        self.student_marks = new_marks
        return
    def update_marks(self,new_marks):
        self.student_marks = new_marks
        return
    def to_string(self):
        utility()
        string = "name: {},dob: {},marks: {}".format(self.student_name,self.student_age,self.student_dob,self.student_marks)
        return string
    def utility(self,args*):
         Code 
         code 
         code


student1 = student("Akhil",21,"20/08/2000")
student2 = student("aayushmaan",19,"04/08/2002")

print(student1.to_string()+"\n")
print(student2.to_string())

student2.utility()
student2.update_marks(100)
                
        