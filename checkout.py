from tkinter import * 
from tkinter import ttk,messagebox 
from database import connect_db 
class Checkout: 
    def __init__(self,root): 
        self.root=root 
        self.root.geometry("800x400") 
        Label(root,text="Checkout",font=("Arial",22)).pack(pady=10) 
        self.tree=ttk.Treeview(root, 
        columns=("ID","Name","Room","Total"), 
        show="headings") 
        for c in ("ID","Name","Room","Total"): 
            self.tree.heading(c,text=c) 
        self.tree.pack(fill=BOTH,expand=True) 
        Button(root,text="Checkout Customer", 
               bg="red", 
               fg="white", 
              command=self.checkout).pack(pady=10) 
        self.load() 
    def load(self): 
        db=connect_db() 
        cursor=db.cursor() 
        cursor.execute( 
        "SELECT booking_id,customer_name,room_no,total_price FROM bookings" 
        ) 
        rows=cursor.fetchall() 
        for r in rows: 
            self.tree.insert("",END,values=r) 
    def checkout(self): 
        selected=self.tree.focus() 
        if selected=="": 
            return 
        data=self.tree.item(selected)["values"] 
        booking_id=data[0] 
        room_no=data[2] 
  db=connect_db() 
        cursor=db.cursor() 
        cursor.execute( 
        "DELETE FROM bookings WHERE booking_id=%s", 
        (booking_id,) 
        ) 
        cursor.execute( 
        "UPDATE rooms SET status='Available' WHERE room_no=%s", 
        (room_no,) 
        ) 
        db.commit() 
        messagebox.showinfo("Success","Customer checked out") 
        self.tree.delete(selected)
