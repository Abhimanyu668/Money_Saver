from tkinter import *
from PIL import Image,ImageTk
from tkinter.font import ITALIC
window = Tk()
import mysql.connector as mysql
import tkinter.messagebox as messageBox


#title and logo of windows
window.title("MoneySaver")
img=PhotoImage(file='A:\\priceTracker\\images\\logo.png')
window.iconphoto(False,img)


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

background_img = PhotoImage(file = "images/figma_generated_img.png")
background = canvas.create_image(
    377.5, 295.5,
    image=background_img)

#function to jump on home screen
def home_Window():
    window.destroy()
    import main1


def insert_product():
    url=ent.get()
    price=ent1.get()
    con=mysql.connect(host="bttotienkk1dqejaut6j-mysql.services.clever-cloud.com",
            user="uamgwvzwbpd8b6kz",passwd="xCYLrsYFurFUe1T7PCrK",
            database="bttotienkk1dqejaut6j")
    cursor=con.cursor()
    sql="select * from main ORDER BY Serial DESC LIMIT 1"
    cursor.execute(sql)
    email=cursor.fetchone()
    id=email[5]
    #print(id)
    cursor.execute("commit");
    if(url=="" or price==""):
        messageBox.showinfo("Insert status","All fields are required:")
    else:
        con=mysql.connect(host="bttotienkk1dqejaut6j-mysql.services.clever-cloud.com",
            user="uamgwvzwbpd8b6kz",passwd="xCYLrsYFurFUe1T7PCrK",
            database="bttotienkk1dqejaut6j")
        cursor=con.cursor()
        sql="update main set URL=%s,Desirable=%s where Serial=%s"
        cursor.execute(sql,(url,price,id))
        cursor.execute("commit");
        messageBox.showinfo("your app status", "Inserted successfully\n your monotering to the application is successful:")
        con.close();
    
#after login to application Entery for product url
#and price

lbl=Label(window,
        text="URL:"
        ,bd=0,bg="BLUE",
        fg="white",font="Times 15 bold italic")
lbl.place(
        x = 120, y = 135,
        width = 100,
        height = 45)

ent=Entry(window,bg="yellow",
        fg="black",bd=8, 
        font="Times 22", 
        width=40,
        relief = "groove")
ent.place(
        x = 240, y = 135,
        width = 530.0,
        height = 45)

lbl1=Label(window,
        text="Enter ur\n Desirable \nPrice:"
        ,bd=0,bg="BLUE",
        fg="white",font="Times 9 bold italic")
lbl1.place(
        x = 120, y = 207,
        width = 100,
        height = 45)



ent1=Entry(window,bg="yellow",
        fg="black",bd=8, 
        font="Times 22", 
        width=40,
        relief = "groove")
ent1.place(
        x = 240, y = 207,
        width = 150.0,
        height = 45)

btn1=Button(window,text="Start\nMonitring",
        bg="red",font="Tomorrow 15 ",
        bd=8,relief=RAISED,
        command=lambda:[insert_product(),login_page()],
        foreground = "white",
        cursor="hand2")

btn1.place(
        x = 300, y = 320,
        width = 153,
        height = 60)



#===function for fetching login page after entering the start monotering button===
def login_page():
    global ent_name1, ent_email1,ent_password1
    lbl.destroy()
    lbl1.destroy()
    ent.destroy()
    ent1.destroy()
    
    btn1.destroy()
#==========================Login Frame===================
    frame2=Frame(window,bg="#42195c",relief=RAISED)
    frame2.place(x=40,y=214,
        width=380,
        height=310)
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

    password1=Label(frame2,text="Enter Password:",
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

    button_login=Button(frame2,text="Enter",
        bg="#25ccc6",font="Tomorrow 28 ",
        bd=8,relief=RAISED,
        command=lambda:[fetch_login(),insert_main(),product_window()],
        cursor="hand2",
        foreground = "red")

    button_login.place(
        x = 110, y =195,
        width = 153,
        height = 60)



# function for inserting data in main table
def insert_main():
    Email1=ent_email1.get()
    password=ent_password1.get()
    #print(Email1)
    con=mysql.connect(host="bttotienkk1dqejaut6j-mysql.services.clever-cloud.com",
            user="uamgwvzwbpd8b6kz",passwd="xCYLrsYFurFUe1T7PCrK",
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
            user="uamgwvzwbpd8b6kz",passwd="xCYLrsYFurFUe1T7PCrK",
            database="bttotienkk1dqejaut6j")
            cursor=con.cursor()
            cursor.execute("select * from registration where email=%s and password=%s",(ent_email1.get(),ent_password1.get()))
            row=cursor.fetchone()
            if row==None:
                messageBox.showerror("Error","Invalid Email Or password")
            else:
                messageBox.showinfo("Success","welcome")
            cursor.close()
        except Exception as es:
            messageBox.showerror("Error",f"Error due to:{str(es)}") 



#home Button
img =Image.open("A:\\priceTracker\\images\\home_icon.png")
resized_image=img.resize((50,40),Image.ANTIALIAS)
converted_image=ImageTk.PhotoImage(resized_image)
btn2 = Button(window,
    image = converted_image,
    borderwidth = 0,
    highlightthickness = 0,
    command=home_Window,
    cursor="hand2",
    relief = "flat")

btn2.place(
    x = 940, y = 2,
    width = 50,
    height = 40)

#add thumb image
#btn5=Button(window,text="Enter",
 #   bg="red",font="Tomorrow 28 ",
  #  bd=8,relief=RAISED,
   # command=lambda:[print_login()],
    #foreground = "white",
    #cursor="hand2")

    #btn5.place(
   # x = 200, y = 375,
    #width = 153,
    #height = 60)
    # photo=Image.open("A:\\priceTracker\\images\\thumb_man.png")
#resized_image=photo.resize((50,40),Image.ANTIALIAS)
#converted_image=ImageTk.PhotoImage(resized_image)
#lbl=Label(window,
 #       image=converted_image
  #      ,bd=0)
#lbl.place(
 #   x = 300, y = 300,
  #  width = 153,
   # height = 40)


window.mainloop()
