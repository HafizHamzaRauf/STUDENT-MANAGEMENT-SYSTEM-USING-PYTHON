
class User:
    def  __init__(self,username,password):
        self.__username = username
        self.__password = password
    @property 
    def  username(self):
        return self.__username
    @property 
    def  password(self):
        return self.__password
    @username.setter
    def username(self,val):
        self.__username = val
    @password.setter
    def password(self,val):
        self.__password = val
    
        