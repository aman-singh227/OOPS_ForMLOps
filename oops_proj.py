class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        

    def menu(self):
        user_input= input("""Welcome to chatbook !! How would you like to proceed?
                          1. Press 1 to signup
                          2. Press 2 to signin
                          3. Press 3 to to write a post
                          4. Press 4 to message a friend
                          5. Press any other  key to exit
                          
                           -->""")
        if user_input =='1':
            self.signup()
            pass
        elif user_input =='2':
            self.signin()
            pass
        elif user_input == '3':
            self.my_post()
            pass
        elif user_input == '4':
            self.sendmsg()
            pass
        else:
            exit()

    def signup(self):
        email= input('Enter the email here :-')
        pwd = input('Enter the password here :-')
        self.username = email
        self.password = pwd
        print('You have signed up successfully')
        print('\n')
        self.menu()
    
    def signin(self):
        if self.username =="" and  self.password =='':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname=input("Enter your email/username here ->")   
            pwd=input("Enter your email/username here ->")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully")
                self.loggedin = True
            else:
                print("Please input the creditals")   
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt=input("Write your post/blog")
            print(f"Following content has been posted ->{txt}")
        else:
            print("Firstly signin/signup to write the post")  
        print("\n")
        self.menu()  

    def sendmsg(self):
        if self.loggedin==True:
            txt= input("Enter your message here ->")
            frnd = input('Whom to sned the msg?')
            print("The msg has been send")
        else:
            print("Firstly signin/signup the message")
        print("\n")
        self.menu()        


obj = chatbook()   