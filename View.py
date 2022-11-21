from Student import Student
from Faculty import Faculty
from utils import print_line
class Student_Management_System_View:
    def starting_menu(self):
        print('-'*50)
        print('Welcome To Student Management System'.center(50))
        print('-'*50)
        print('1: REGISTER')
        print('2: LOGIN')
        print('3: EXIT')
        print('-'*50)
        try:
            choice = input('Enter Your Choice:')
            if(choice=='1' or choice =='2' or  choice=='3'):
                return choice
            else:
                raise Exception('Please Enter  a valid choice')
        except Exception as e:
            print(str(e))
            return self.starting_menu()
    def get_User_Type(self):
        try:
            type = input('Are You a Student(s) or a Faculty Member(f):')
            if(type.lower()=='s' or  type.lower()=='f'):
                return type
            else:
                raise Exception('Enter a valid choice')
        except Exception as e:
            print(str(e))
            return self.get_User_Type()      
    def register(self,user_type):
        print_line('Registration')
        if(user_type=='f'):
            return self.get_faculty()
        elif(user_type =='s'):
            return self.get_student()
        
    def get_student(self):
        try:
            username = input('Enter Your Name:')
            password = input('Enter password(more than 5 digit):')
            if(password.__len__()< 5):
                raise Exception('Please Enter password with more than 5 digits')
            semester = int(input('Enter your semester:'))
            if(semester < 0 ):
                raise Exception('Please enter semester number correctly')
            cgpa = float(input('Enter Your CGPA:'))
            if(cgpa < 0 or  cgpa  > 4):
                raise Exception('Please Enter CGPA between (0-4)')
            major = input('Enter Your Major:')
            student = Student(username,password,semester,cgpa,major)
            return student            
        except Exception as  e:
            print(str(e))
            return self.get_student()
    def get_faculty(self):
        try:
            username = input('Enter Your Name:')
            password = input('Enter password(more than 5 digit):')
            if(password.__len__()< 5):
                raise Exception('Please Enter password with more than 5 digits')
            designation = input('Enter Your Designation:')
            main_subject = input('Enter Your Main Subject')
            faculty = Faculty(username, password, designation, main_subject)
            return faculty
        except Exception as e:
            print(str(e))
            return self.get_faculty()

    def login(self):
        print_line('LOGIN')
        try:
            username = input('Enter Username:')
            password = input('Enter Password:')
            if(username=='' or password==''):
                raise Exception('Please Enter username or Password')
            return (username,password)
        except Exception as e:
            print(str(e))
            return self.login()
    
    def operations_menu(self):
        print('-'*50)
        print('1: View Profile')
        print('2: Edit Profile')
        print('3: Delete Profile')
        print('4: LOGOUT')
        print('-'*50)
        try:
            choice = input('Enter Your choice:')
            if(choice=='1' or choice =='2' or  choice=='3' or choice=='4'):
                    return choice
            else: 
                raise Exception('Please Enter a valid choice')
        except Exception as e:
            print(str(e))
            return self.operations_menu()
    def view_profile(self,user_type,obj):
        print_line('YOUR PROFILE')
        obj.print_user()
        print('View Profile')
    def edit_profile(self,user_type):
        print_line('EDIT PROFILE')
        if(user_type.lower()=='s'):
            return self.get_student()
        if(user_type.lower()=='f'):
            return  self.get_faculty()
    def delete_profile(self):
        print_line('DELETING PROFILE')
        
