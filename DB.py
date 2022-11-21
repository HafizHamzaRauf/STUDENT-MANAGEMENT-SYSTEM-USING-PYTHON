import pymysql
from Exceptions import DBConnectionError,UserNotFoundError
from Student import Student
from Faculty import Faculty
class DB:
    def __init__(self,host,user,password, database):
        try:
            self.__db= None
            self.__cursor = None
            self.__db = pymysql.connect(host = host,user= user,password= password,database= database)
            self.__cursor = self.__db.cursor()
            if(self.__db==None or self.__cursor== None):
                raise DBConnectionError('Database Connection Error')
        except DBConnectionError as e:
            e.printErrorMessage()
    def __insert_user(self,obj):
        try:
            #INSERTING A NEW  USER  IN THE TABLE
            query = 'INSERT INTO user (username ,password) VALUES(%s ,%s)'
            args =  (obj.username,obj.password)
            self.__cursor.execute(query,args)
            self.__db.commit()
            
            #SELECTING THE NEWLY CREATED USER  TO RETURN ITS  USER_ID
            query= 'SELECT user_id FROM user WHERE username=%s'
            args= (obj.username)
            self.__cursor.execute(query,args)
            data = self.__cursor.fetchall()
            return data[0][0]
        except Exception as e:
            print(str(e))
    def insert_faculty(self,faculty):
        try:
            user_id = self.__insert_user(faculty)
            query = 'INSERT INTO faculty (designation,main_subject,user_id) VALUES(%s ,%s,%s)'
            args = (faculty.designation,faculty.main_subject,user_id)
            self.__cursor.execute(query,args)
            self.__db.commit()
        except Exception as e:
            print(str(e))  
     
    def insert_student(self,student):
        try:
            user_id = self.__insert_user(student)
            query = 'INSERT INTO student (semester,cgpa,major,user_id) VALUES(%s ,%s,%s,%s)'
            args = (student.semester,student.cgpa,student.major,user_id)
            self.__cursor.execute(query,args)
            self.__db.commit()
        except Exception as e:
            print(str(e))  
    def authenticate_User(self,user_info,user_type):
        try:            
            query = 'SELECT * FROM  user WHERE username = %s and password = %s'
            self.__cursor.execute(query,user_info)
            data= self.__cursor.fetchall()
            status  = len(data)
            if(status==0):
                return (False,False)
            else:
                if(user_type=='s'):
                    query='SELECT * FROM student where user_id=%s'
                    args = (data[0][0])
                    self.__cursor.execute(query,args)
                    value= self.__cursor.fetchall()
                    if(len(value)==0):
                        return (False,None)
                    else:
                        return (True,value[0])
                elif(user_type=='f'):
                    query='SELECT * FROM faculty where user_id=%s'
                    args = (data[0][0])
                    self.__cursor.execute(query,args)
                    value= self.__cursor.fetchall()
                    if(len(value)==0):
                        return (False,None)
                    else:
                        return  (True,value[0])
        except Exception as e:
            print(str(e))
    def get_User_id(self,obj):
        #getting the id  of the previous data
        query  = 'SELECT user_id from user where username =%s'
        args = obj.username
        self.__cursor.execute(query,args)
        data = self.__cursor.fetchall()
        return data[0][0]
    def update_faculty(self,prev_data,new_data):
        try:
            user_id = self.get_User_id(prev_data)
            query = 'update faculty set designation=%s ,main_subject =%s where user_id= %s'
            args  = (new_data.designation,new_data.main_subject,user_id)
            self.__cursor.execute(query,args)
            query= 'update user set username = %s, password = %s  where user_id =  %s'
            args  = (new_data.username,new_data.password,user_id)
            
            self.__cursor.execute(query,args)
            self.__db.commit()
            
        except Exception as e:
            print(str(e))              
    def update_student(self,prev_data,new_data):
        try:
            user_id= self.get_User_id(prev_data)
            query= 'update user set username = %s, password = %s  where user_id =  %s'
            args  = (new_data.username,new_data.password,user_id)
            self.__cursor.execute(query,args)
            query='update student set semester= %s ,cgpa= %s  ,major = %s  where user_id = %s'
            args = (new_data.semester , new_data.cgpa ,new_data.major,user_id)
            self.__cursor.execute(query,args)
            self.__db.commit()
        except Exception as e:
            print(str(e))
    def __del__(self):
        if(self.__cursor!= None):
            self.__cursor.close()
        if(self.__db!= None):
            self.__db.close()

    def delete_faculty(self,obj):
        try:
            id = self.get_User_id(obj)
            query  = 'delete from faculty where user_id  = %s'
            args = (id)
            self.__cursor.execute(query  ,args)
            query='delete from user where user_id = %s'
            args = (id)
            self.__cursor.execute(query,args)
            self.__db.commit()
        except Exception as e:
            print(str(e))
    def delete_student(self,obj):
        try:
            id = self.get_User_id(obj)
            
            query  = 'delete from student where user_id  = %s'
            args = (id)
            self.__cursor.execute(query  ,args)
            query='delete from user where user_id = %s'
            args = (id)
            self.__cursor.execute(query,args)
            self.__db.commit()
        except Exception as e:
            print(str(e))
