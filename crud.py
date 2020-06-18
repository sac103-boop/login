from tkinter import *
from tkinter import messagebox
import sqlite3


root=Tk()

menu=Menu(root)
root.geometry("700x450")
root.resizable(0,0)
root.title("Add People")
root.config(bg="#E6EDF1",menu=menu)

#--------------------------------frame-----------------------------------------------------
Frame=Frame(relief="flat")
Frame.pack()
Frame.config(width=600, height=400,bg="#fff")
Frame.grid(pady=25,padx=50)

img = PhotoImage(file="logob.png") 
imagen=Label(Frame,image=img)
imagen.place(x=-3,y=0)


def label(pl,tx,fo,b,px,py):
	Label(pl,text=tx,font=fo,bg=b).place(x=px,y=py)


principal_label=label(Frame,"ADD PEOPLE",("Calibri",20),"#fff",230,100)


#----------------idLabelandEntry---------------------------

id_label=label(Frame,"Id:",("calibri",15),"#fff",100,135)

setter1=StringVar()

id_enter=Entry(Frame,textvariable=setter1)
id_enter.place(x=100,y=165)
id_enter.config(font=("Comic Sans MS",10),bg="#F8FAFD")


#--------------fname label and Entry----------------------
fname_label=label(Frame,"First Name:",("calibri",15),"#fff",330,135)

setter2=StringVar()

fname_enter=Entry(Frame,textvariable=setter2)
fname_enter.place(x=330,y=165)
fname_enter.config(font=("Comic Sans MS",10),bg="#F8FAFD")

#--------------lname label and entry----------------------

lname_label=label(Frame,"Last Name:",("calibri",15),"#fff",210,190)

setter3=StringVar()

lname_enter=Entry(Frame,textvariable=setter3)
lname_enter.place(x=210,y=220)
lname_enter.config(font=("Comic Sans MS",10),bg="#F8FAFD")

#--------------age label and entry----------------------
age_label=label(Frame,"Age:",("calibri",15),"#fff",100,250)

setter4=StringVar()

age_enter=Entry(Frame,textvariable=setter4)
age_enter.place(x=100,y=275)
age_enter.config(font=("Comic Sans MS",10),bg="#F8FAFD")

#--------------address label and entry----------------------
address_label=label(Frame,"Address:",("calibri",15),"#fff",300,250)

setter5=StringVar()

address_enter=Entry(Frame,textvariable=setter5)
address_enter.place(x=300,y=275)
address_enter.config(font=("Comic Sans MS",10),bg="#F8FAFD")

#-------create and connect to data base------------------------
cbbdd=False
def connect():
	people=sqlite3.connect("people")
	cursor=people.cursor()
	global cbbdd
	global count
	cbbdd = True
	try:
		cursor.execute('''CREATE TABLE People(
		Id INTEGER PRIMARY KEY AUTOINCREMENT,
		Fname VARCHAR(20),
		Lname VARCHAR (25),
		Age VARCHAR(20),
		address VARCHAR(20))''')
		
		messagebox.showinfo(title="BBDD", message="The database was created successfully")
	except:
		messagebox.showwarning(title="BBDD", message="The database has already been created")
		cbbdd = True
#--------------------close the program---------------------------
def exit():
	confirm=messagebox.askyesno(title="Exit",message="Do you want to go out?")
	if confirm:
		root.destroy()
#------------------------------clean all fields-----------------------
def clean():
	setter1.set("")
	setter2.set("")
	setter3.set("")
	setter4.set("")
	setter5.set("")
#--------------------------------add a people--------------------------
def create():
	if cbbdd:
		people=sqlite3.connect("people")
		cursor=people.cursor()

		data=[(fname_enter.get(),lname_enter.get(),age_enter.get(),address_enter.get())]
		cursor.executemany("INSERT INTO People VALUES(NULL,?,?,?,?)",data)
		people.commit()
		people.close()

		messagebox.showinfo(title="Successful", message="This person was added")
		setter1.set("")
		setter2.set("")
		setter3.set("")
		setter4.set("")
		setter5.set("")
	else:
		pass
def read():
	if cbbdd:
		people=sqlite3.connect("people")
		cursor=people.cursor()
		num=id_enter.get()
		cursor.execute("SELECT * FROM People WHERE Id=?",num)
		container=cursor.fetchall()
		for cont in container:
			setter2.set(cont[1])
			setter3.set(cont[2])
			setter4.set(cont[3])
			setter5.set(cont[4])
		people.commit()
		people.close()
	else:
		pass


def update():
	num=id_enter.get()
	if cbbdd:
		people=sqlite3.connect("people")
		cursor=people.cursor()
		#data=[(fname_enter.get(),lname_enter.get(),age_enter.get(),address_enter.get())]
		cursor.execute("UPDATE People SET Fname=?, Lname=?,age=?,address=? WHERE Id=?",(fname_enter.get(),lname_enter.get(),age_enter.get(),address_enter.get(),id_enter.get()))

		people.commit()
		people.close()
		messagebox.showinfo(title="Successful", message="This person was Updated")
		setter1.set("")
		setter2.set("")
		setter3.set("")
		setter4.set("")
		setter5.set("")

def delete():
	num=id_enter.get()
	if cbbdd:
		people=sqlite3.connect("people")
		cursor=people.cursor()
		cursor.execute("DELETE FROM People WHERE Id=?",num)
		people.commit()
		people.close()
		messagebox.showinfo(title="Successful", message="This person was Deleted")
		setter1.set("")
		setter2.set("")
		setter3.set("")
		setter4.set("")
		setter5.set("")

	else:
		pass


bcreate=Button(Frame,text="Create",command=create)
bcreate.config(width=10,relief="flat",bg="#B0BDD7",font=("Bradley Hand ITC",15))
bcreate.place(x=25,y=320)

bread=Button(Frame,text="Read",command=read)
bread.config(width=10,relief="flat",bg="#B0BDD7",font=("Bradley Hand ITC",15))
bread.place(x=165,y=320)

bupdate=Button(Frame,text="Update")
bupdate.config(width=10,relief="flat",bg="#B0BDD7",font=("Bradley Hand ITC",15),command=update)
bupdate.place(x=305,y=320)

bdelete=Button(Frame,text="Delete",command=delete)
bdelete.config(width=10,relief="flat",bg="#B0BDD7",font=("Bradley Hand ITC",15))
bdelete.place(x=445,y=320)



#-----------------------------------------top menu--------------------------------
bbdd=Menu(menu,tearoff=0)
bbdd.add_command(label="Connect",command=connect)

bbdd.add_command(label="Exit",command=exit)

erase=Menu(menu,tearoff=0)
erase.add_command(label="Erase all fields",command=clean)


crud=Menu(menu,tearoff=0)
crud.add_command(label="Create",command=create)
crud.add_command(label="Read",command=read)
crud.add_command(label="Update",command=update)
crud.add_command(label="Delete",command=delete)

menu.add_cascade(label="BBDD", menu=bbdd)
menu.add_cascade(label="ERASE", menu=erase)
menu.add_cascade(label="CRUD", menu=crud)

root.mainloop()