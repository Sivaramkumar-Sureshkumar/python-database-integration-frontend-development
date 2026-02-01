import tkinter as tk
import sqlite3
from tkinter import messagebox
import mysql.connector as mycon
from tkinter import *
import random
import string
con=mycon.connect(host="localhost",user="root",passwd="sivaramkumar",database="srkbooking")
cur=con.cursor()
"""cur.execute("create database srk")"""
cur.execute("use srkbooking")
"""cur.execute("create table login(username varchar(10),password varchar(30),hint varchar(10)")"""
root=tk.Tk()
root.title("AI BOOK MENTOR")
root.geometry("400x400")
root.configure(bg="#5e0038")
label_1=Label(root,text="WELCOME",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
label_2=Label(root,text="TO",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
label_3=Label(root,text="AI BOOK MENTOR",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()

def payment():
    def process_payment():
        card_number = entry_card_number.get()
        expiry_date = entry_expiry_date.get()
        cvv = entry_cvv.get()
        if card_number == "" or expiry_date == "" or cvv == "":
            messagebox.showerror("Error", "Please fill in all the fields")
        else:
            messagebox.showinfo("Payment Successful", "Payment has been processed successfully!")
    payment = tk.Tk()
    payment.title("SRK BOOKING -PAYMENT INTERFACE")
    payment.geometry("400x400")
    payment.configure(bg="#5e0038")
    label_card_number = tk.Label(payment, text="Card Number:",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB")
    label_expiry_date = tk.Label(payment, text="Expiry Date:",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB")
    label_cvv = tk.Label(payment, text="CVV:",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB")
    entry_card_number = tk.Entry(payment)
    entry_expiry_date = tk.Entry(payment)
    entry_cvv = tk.Entry(payment, show="*")
    button_payment = tk.Button(payment, text="Process Payment", command=process_payment)
    label_card_number.grid(row=0, column=0, padx=10, pady=10)
    entry_card_number.grid(row=0, column=1, padx=10, pady=10)
    label_expiry_date.grid(row=1, column=0, padx=10, pady=10)
    entry_expiry_date.grid(row=1, column=1, padx=10, pady=10)
    label_cvv.grid(row=2, column=0, padx=10, pady=10)
    entry_cvv.grid(row=2, column=1, padx=10, pady=10)
    button_payment.grid(row=3, columnspan=2, padx=10, pady=20)
def error0():
    error0=tk.Tk()
    error0.title("SRK BOOKING- ACCOUNT ACCESS DENIED")
    error0.geometry("400x400")
    error0.configure(bg="#5e0038")
    name_user=Label(error0,text="ERROR , ACCESS DENIED",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    b4=Button(error0,text="RETURN TO MAIN PAGE",font=("Arial Black",20),bg="#A94064",fg="#022D36")
    b4.pack()
    b4.config(command=button_1)
def createnew():
    createnew=tk.Tk()
    createnew.title("SRK BOOKING- CREATING NEW PASSWORD")
    createnew.geometry("400x400")
    createnew.configure(bg="#5e0038")
    name_user=Label(createnew,text="YOUR USERNAME",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    print_user=Label(createnew,text="hello",font=("Arial Black",20),bg="#5e0038",fg="#019799").pack()
def forgot_password():
    def validate_fields5():
        if entry_1.get() == "":
            messagebox.showerror("ERROR","USERNAME IS UNFILLED!")
        elif entry_2.get() == "":
            messagebox.showerror("ERROR","CERTAIN FIELD IS UNFILLED")
        elif entry_1.get() and entry_2.get()!= "":
            a=entry_1.get()
            cod="select hint_password from logininfo where username="+str(a)
            print(cod)
            cur.execute(cod)
            X=cur.fetchall()
            if X == entry_1.get():
                b1.config(command=createnew)
            else:
                b1.config(command=error0)
    forgot_password=tk.Tk()
    forgot_password.title("SRK BOOKING- FORGOT PASSWORD")
    forgot_password.geometry("400x400")
    forgot_password.configure(bg="#5e0038")
    name_user=Label(forgot_password,text="ENTER USERNAME",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    entry_1=Entry(forgot_password,width=60,font=("Arial Black",20))
    entry_1.focus_set()
    entry_1.pack()
    hint=Label(forgot_password,text="ENTER YOUR FAVOURITE PLACE NAME",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    entry_2=Entry(forgot_password,width=60,font=("Arial Black",20))
    entry_2.focus_set()
    entry_2.pack()
    b1=Button(forgot_password,text="NEXT",font=("Arial Black",20),bg="green",fg="black")
    b1.pack()
    b1.config(command=validate_fields5)
def airlines():
    airlines=tk.Tk()
    airlines.title("SRK AIRLINES BOOKING")
    airlines.geometry("400x400")
    airlines.configure(bg="#5e0038")
    Label_15=Label(airlines,text="SRK AIRLINES BOOKING",font=("Arial Black",30),bg="#5e0038",fg="#F19CBB").pack()
    b15=Button(airlines,text="BOOK TICKET",font=("Arial Black",20),bg="#5a868f",fg="#a60077")
    b15.pack()
    b15.config(command=airlines_book)
    b16=Button(airlines,text="CANCEL TICKET",font=("Arial Black",20),bg="#5a868f",fg="#a60077")
    b16.pack()
    b16.config(command=airlines_cancel)
    b17=Button(airlines,text="TICKET DETAILS",font=("Arial Black",20),bg="#5a868f",fg="#a60077")
    b17.pack()
    b17.config(command=airlines_tkdetails)
def userdet():
    userdet=tk.Tk()
    userdet.title("SRK BUS BOOKING - CANCEL TICKETS CONFIRMATION")
    userdet.geometry("400x400")
    userdet.configure(bg="#5e0038")
def canceltk():
    canceltk=tk.Tk()
    canceltk.title("SRK BUS BOOKING - CANCEL TICKETS")
    canceltk.geometry("400x400")
    canceltk.configure(bg="#5e0038")
    Label_11=Label(canceltk,text="SRK BUS BOOKING",font=("Arial Black",30),bg="#5e0038",fg="#F19CBB").pack()
    Label_12=Label(canceltk,text="ENTER THE TICKET ID",font=("Arial Black",25),bg="#5e0038",fg="#F19CBB").pack()
    entry_1=Entry(canceltk,width=60,font=("Arial Black",20))
    entry_1.focus_set()
    entry_1.pack()
    b7=Button(canceltk,text="SUBMIT",font=("Arial Black",20),bg="green",fg="black")
    b7.pack()
    b7.config(command=userdet)
def error_2():
        error_2=tk.Tk()
        error_2.title("ERROR OCCURED")
        error_2.geometry("400x400")
        error_2.configure(bg="#00B0BA")
        Label_10=Label(error_2,text="SRK BOOKING",font=("Arial Black",25),bg="#00B0BA",fg="Black").pack()
        Label_11=Label(error_2,text="ERROR OCCURED DUE TO ANY OF THESE BELOW \n1.DEPARTURE DATE IS EMPTY \n2.DESTINATION POINT IS EMPTY \n3.PICKUP POINT IS EMPTY OR INCORRECT \n3.AVERAGE DISTANCE IS EMPTY",font=("Arial Black",20),bg="#00B0BA",fg="#022d36").pack()
        b4=Button(error_2,text="RETRY",font=("Arial Black",20),bg="grey",fg="black")
        b4.pack()
        b4.config(command=bus)
def bus():
    def validate_fields3():
        if entry_1.get() == "" or entry_2.get()== "" or entry_3.get() == "" or entry_4.get() == "":
            b5.config(command=error_2)
        else:
            b5.config(command=availablebus)       
    bus=tk.Tk()
    bus.title("AI BOOK MENTOR")
    bus.geometry("400x400")
    bus.configure(bg="#5e0038")
    Label_11=Label(bus,text="WELCOME TO AI BOOK MENTOR",font=("Arial Black",30),bg="#5e0038",fg="#F19CBB").pack()
    Label_12=Label(bus,text="ENTER THE DEPARTURE DATE",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    entry_1=Entry(bus,width=60,font=("Arial Black",20))
    entry_1.focus_set()
    entry_1.pack()
    Label_13=Label(bus,text="ENTER THE DESTINATION POINT",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    entry_2=Entry(bus,width=60,font=("Arial Black",20))
    entry_2.focus_set()
    entry_2.pack()
    Label_14=Label(bus,text="ENTER THE PICKUP POINT",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    entry_3=Entry(bus,width=60,font=("Arial Black",20))
    entry_3.focus_set()
    entry_3.pack()
    Label_15=Label(bus,text="ENTER THE AVERAGE DISTANCE (in Km)",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    entry_4=Entry(bus,width=60,font=("Arial Black",20))
    entry_4.focus_set()
    entry_4.pack()
    b5=Button(bus,text="NEXT",font=("Arial Black",20),bg="green",fg="black")
    b5.pack()
    b5.config(command=validate_fields3)
def ticketdet():
    ticketdet=tk.Tk()
    ticketdet.title("SRK BUS BOOKING - TICKET DETAILS")
    ticketdet.geometry("400x400")
    ticketdet.configure(bg="#5e0038")
    Label_18=Label(ticketdet,text="SRK BUS BOOKING",font=("Arial Black",25),bg="#5e0038",fg="#F19CBB").pack()
    Label_18=Label(ticketdet,text="ENTER THE TICKET ID",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    entry_7=Entry(ticketdet,width=60,font=("Arial Black",20))
    entry_7.focus_set()
    entry_7.pack()
    Label_18=Label(ticketdet,text="ENTER THE NAME OF THE PASSENGER",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    entry_8=Entry(ticketdet,width=60,font=("Arial Black",20))
    entry_8.focus_set()
    entry_8.pack()
    b4=Button(ticketdet,text="SEARCH",font=("Arial Black",20),bg="green",fg="black")
    b4.pack()
    b4.config(command=Ticketdetails)
def busdetails():
    busdetails=tk.Tk()
    busdetails.title("AI BOOK MENTOR- TOPIC CHOOSE")
    busdetails.geometry("400x400")
    busdetails.configure(bg="#5e0038")
    Label_18=Label(busdetails,text="CHOOSE THE DOMAIN YOU ARE INTERESTED IN ?",font=("Arial Black",25),bg="#5e0038",fg="#F19CBB").pack()
    b12=Button(busdetails,text="ARTIFICIAL INTELLIGENCE",font=("Arial Black",20),bg="#019799",fg="#022D36")
    b12.pack()
    b12.config(command=bus)
    b13=Button(busdetails,text="ROBOTICS",font=("Arial Black",20),bg="#019799",fg="#022D36")
    b13.pack()
    b13.config(command=bus)
    b14=Button(busdetails,text="PHYSICS",font=("Arial Black",20),bg="#019799",fg="#022D36")
    b14.pack()
    b14.config(command=bus)
    b14=Button(busdetails,text="ARTS & DESIGN",font=("Arial Black",20),bg="#019799",fg="#022D36")
    b14.pack()
    b14.config(command=bus)
    b14=Button(busdetails,text="MUSIC THEORY",font=("Arial Black",20),bg="#019799",fg="#022D36")
    b14.pack()
    b14.config(command=bus)
    b14=Button(busdetails,text="GEOGRAPHY",font=("Arial Black",20),bg="#019799",fg="#022D36")
    b14.pack()
    b14.config(command=bus)
    b14=Button(busdetails,text="MATHEMATICS",font=("Arial Black",20),bg="#019799",fg="#022D36")
    b14.pack()
    b14.config(command=bus)
def orangecity():
    seat_states=[0]*30
    def book_seat(seat_number):
        if seat_states[seat_number]==0:
            seat_states[seat_number]=1
            btn=seat_buttons[seat_number]
            btn.configure(bg='red',state=tk.DISABLED)
            animate_booking(btn)
    def animate_booking(button):
        for i in range(1,6):
            color='white' if i % 2==0 else 'red'
            button.configure(bg=color)
            button.update()
            button.after(200)
        button.configure(bg='red')
    orangecity=tk.Tk()
    orangecity.title("SRK BUS BOOKING - ORANGECITY")
    orangecity.geometry("400x400")
    orangecity.configure(bg="orange")
    seat_buttons=[]
    for i in range(30):
        row=i // 6
        col=i % 6
        btn=tk.Button(orangecity,text=i+1,width=4,height=2,bg='green',command=lambda seat=i:book_seat(seat))
        btn.grid(row=row,column=col,padx=20,pady=20)
        seat_buttons.append(btn)
def intracity():
    seat_states=[0]*25
    def book_seat(seat_number):
        if seat_states[seat_number]==0:
            seat_states[seat_number]=1
            btn=seat_buttons[seat_number]
            btn.configure(bg='red',state=tk.DISABLED)
            animate_booking(btn)
    def animate_booking(button):
        for i in range(1,6):
            color='white' if i % 2==0 else 'red'
            button.configure(bg=color)
            button.update()
            button.after(200)
        button.configure(bg='red')
        global no_tickets 
        no_tickets=+1 
    intracity=tk.Tk()
    intracity.title("SRK BUS BOOKING - INTRACITY")
    intracity.geometry("400x400")
    intracity.configure(bg="#0D98BA")
    seat_buttons=[]
    for i in range(25):
        row=i // 6
        col=i % 6
        btn=tk.Button(intracity,text=i+1,width=4,height=2,bg='green',command=lambda seat=i:book_seat(seat))
        btn.grid(row=row,column=col,padx=20,pady=20)
        seat_buttons.append(btn)
def kallada():
    seat_states=[0]*25
    def book_seat(seat_number):
        if seat_states[seat_number]==0:
            seat_states[seat_number]=1
            btn=seat_buttons[seat_number]
            btn.configure(bg='red',state=tk.DISABLED)
            animate_booking(btn)
    def animate_booking(button):
        for i in range(1,6):
            color='white' if i % 2==0 else 'red'
            button.configure(bg=color)
            button.update()
            button.after(200)
        button.configure(bg='red')
    kallada=tk.Tk()
    kallada.title("SRK BUS BOOKING - KALLADA")
    kallada.geometry("400x400")
    kallada.configure(bg="#4C0212")
    seat_buttons=[]
    for i in range(25):
        row=i // 6
        col=i % 6
        btn=tk.Button(kallada,text=i+1,width=4,height=2,bg='green',command=lambda seat=i:book_seat(seat))
        btn.grid(row=row,column=col,padx=20,pady=20)
        seat_buttons.append(btn)
def availablebus():
    availablebus=tk.Tk()
    availablebus.title("SRK BUS BOOKING -AVAILABLE BUSES")
    availablebus.geometry("400x400")
    availablebus.configure(bg="#5e0038")
    Label_18=Label(availablebus,text="AVAILABLE BUSES",font=("Arial Black",25),bg="#5e0038",fg="#F19CBB").pack()
    b5=Button(availablebus,text="ORANGE CITY BUS",font=("Arial Black",20),bg="orange",fg="Black")
    b5.pack()
    b5.config(command=orangecity)
    b6=Button(availablebus,text="INTRACITY BUS",font=("Arial Black",20),bg="#0D98BA",fg="Black")
    b6.pack()
    b6.config(command=intracity)
    b7=Button(availablebus,text="KALLADA BUS",font=("Arial Black",20),bg="#4C0212",fg="Black")
    b7.pack()
    b7.config(command=kallada)
def newwindow_2():
    newwindow_2=tk.Tk()
    newwindow_2.title("AI BOOK MENTOR- USER LEVEL")
    newwindow_2.geometry("400x400")
    newwindow_2.configure(bg="#5e0038")
    Label_9=Label(newwindow_2,text="AI BOOK MENTOR",font=("Arial Black",25),bg="#5e0038",fg="#F19CBB").pack()
    Label_10=Label(newwindow_2,text="LOGGED IN SUCCESSFULLY !",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    b3=Button(newwindow_2,text="BEGINNER",font=("Arial Black",20),bg="#019799",fg="#022D36")
    b3.pack()
    b3.config(command=busdetails)
    b4=Button(newwindow_2,text="INTERMEDIATE",font=("Arial Black",20),bg="#019799",fg="#022D36")
    b4.pack()
    b4.config(command=busdetails)
    b5=Button(newwindow_2,text="ADVANCED",font=("Arial Black",20),bg="#019799",fg="#022D36")
    b5.config(command=busdetails)
    b5.pack()
    
def error_1():
        error_1=tk.Tk()
        error_1.title("ERROR OCCURED")
        error_1.geometry("400x400")
        error_1.configure(bg="#00B0BA")
        Label_10=Label(error_1,text="AI BOOK MENTOR",font=("Arial Black",25),bg="#00B0BA",fg="Black").pack()
        Label_11=Label(error_1,text="ERROR OCCURED DUE TO ANY OF THESE BELOW \n1.USERNAME FIELD IS EMPTY \n2.PASSWORD FIELD IS EMPTY \n3.CAPTCHA IS EMPTY OR INCORRECT",font=("Arial Black",20),bg="#00B0BA",fg="#022d36").pack()
        b4=Button(error_1,text="RETRY",font=("Arial Black",20),bg="grey",fg="black")
        b4.pack()
        b4.config(command=button_1)
def button_1():
    def validate_fields1():
        if entry_1.get() == "" or entry_2.get() == "" or entry_5.get() == "":
            b4.config(command=error_1)
        elif entry_1.get()!="" and entry_2.get()!= "" and entry_3.get()!="":
            t=(entry_1.get(),entry_2.get(),entry_3.get())
            cur.execute("insert into logininfo values"+str(t))
            con.commit()
            b4.config(command=newwindow_2)
    from tkinter import ttk
    from tkinter import messagebox
    button_1=tk.Tk()
    button_1.title("SIGN UP")
    button_1.geometry("400x400")
    button_1.configure(bg="#00B0BA")
    Label_10=Label(button_1,text="AI BOOK MENTOR",font=("Arial Black",25),bg="#00B0BA",fg="#022D36").pack()
    Label_11=Label(button_1,text="ENTER THE NAME OF THE USER",font=("Arial Black",20),bg="#00B0BA",fg="#022d36")
    Label_11.place(x=50,y=50)
    entry_1=Entry(button_1,width=30,font=("Arial Black",20))
    entry_1.place(x=50,y=100)
    Label_11=Label(button_1,text="ENTER THE NEW PASSWORD (minimum 8 characters)",font=("Arial Black",20),bg="#00B0BA",fg="#022d36")
    Label_11.place(x=50,y=150)
    entry_2=Entry(button_1,width=30,show="*",font=("Arial Black",20))
    entry_2.place(x=50,y=200)
    def generate_captcha():
        captcha_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        captcha_label.config(text=captcha_str)
    captcha_label = Label(button_1,width=10, font=("Arial Black", 20))
    generate_button=Button(button_1, text="GENERATE CAPTCHA",font=("Arial Black",20),bg="#a3152d",fg="white")
    captcha_label.place(x=100,y=250)
    generate_button.config(command=generate_captcha)
    generate_button.place(x=500,y=250)
    captcha=Label(button_1,text="ENTER CAPTCHA HERE",font=("Arial Black",20),bg="#00B0BA",fg="#022D36")
    captcha.place(x=50,y=300)
    entry_5=Entry(button_1,width=30,font=("Arial Black",20))
    entry_5.place(x=50,y=350)
    Label_12=Label(button_1,text="HINT (for password recovery) ENTER YOUR FAVOURITE PLACE NAME",font=("Arial Black",20),bg="#00B0BA",fg="#022d36")
    Label_12.place(x=50,y=400)
    entry_3=Entry(button_1,width=30,font=("Arial Black",20))
    entry_3.place(x=50,y=450)
    b4=Button(button_1,text="SUBMIT",font=("Arial Black",20),bg="green",fg="black")
    b4.place(x=600,y=500)
    b4.config(command=validate_fields1)
def button_2():
    def validate_fields2():
        if entry_1.get() == "":
            messagebox.showerror("ERROR","USERNAME IS UNFILLED!")
        elif entry_2.get() == "":
            messagebox.showerror("ERROR","PASSWORD IS UNFILLED!")
        elif entry_3.get() == "":
            messagebox.showerror("ERROR","CAPTCHA IS UNFILLED!")
        else:
            b4.config(command=newwindow_2)
    from tkinter import ttk
    button_2=tk.Tk()
    button_2.title("LOGIN")
    button_2.geometry("400x400")
    button_2.configure(bg="#5e0038")
    Label_20=Label(button_2,text="AI BOOK MENTOR",font=("Arial Black",25),bg="#5e0038",fg="#F19CBB").pack()
    name_user=Label(button_2,text="ENTER USERNAME",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    entry_1=Entry(button_2,width=60,font=("Arial Black",20))
    entry_1.focus_set()
    entry_1.pack()
    password_2=Label(button_2,text="ENTER PASSWORD",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    entry_2=Entry(button_2,width=60,show="*",font=("Arial Black",20))
    entry_2.focus_set()
    entry_2.pack()
    def generate_captcha():
        captcha_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        captcha_label.config(text=captcha_str)
    captcha_label = Label(button_2,width=10, font=("Arial Black", 20))
    generate_button = Button(button_2, text="Generate CAPTCHA",font=("Arial Black",20),bg="#019799",fg="#022D36")
    captcha_label.pack()
    generate_button.config(command=generate_captcha)
    generate_button.pack()
    captcha=Label(button_2,text="ENTER CAPTCHA HERE",font=("Arial Black",20),bg="#5e0038",fg="#F19CBB").pack()
    entry_3=Entry(button_2,width=60,font=("Arial Black",20))
    entry_3.focus_set()
    entry_3.pack()
    b4=Button(button_2,text="SUBMIT",font=("Arial Black",20),bg="#A94064",fg="#022D36")
    b4.pack()
    b4.config(command=validate_fields2)
    b3=Button(button_2,text="Forgot Password ?",width=20,font=("Arial Black",20),bg="#019799",fg="#022D36")
    b3.pack()
    b3.config(command=forgot_password)
def availableairlines():
    availableairlines=tk.Tk()
    availableairlines.title("SRK AIRLINES BOOKING")
    availableairlines.geometry("400x400")
    availableairlines.configure(bg="#5e0038")
    Label_20=Label(availableairlines,text="SRK AIRLINES BOOKING",font=("Arial Black",25),bg="#5e0038",fg="#F19CBB").pack()
    Label_21=Label(availableairlines,text="AVAILABLE AIRLINES",font=("Arial Black",25),bg="#5e0038",fg="#F19CBB").pack()
def airbook():
    airbook=tk.Tk()
    airbook.title("SRK AIRLINES BOOKING")
    airbook.geometry("400x400")
    airbook.configure(bg="#019799")
    def validate_fields4():
        if entry_1.get() == "":
            messagebox.showerror("ERROR","DEPARTURE DATE IS UNFILLED!")
        elif entry_2.get() == "":
            messagebox.showerror("ERROR","DESTINATION PLACE IS UNFILLED!")
        elif entry_3.get() == "":
            messagebox.showerror("ERROR","DEPARTURE PLACE IS UNFILLED!")
        else:
            b5.config(command=availableairlines)
    Label_20=Label(airbook,text="SRK AIRLINES BOOKING",font=("Arial Black",25),bg="#019799",fg="#001718").pack()
    Label_12=Label(airbook,text="ENTER THE DEPARTURE DATE",font=("Arial Black",20),bg="#019799",fg="#001718").pack()
    entry_1=Entry(airbook,width=60,font=("Arial Black",20))
    entry_1.focus_set()
    entry_1.pack()
    Label_13=Label(airbook,text="ENTER THE DESTINATION PLACE",font=("Arial Black",20),bg="#019799",fg="#001718").pack()
    entry_2=Entry(airbook,width=60,font=("Arial Black",20))
    entry_2.focus_set()
    entry_2.pack()
    Label_14=Label(airbook,text="ENTER THE DEPARTURE PLACE",font=("Arial Black",20),bg="#019799",fg="#001718").pack()
    entry_3=Entry(airbook,width=60,font=("Arial Black",20))
    entry_3.focus_set()
    entry_3.pack()
    b5=Button(airbook,text="NEXT",font=("Arial Black",20),bg="green",fg="black")
    b5.pack()
    b5.config(command=validate_fields4)
def airlines():
    airlines=tk.Tk()
    airlines.title("SRK AIRLINES BOOKING")
    airlines.geometry("400x400")
    airlines.configure(bg="#019799")
    Label_20=Label(airlines,text="SRK AIRLINES BOOKING",font=("Arial Black",25),bg="#019799",fg="#001718").pack()
    b12=Button(airlines,text="BOOK TICKET",font=("Arial Black",20),bg="#019799",fg="#001718")
    b12.pack()
    b12.config(command=airbook)
    b13=Button(airlines,text="CHECK TICKET DETAILS",font=("Arial Black",20),bg="#019799",fg="#001718")
    b13.pack()
    b13.config(command=airdet)
    b14=Button(airlines,text="CANCEL TICKET",font=("Arial Black",20),bg="#019799",fg="#001718")
    b14.pack()
    b14.config(command=cancelair)    
root.geometry("200x100")
b1=Button(root,text="NEW USER (SIGN UP)",width=20,font=("Arial Black",20),bg="#019799",fg="#022D36")
b1.place(x=470,y=400)
b1.config(command=button_1)
b2=Button(root,text="EXISTING USER (SIGN IN)",width=20,font=("Arial Black",20),bg="#019799",fg="#022D36")
b2.place(x=470,y=500)
b2.config(command=button_2) 
