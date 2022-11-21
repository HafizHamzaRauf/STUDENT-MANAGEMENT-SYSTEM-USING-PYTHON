from utils import print_line
class DBConnectionError(Exception):
    def  __init__(self,msg):
        self.__messge = msg
    def printErrorMessage(self):
        print(self.__messge)
        
class UserNotFoundError(Exception):
    def  __init__(self,msg):
        self.__messge = msg
    def printErrorMessage(self):
        print_line(self.__messge)
        
