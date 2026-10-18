from tkinter import *
from tkinter import messagebox
import data

db=data.Database('d:/lesson/project/data.db')

win = Tk()
win.geometry('500x300')
win.title('login form')
win.configure(bg='pink')
# function =====================================
def add():
    fname=ent_fname.get()
    lname=ent_lname.get()
    email=ent_email.get()
    password=ent_password.get()

    db.insert(fname,lname,email,password)
    messagebox.showinfo('insert','record inserted')
    clear_ent()

def clear_ent ():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_email.delete(0,END)
    ent_password.delete(0,END)
    ent_fname.focus_set()

def exit ():
    result = messagebox.askquestion('exit','are you sure ?')
    if result == 'yes':
        win.destroy()

def login():
    fname=ent_fname.get()
    lname=ent_lname.get()
    email=ent_email.get()
    password=ent_password.get()
    user = db.search(email,password)
    if user:
        new_win = Toplevel(win)
        new_win.geometry('300x200')
        new_win.title('Welcome')
        lbl_welcome = Label(new_win,
            text=f'Welcome {fname}',
            font='tahoma 15 bold',
        )
        lbl_welcome.pack(pady=60)
    else:
        messagebox.showerror('Error','Email or password is incorrect! ' \
        ' please sign up')

#   widget ========================================


lbl_fname=Label(win,text="first name :",font='tahoma 15 bold',bg='pink')
lbl_fname.place(x=40,y=20)

ent_fname=Entry(win,width=30)
ent_fname.place(x=200,y=25)

lbl_lname=Label(win,text="last name :",font='tahoma 15 bold',bg='pink')
lbl_lname.place(x=40,y=60)

ent_lname=Entry(win,width=30)
ent_lname.place(x=200,y=65)

lbl_star=Label(win,text="*",font='tahoma 15 bold' ,fg='red' ,bg='pink')
lbl_star.place(x=15,y=100)

lbl_email=Label(win,text="email :",font='tahoma 15 bold',bg='pink')
lbl_email.place(x=40,y=100)

ent_email=Entry(win,width=30)
ent_email.place(x=200,y=105)


lbl_star=Label(win,text="*",font='tahoma 15 bold' ,fg='red',bg='pink')
lbl_star.place(x=15,y=140)

lbl_password=Label(win,text="password:",font='tahoma 15 bold',bg='pink')
lbl_password.place(x=40,y=140)

ent_password=Entry(win,width=30 , show= '*')
ent_password.place(x=200,y=145)

btn_signup=Button(win,width=20,text='sign up' ,command=add)
btn_signup.place(x=40,y=200)

btn_signin=Button(win,width=20,text='sign in',command=login)
btn_signin.place(x=232,y=200)

btn_exit=Button(win ,text='exit'  , command=exit, width=20)
btn_exit.place(x=150 , y=250)


win.mainloop()