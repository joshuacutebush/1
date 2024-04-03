from tkinter import*
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)


        # Login Frame
        Frame_login = Frame(self.root, bg="")
        Frame_login.place(x=330, y=150, width=500, height=400 )

        # Title & Subtitle
        title= Label(Frame_login, text="Login Here", font=("impact", 35, "bold"), fg="#6162ff", bg="white").place(x=90,y=30)
        title = Label(Frame_login, text="Members Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90,y=100)

        #Username
        lbl_user =  Label(Frame_login, text="Username", font=("groudy old style", 15, "bold"), fg="grey", bg="white").place(x=90, y=140)
        self.username = Entry(Frame_login, font=("groudy old style", 15),bg="#e7e6e6")
        self.username.place(x=90, y=170, width=320, height=35)

       # Password
        lbl_password = Label(Frame_login, text="Password", font=("groudy old style", 15, "bold"), fg="grey",bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("groudy old style", 15), bg="#e7e6e6")
        self.password.place(x=90, y=240, width=320, height=35)

        #Button
        forget = Button(Frame_login, text="ForgetPassword?",bd=0,cursor="hand2", font=("groudy old style", 12, "bold"), fg="#6162ff",bg="white").place(x=90, y=280)
        submit = Button(Frame_login, command=self.check_function,cursor="hand2", text="Login?", bd=0, font=("groudy old style", 15), bg="#6162ff",fg="white").place(x=90, y=320, width=180, height=40)

    def check_function(self):
            if self.username.get()=="" or self.password.get()=="":
                messagebox.showerror("Error", "All Field are required",parent=self.root)
            elif self.username.get()!="Joshua" or self.password.get()!="123456":
                messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
            else:
                messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")


root = Tk()
obj = Login(root)
root.mainloop()

