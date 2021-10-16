
class login:
    def __init__(self):
        self.credintials = {}
    def register(self, username, password):
        self.credintials[username] = password

    def check(self, user, pas):
        if user in self.credintials.keys() and pas == self.credintials[user] :
            print("Login success!")
        else:
            print('Wrong Username or Password')

s = login()


def account ( Stop ):

    while Stop == False:
        tasks = int(input('''please enter the task you want to do :
1) signup 
2) login
3) quit \t'''))

        if tasks == 1:
            UserName = (input('Please enter your username:\t'))
            Password= (input('Please enter your password:\t'))
            s.register(UserName, Password)


        if tasks == 2:
            LoginInfoUser = (input('Please enter your username:\t'))
            LoginInfoPassword = (input('Please enter your password:\t'))
            s.check(LoginInfoUser,LoginInfoPassword)
        if tasks == 3:
            print("Thanks for using my code!")
            Stop =True