from tkinter import * 
from tkinter import ttk,messagebox 
from database import connect_db 
class Bookings: 
    def __init__(self,root): 
        self.root=root 
        self.root.geometry("1100x550") 
        self.root.title("Booking Details") 
        Label(root, 
              text="All Bookings", 
              font=("Arial",20,"bold")).pack(pady=10) 
        columns=("ID","Name","Phone","State","Room No", 
                 "Room Type","Checkin","Checkout","Days", 
                 "Total","Meal") 
        self.tree=ttk.Treeview(root, 
                               columns=columns, 
                               show="headings") 
        for col in columns: 
            self.tree.heading(col,text=col) 
            self.tree.column(col,width=100) 
        self.tree.pack(fill=BOTH,expand=True,pady=10) 
        # Cancel Booking Button 
        Button(root, 
               text="Cancel Booking", 
               bg="red", 
               fg="white", 
               font=("Arial",12), 
               command=self.cancel_booking).pack(pady=10)    
 self.load_bookings() 
    # ----------------------------- 
    # Load bookings 
    # ----------------------------- 
    def load_bookings(self): 
        db=connect_db() 
        cursor=db.cursor() 
        cursor.execute("SELECT * FROM bookings") 
        rows=cursor.fetchall() 
        for item in self.tree.get_children(): 
            self.tree.delete(item) 
        for row in rows: 
            self.tree.insert("",END,values=row) 
    # ----------------------------- 
    # Cancel booking 
    # ----------------------------- 
    def cancel_booking(self): 
        selected=self.tree.focus() 
        if selected=="": 
            messagebox.showerror("Error","Select a booking first") 
            return 
        data=self.tree.item(selected)["values"] 
        booking_id=data[0] 
        room_no=data[4] 
        db=connect_db() 
        cursor=db.cursor() 
        # Delete booking 
        cursor.execute( 
        "DELETE FROM bookings WHERE booking_id=%s", 
        (booking_id,) 
        ) 
        # Make room available again 
        cursor.execute( 
        "UPDATE rooms SET status='Available' WHERE room_no=%s", 
        (room_no,) 
        ) 
        db.commit() 
        messagebox.showinfo("Success","Booking cancelled") 
        self.load_bookings()
