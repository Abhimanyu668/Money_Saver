from logging import warning
from tkinter import *
from tkinter.font import ITALIC
import tkinter.messagebox as messageBox
import mysql.connector as mysql
from PIL import Image,ImageTk
window = Tk()

#title and logo of windows
window.title("MoneySaver")
img=PhotoImage(file='A:\\priceTracker\\images\\logo.png')
window.iconphoto(False,img)



# function for inserting data in main table
def insert_main():
    Email1=ent_email1.get()
    password=ent_password1.get()
    #print(Email1)



    con=mysql.connect(host="bttotienkk1dqejaut6j-mysql.services.clever-cloud.com",
            user="*************",passwd="*************",
            database="bttotienkk1dqejaut6j")
    cursor=con.cursor()
    #sql="select password from registration where Email=%s";
    #cursor.execute(sql,(Email1,))
    #cursor.execute("select Email from registration where Email=%s",(email1))
    #row=cursor.fetchone()
    #print(row[0])
    #password=row[0]
    cursor.execute("insert into main(Email,password)values('"+Email1+"','"+password+"')")
    cursor.execute("commit");
    con.close();

#inset function for inserting data into databases from register function
def insert_reg():
    name=ent_name.get()
    email=ent_email.get()
    password=ent_password.get()
    if(name=="" or email=="" or password==""):
        messageBox.showinfo("Insert status","All fields are required:")
        delete_reg()
        register()
    else:
        con=mysql.connect(host="bttotienkk1dqejaut6j-mysql.services.clever-cloud.com",
            user="*************",passwd="*************",
            database="bttotienkk1dqejaut6j")
        cursor=con.cursor()
        cursor.execute("insert into registration(Name,Email,Password)values('"+name +"','"+email +"','"+password +"')")
        cursor.execute("commit");
        messageBox.showinfo("Insert status", "Registerd successfully\n Now you can add URL and PRICE\n into application:")
        con.close();
        delete_login()
        login()


#function for jump to url page
def product_window():
    window.destroy()
    import product

#function for match data from database
def fetch_login():
    if ent_email1.get()=="" or ent_password1.get=="":
        messageBox.showerror("Error","All fields are required") 
    else:
        try:
            con=mysql.connect(host="bttotienkk1dqejaut6j-mysql.services.clever-cloud.com",
            user="*************",passwd="*************",
            database="bttotienkk1dqejaut6j")
            cursor=con.cursor()
            cursor.execute("select * from registration where email=%s and password=%s",(ent_email1.get(),ent_password1.get()))
            row=cursor.fetchone()
            if row==None:
                delete_login()
              
                messageBox.showerror("Error","Invalid Name & Email")
                login()                
            else:
                messageBox.showinfo("Success","welcome")
                insert_main()
                product_window()
            cursor.close()
        except Exception as es:
            messageBox.showerror("Error",f"Error due to:{str(es)}") 




#exit application for user
def exit_user():
    exit()

#windows screen

width_of_window=1000
height_of_window=600

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x_coordinate=(screen_width/2) - (width_of_window/2)
y_coordinate=(screen_height/2) - (height_of_window/2)
window.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_coordinate,y_coordinate))

#window.geometry("1000x600")
window.configure(bg = "#d4aa15")


