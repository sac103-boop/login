from tkinter import *
from tkinter import messagebox
import sqlite3

usuarios=sqlite3.connect("Usuarios")
cursor=usuarios.cursor()


root=Tk()
root.title("Log In")
root.resizable(0,0)
root.geometry("680x450")
root.config(bg="#E6EDF1")


frame=Frame(relief="flat")
frame.pack()
frame.config(bg="#fff",width="300", height="370")
frame.grid(pady=48,padx=189)

img = PhotoImage(file="logo.png") 
imagen=Label(frame,image=img)
imagen.place(x=-3,y=0)

welcome=Label(frame, text="Welcome")
welcome.place(x=95,y=100)
welcome.config(font=("calibri",20),bg="#fff")

usuario_label=Label(frame,text="UserName:")
usuario_label.place(x=45,y=145)
usuario_label.config(font=("calibri",15),bg="#fff")

usuario_entry=Entry(frame, width=25)
usuario_entry.place(x=45,y=170)
usuario_entry.config(font=("Comic Sans MS",10))

usuario_contraseña=Label(frame,text="Password:")
usuario_contraseña.place(x=45,y=205)
usuario_contraseña.config(font=("calibri",15),bg="#fff")

usuario_entry_password=Entry(frame, width=25)
usuario_entry_password.place(x=45,y=230)
usuario_entry_password.config(font=("Comic Sans MS",10),show="*")





def logIn():

	cursor.execute("SELECT * FROM Usuarios WHERE user=? AND password=?",(usuario_entry.get(),usuario_entry_password.get()))
	consulta=cursor.fetchall()
	usuarios.commit()
	if usuario_entry.get()=='' or usuario_entry_password.get()=='':
		messagebox.showwarning(title="ERROR", message="The field can't be empty")
	else:
		if consulta:
			root.destroy()
			import crud

		else:
			messagebox.showwarning(title="ERROR", message="The password is wrong")


def nueva_ventana():
	root.destroy()
	import signup



boton_login=Button(frame, width=10, command=lambda:logIn(),text="LOGIN",font=("Bradley Hand ITC",10),relief="flat")
boton_login.place(x=45,y=300)
boton_login.config(bg="#B0BDD7")

boton_signup=Button(frame, width=15,text="SIGN UP NOW",font=("Bradley Hand ITC",10),relief="flat",command=nueva_ventana)
boton_signup.place(x=145,y=300)
boton_signup.config(bg="#B0BDD7")





root.mainloop()

