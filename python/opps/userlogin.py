class user:

    username = None
    password = None

    def __init__(self,u,p):
        self.username = u        
        self.password = p
    def login(self):
        print("login success " +self.username)

    def logout(self):
        print("loged out ", +self.password)



class test:
    user1 = user("anuj",12345)
    user1.login()
    user1.logout()