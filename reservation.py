from tkinter import * 
from tkinter import ttk,messagebox 
from tkcalendar import DateEntry 
from database import connect_db 
from datetime import datetime 
class Reservation: 
    def __init__(self,root): 
        self.root=root 
        self.root.geometry("600x600") 
        Label(root,text="Reservation",font=("Arial",22)).pack(pady=10) 
        Label(root,text="Customer Name").pack() 
        self.name=Entry(root) 
        self.name.pack() 
        Label(root,text="Phone").pack() 
        self.phone=Entry(root) 
        self.phone.pack() 
        Label(root,text="State").pack() 
        self.state=ttk.Combobox(root) 
        self.state["values"]=( 
        "Andhra Pradesh","Telangana","Tamil Nadu","Kerala", 
        "Karnataka","Maharashtra","Gujarat","Delhi","Punjab", 
   "Rajasthan","Uttar Pradesh","West Bengal") 
        self.state.pack() 
        Label(root,text="Room Type").pack() 
        self.room_type=ttk.Combobox(root) 
        self.room_type["values"]=("Single","Double","Deluxe","Suite") 
        self.room_type.pack() 
        Label(root,text="Checkin Date").pack() 
        self.checkin=DateEntry(root,date_pattern="yyyy-mm-dd") 
        self.checkin.pack() 
        Label(root,text="Checkout Date").pack() 
        self.checkout=DateEntry(root,date_pattern="yyyy-mm-dd") 
        self.checkout.pack() 
        Label(root,text="Meal").pack() 
        self.meal=Entry(root) 
        self.meal.pack() 
        Button(root,text="Book Room", 
               bg="green", 
               fg="white", 
               command=self.book).pack(pady=20) 
    def book(self): 
        db=connect_db() 
        cursor=db.cursor() 
        room_type=self.room_type.get() 
        cursor.execute( 
        "SELECT room_no,price FROM rooms WHERE room_type=%s AND status='Available' LIMIT 1", 
        (room_type,) 
        )
        room=cursor.fetchone() 
        if room is None: 
            messagebox.showerror("Error","No available rooms") 
            return 
room_no=room[0] 
        price=room[1] 
        checkin=datetime.strptime(self.checkin.get(),"%Y-%m-%d") 
        checkout=datetime.strptime(self.checkout.get(),"%Y-%m-%d") 
        days=(checkout-checkin).days 
        total=days*price 
        cursor.execute(""" 
        INSERT INTO bookings 
        (customer_name,phone,state,room_no,room_type,checkin,checkout,days,total_price,meal) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
        """, 
        ( 
        self.name.get(), 
        self.phone.get(), 
        self.state.get(), 
        room_no, 
        room_type, 
        self.checkin.get(), 
        self.checkout.get(), 
        days, 
        total, 
        self.meal.get() 
        )) 
        cursor.execute( 
        "UPDATE rooms SET status='Booked' WHERE room_no=%s", 
        (room_no,) 
        ) 
        db.commit() 
  messagebox.showinfo( 
        "Success", 
        f"Room {room_no} booked\nBill ₹{total}"
