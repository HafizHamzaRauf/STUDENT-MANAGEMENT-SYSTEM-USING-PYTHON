from User import User

class Faculty(User):
    def __init__(self,username,password,designation,main_subject):
        super().__init__( username, password)
        self.__designation = designation
        self.__main_subject = main_subject
    @property 
    def designation(self):
        return self.__designation
    @designation.setter
    def designation(self,value):
        self.__designation = value
    @property 
    def main_subject(self):
        return self.__main_subject
    @main_subject.setter
    def main_subject(self,value):
        self.__main_subject = value
    def print_user(self):
        print('-'*50)
        print('Faculty Member Name:',self.username)
        print('Faculty Member Password:',self.password)
        print('Faculty Member Designation:',self.designation)
        print('Faculty Member Subject:',self.main_subject)
        print('-'*50)
