# _protected __private
# access modifier

# getters and setters

class userdetail:
    __username = ''
    __password = ''
    
    def getusername(self):
        return self.__username
    
    def getpassword(self):
        return self.__password
    def setusername(self,uname):
        self.__username = uname
    
    def setpassword(self,password):
        self.__password = password

class authenticate(userdetail):
    pass 



class test:
    priyanshu = authenticate()
    priyanshu.setusername("priyanshujha@gmail.com")
    priyanshu.setpassword(12345)