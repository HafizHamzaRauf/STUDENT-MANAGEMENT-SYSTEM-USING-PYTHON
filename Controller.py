from View import Student_Management_System_View
from Exceptions import UserNotFoundError
from utils import print_line
from  DB import DB
from Student import Student
from Faculty import Faculty
class Controller:
    def __init__(self):
        self.__view= Student_Management_System_View()
        self.__current_customer = None
        self.__user_type = None
        self.__db = DB('localhost', 'root', 'abc', 'fcit')
    @property 
    def view(self):
        return self.__view
    def main(self):
        starting_menu_choice= self.view.starting_menu()
        if(starting_menu_choice=='3'):
            print_line('Thanks For Using This System')
            exit()
        self.__user_type=self.view.get_User_Type()
        if(starting_menu_choice=='1'):
            obj = self.view.register(self.__user_type)
            self.register(obj)
            print_line('LOGIN TO CONTINUE')
            self.login()
        if(starting_menu_choice=='2'):
            self.login()
        self.perform_functions()
    def perform_functions(self):
        operation_menu_choice= self.view.operations_menu()
        if(operation_menu_choice=='1'):
            self.view_profile()
            self.perform_functions()
        if(operation_menu_choice=='2'):
            self.edit_profile()
            self.perform_functions()
        if(operation_menu_choice=='3'):
            self.delete_profile()
            self.perform_functions()
        if(operation_menu_choice=='4'):
            self.__current_customer= None
            self.main()
    def register(self,obj):        
        if(self.__user_type=='s'):
            self.__db.insert_student(obj)
        if(self.__user_type=='f'):
            self.__db.insert_faculty(obj)  
        print_line('REGISTRATION SUCCESSFULL')
    def login(self):
        try: 
            user_info = self.view.login()
            
            status = self.__db.authenticate_User(user_info,self.__user_type)
            if(status[0]==False):
                raise UserNotFoundError('User not found with this credentials')
            if(self.__user_type=='s'):
                self.__current_customer = Student(user_info[0],user_info[1],status[1][0],status[1][1],status[1][2])
            elif(self.__user_type=='f'):
                self.__current_customer = Faculty(user_info[0], user_info[1], status[1][0], status[1][1])
            print_line('User LOGIN SUCCESSFULL!')
        except UserNotFoundError as e:
            e.printErrorMessage()
            self.login()
        except Exception as e:
            print(str(e))
            self.login()
    def view_profile(self):
        self.__current_customer.print_user()
    def edit_profile(self):
        
        updated_customer = self.view.edit_profile(self.__user_type) 
        updated_customer.print_user()
        if(self.__user_type=='s'):
            self.__db.update_student(self.__current_customer,updated_customer)
        if(self.__user_type=='f'):
            self.__db.update_faculty(self.__current_customer,updated_customer)
        self.__current_customer= updated_customer
        print_line('PROFILE UPDATED SUCCESSFULLY')
    def delete_profile(self):
        try:
            self.view.delete_profile()
            if(self.__user_type=='f'):
                self.__db.delete_faculty(self.__current_customer)
            if(self.__user_type=='s'):
                self.__db.delete_student(self.__current_customer)
            print_line('USER DELETED  SUCCESSFULLY')
            self.__current_customer = None
            self.main()
        except Exception as e:
            print(str(e))
            
            
            

val = Controller()
val.main()
        