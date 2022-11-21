from User import User

class Student(User):
    def __init__(self,username= None,password=None,semester= None,cgpa=None,major= None):
        super().__init__(  username, password)
        self.__semester  = semester
        self.__cgpa  = cgpa
        self.__major = major
    @property
    def semester(self):
        return self.__semester
    @semester.setter
    def semester(self,value):
        self.__semester= value    
    @property
    def cgpa(self):
        return self.__cgpa
    @cgpa.setter
    def  cgpa(self,value):
        self.__cgpa = value
    @property
    def major(self):
        return self.__major
    @major.setter
    def major(self,value):
        self.__major= value
    def print_user(self):
        print('-'*50)
        print('Student Name:',self.username)
        print('Student Password:',self.password)
        print('Current Semester:',self.semester)
        print('CGPA:',self.cgpa)
        print('Major:',self.major)
        print('-'*50)

