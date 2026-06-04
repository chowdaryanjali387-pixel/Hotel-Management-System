from tkinter import * 
from tkinter import ttk, messagebox 
from database import connect_db 
class Rooms: 
    def __init__(self, root): 
        self.root = root 
        self.root.geometry("750x500") 
        self.root.title("Room Management") 
        Label(root,text="Room Management",font=("Arial",22)).pack(pady=10) 
        frame = Frame(root) 
        frame.pack(pady=10) 
        # Room Number 
        Label(frame,text="Room No").grid(row=0,column=0,padx=10,pady=5) 
        self.room_no = Entry(frame) 
        self.room_no.grid(row=0,column=1) 
        # Room Type 
        Label(frame,text="Room Type").grid(row=1,column=0,padx=10,pady=5) 
        self.room_type = ttk.Combobox(frame) 
 self.room_type["values"] = ("Single","Double","Deluxe","Suite") 
        self.room_type.grid(row=1,column=1) 
        # Price 
        Label(frame,text="Price").grid(row=2,column=0,padx=10,pady=5) 
        self.price = Entry(frame) 
        self.price.grid(row=2,column=1) 
 # Status 
        Label(frame,text="Status").grid(row=3,column=0,padx=10,pady=5) 
        self.status = ttk.Combobox(frame) 
        self.status["values"] = ("Available","Booked") 
        self.status.grid(row=3,column=1) 
        # Buttons 
        Button(frame,text="Add Room", 
               bg="green", 
               fg="white", 
               command=self.add_room).grid(row=4,column=0,pady=10) 
        Button(frame,text="Update Price", 
               bg="blue", 
               fg="white", 
               command=self.update_price).grid(row=4,column=1) 
        Button(frame,text="Delete Room", 
               bg="red", 
               fg="white", 
               command=self.delete_room).grid(row=4,column=2) 
        # Table 
        self.tree = ttk.Treeview(root, 
        columns=("ID","Room No","Type","Price","Status"), 
        show="headings") 
        self.tree.heading("ID",text="ID") 
        self.tree.heading("Room No",text="Room No") 
        self.tree.heading("Type",text="Type") 
        self.tree.heading("Price",text="Price") 
        self.tree.heading("Status",text="Status") 
        self.tree.pack(fill=BOTH,expand=True,pady=20) 
        self.load_rooms() 
    # ----------------------------- 
    # Load Rooms 
    # ----------------------------- 
 def load_rooms(self): 
        db = connect_db() 
        cursor = db.cursor() 
        cursor.execute("SELECT * FROM rooms") 
        rows = cursor.fetchall() 
        for item in self.tree.get_children(): 
            self.tree.delete(item) 
        for row in rows: 
            self.tree.insert("",END,values=row) 
    # ----------------------------- 
    # Add Room 
    # ----------------------------- 
    def add_room(self): 
        if self.room_no.get()=="" or self.room_type.get()=="": 
            messagebox.showerror("Error","Fill all fields") 
            return 
        db = connect_db() 
        cursor = db.cursor() 
        cursor.execute( 
        "INSERT INTO rooms(room_no,room_type,price,status) VALUES(%s,%s,%s,%s)", 
        ( 
        self.room_no.get(), 
        self.room_type.get(), 
        self.price.get(), 
        self.status.get() 
        )) 
        db.commit() 
   messagebox.showinfo("Success","Room added") 
        self.load_rooms() 
    # ----------------------------- 
    # Delete Room 
    # ----------------------------- 
    
 def delete_room(self): 
        selected = self.tree.focus() 
        if selected == "": 
            messagebox.showerror("Error","Select a room") 
            return 
        data = self.tree.item(selected) 
        room_id = data["values"][0] 
        db = connect_db() 
        cursor = db.cursor() 
        cursor.execute( 
        "DELETE FROM rooms WHERE room_id=%s", 
        (room_id,) 
        ) 
        db.commit() 
        messagebox.showinfo("Deleted","Room deleted") 
        self.load_rooms() 
    # ----------------------------- 
    # Update Price 
    # ----------------------------- 
    def update_price(self): 
        selected = self.tree.focus() 
        if selected == "": 
            messagebox.showerror("Error","Select a room") 
            return 
        if self.price.get()=="":      
   messagebox.showerror("Error","Enter new price") 
            return 
        data = self.tree.item(selected) 
        room_id = data["values"][0] 
        db = connect_db() 
        cursor = db.cursor()     
   cursor.execute( 
        "UPDATE rooms SET price=%s WHERE room_id=%s", 
        ( 
        self.price.get(), 
        room_id 
        )) 
        db.commit() 
        messagebox.showinfo("Updated","Price updated") 
        self.load_rooms()