canvas = Canvas(
    window,
    bg = "#d4aa15",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


#set background image
background_img = PhotoImage(file = "images//figma_generated_img.png")
background = canvas.create_image(
  377.5, 295.5,
  image=background_img)
    

#=============Register Frame=========================

def register():
    global ent_name,ent_email,ent_password   
    title=Label(frame2,text="Register Here",
        font=("times now roman",15,"bold",ITALIC),
        bg="#42195c",fg="#eddba4")
    title.place(x=115,y=10)

    name=Label(frame2,text="Enter name:",
        font=("Tomorrow 28",9,"bold",ITALIC),
        bg="#42195c",fg="#d4aa15")
    name.place(x=40,y=45)

    ent_name=Entry(frame2,bg="white",
        fg="black",bd=4, 
        font="Times 22", 
        width=20,
        relief = "groove",)
    ent_name.place(x=40,y=63, 
            height=37)

    email=Label(frame2,text="Enter Email:",
        font=("Tomorrow 28",9,"bold",ITALIC),
        bg="#42195c",fg="#d4aa15")
    email.place(x=40,y=102)

    ent_email=Entry(frame2,bg="white",
        fg="black",bd=4, 
        font="Times 22", 
        width=20,
        relief = "groove",)
    ent_email.place(x=40,y=120,
                height=37)


    password=Label(frame2,text="Create password:",
        font=("Tomorrow 28",9,"bold",ITALIC),
        bg="#42195c",fg="#d4aa15")
    password.place(x=40,y=162)

    ent_password=Entry(frame2,bg="white",
        fg="black",bd=4, 
        font="Times 22", 
        width=20,
        relief = "groove",)
    ent_password.place(x=40,y=180,
                    height=37)


    button_reg=Button(frame2,text="Enter",
    bg="#25ccc6",font="Tomorrow 28 ",
    bd=8,relief=RAISED,
    command=lambda:[insert_reg()],
    cursor="hand2",
    foreground = "red")

    button_reg.place(
    x = 115, y =230,
    width = 120,
    height = 50)

#=============Login Frame===========
frame2=Frame(window,bg="#42195c",relief=RAISED)
frame2.place(x=40,y=214,
        width=380,
        height=310)
def login():
    global ent_email1,ent_password1
    title1=Label(frame2,text="Login Here",
            font=("times now roman",15,"bold",ITALIC),
            bg="#42195c",fg="#eddba4")
    title1.place(x=115,y=10)

    email1=Label(frame2,text="Enter Email:",
            font=("Tomorrow 28",9,"bold",ITALIC),
            bg="#42195c",fg="#d4aa15")
    email1.place(x=40,y=45)

    ent_email1=Entry(frame2,bg="white",
            fg="black",bd=4, 
            font="Times 22", 
            width=20,
            relief = "groove",)
    ent_email1.place(x=40,y=63, 
                height=37)

    password1=Label(frame2,text="Enter password:",
            font=("Tomorrow 28",9,"bold",ITALIC),
            bg="#42195c",fg="#d4aa15")
    password1.place(x=40,y=102)

    ent_password1=Entry(frame2,bg="white",
            fg="black",bd=4, 
            font="Times 22", 
            width=20,
            relief = "groove",)
    ent_password1.place(x=40,y=120,
                    height=37)

    warning=Label(frame2,text="New User? Register First!:",
            font=("Tomorrow 28",9,"bold",ITALIC),
            bg="#42195c",fg="Red")
    warning.place(x=40,y=165)

    button_login=Button(frame2,text="Enter",
        bg="#25ccc6",font="Tomorrow 28 ",
        bd=8,relief=RAISED,
        command=lambda:[fetch_login()],
        cursor="hand2",
        foreground = "red")

    button_login.place(
        x = 110, y =200,
        width = 120,
        height = 50)





#========function for distroying register frame========
def delete_login():
    for item in frame2.winfo_children():
        item.destroy()

#========function for distroying login frame========
def delete_reg():
    for item in frame2.winfo_children():
        item.destroy()

#Login Button
btn2=Button(window,text="Login",
    bg="red",font="Tomorrow 28 ",
    bd=8,relief=RAISED,
    command=lambda:[delete_reg(),login()],
    cursor="hand2",
    foreground = "white")

btn2.place(
    x = 291, y = 104,
    width = 153,
    height = 60)

#Register Button
btn1=Button(window,text="Register",
    bg="red",font="Tomorrow 28 ",
    bd=8,relief=RAISED,
    command=lambda:[delete_login(),register()],
    cursor="hand2",
        foreground = "white")

btn1.place(
    x = 37, y = 104,
    width = 153,
    height = 60)

#Exit Button
btn3=Button(window,text="Exit",
    bg="red",font="Tomorrow 28 ",
    bd=8,relief=RAISED,
    command=exit_user,
    cursor="hand2",
    foreground = "white")

btn3.place(
    x = 532, y = 104,
    width = 153,
    height = 60)


login()
window.mainloop()
