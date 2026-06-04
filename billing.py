from tkinter import * 
from tkinter import messagebox 
from PIL import Image, ImageTk 
from database import connect_db 
from dashboard import Dashboard 
IMAGE_PATH = r"C:\Users\ayaan\OneDrive\Desktop\aman" 
class Login: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("BlueBird Hotel Login") 
        self.root.geometry("1550x800") 
        self.show_login() 
    def show_login(self): 
        # Clear existing widgets 
        for widget in self.root.winfo_children(): 
            widget.destroy() 
        bg = Image.open(f"{IMAGE_PATH}\\login.jpg.jpeg") 
        bg = bg.resize((775,800)) 
        self.bg = ImageTk.PhotoImage(bg) 
        Label(self.root,image=self.bg).place(x=0,y=0,width=775,height=800) 
        frame = Frame(self.root,bg="white") 
        frame.place(x=775,y=0,width=775,height=800) 
        Label(frame,text="Admin Login", 
              font=("Arial",20)).pack(pady=20) 
        self.user = Entry(frame,font=("Arial",14)) 
    self.user.pack(pady=10) 
        self.password = Entry(frame,font=("Arial",14),show="*") 
        self.password.pack(pady=10) 
        Button(frame,text="Login", 
               command=self.login, 
               bg="blue", 
               fg="white", 
               font=("Arial",14)).pack(pady=20) 
    def login(self): 
        db = connect_db() 
        cursor = db.cursor() 
        cursor.execute( 
            "SELECT * FROM admin WHERE admin_id=%s AND password=%s", 
            (self.user.get(), self.password.get()) 
        ) 
        result = cursor.fetchone() 
        if result: 
            # Clear login page 
            for widget in self.root.winfo_children(): 
                widget.destroy() 
            # Resize root for dashboard 
            self.root.geometry("1400x800") 
            # Load dashboard in SAME root 
            Dashboard(self.root) 
        else: 
            messagebox.showerror("Error","Invalid Login") 
