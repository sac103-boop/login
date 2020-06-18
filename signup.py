from tkinter import *
from tkinter import messagebox
import sqlite3

usuarios=sqlite3.connect("Usuarios")
cursor=usuarios.cursor()
try:
	cursor.execute("CREATE TABLE Usuarios(fname VARCHAR(20), lname VARCHAR(30), user VARCHAR(20) UNIQUE, password VARCHAR(20), cpassword VARCHAR (20))")

except:
	pass
	
root=Tk()

menu=Menu(root)

root.title("Sign Up")
root.resizable(0,0)
root.geometry("680x500")
root.config(bg="#E6EDF1",menu=menu)
frame=Frame(relief="groove")
frame.pack()
frame.config(bg="#fff",width="550", height="430")
frame.grid(pady=48,padx=80)
img = PhotoImage(file="logoc.png") 
imagen=Label(root,image=img)
imagen.place(x=78,y=30)

signup=Label(frame,text="Create your account")
signup.place(x=160,y=80)
signup.config(bg="#fff",font=("Calibri",20))

name=Label(frame,text="First Name:")
name.place(x=25,y=130)
name.config(bg="#fff",font=("Calibri",15))

entername=Entry(frame,width=30)
entername.place(x=25,y=160)
entername.config(font=("Comic Sans MS",10),bg="#F8FAFD")

lname=Label(frame,text="Last Name:")
lname.place(x=285,y=130)
lname.config(bg="#fff",font=("Calibri",15))

enterlname=Entry(frame,width=30)
enterlname.place(x=285,y=160)
enterlname.config(font=("Comic Sans MS",10),bg="#F8FAFD")

user=Label(frame,text="UserName:")
user.place(x=25,y=200)
user.config(bg="#fff",font=("Calibri",15))

enteruser=Entry(frame,width=30)
enteruser.place(x=25,y=230)
enteruser.config(font=("Comic Sans MS",10),bg="#F8FAFD")

password=Label(frame,text="Password:")
password.place(x=285,y=200)
password.config(bg="#fff",font=("Calibri",15))

enterpassword=Entry(frame,width=30)
enterpassword.place(x=285,y=230)
enterpassword.config(font=("Comic Sans MS",10),bg="#F8FAFD",show="*")

cpassword=Label(frame,text="Confirm your Password:")
cpassword.place(x=160,y=270)
cpassword.config(bg="#fff",font=("Calibri",15))

entercpassword=Entry(frame,width=30)
entercpassword.place(x=160,y=300)
entercpassword.config(font=("Comic Sans MS",10),bg="#F8FAFD",show="*")

	
def signup():
	if enterpassword.get()!=entercpassword.get():
		entercpassword.config(bg="#FD6143")
		enterpassword.config(bg="#FD6143")
		messagebox.showwarning(title="Password",message="passwords don't match")

	elif enterpassword.get()=="":
		enterpassword.config(bg="#FD6143")
		messagebox.showwarning(title="Password",message="The password field can´t be empty")

	else:

		try:
			person=[(entername.get(),enterlname.get(),enteruser.get(),enterpassword.get(),entercpassword.get())]
			cursor.executemany("INSERT INTO Usuarios VALUES (?,?,?,?,?)", person)
			usuarios.commit()
			entercpassword.config(bg="#60FD43")
			enterpassword.config(bg="#60FD43")
			messagebox.showinfo(title=None, message="your account was create")
		except:
			messagebox.showwarning(title="ERROR", message="This user alredy exist")

def close():
	root.destroy()
	import login
buttonsignup=Button(frame, text="Continue",width=40, relief="flat",command=lambda:signup())
buttonsignup.place(x=30,y=350)
buttonsignup.config(bg="#B0BDD7",font=("Bradley Hand ITC",15))

Exit=Menu(menu,tearoff=0)
Exit.add_command(label="EXIT",command=close)
menu.add_cascade(label="EXIT",menu=Exit)

root.mainloop()
	
