from tkinter import * 
from PIL import Image, ImageTk 
from reservation import Reservation 
from rooms import Rooms 
from billing import Billing 
from checkout import Checkout 
from bookings import Bookings 
from database import connect_db 
IMAGE_PATH = r"C:\Users\ayaan\OneDrive\Desktop\aman" 
class Dashboard: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("BlueBird Hotel Dashboard") 
        self.root.geometry("1400x800") 
        self.root.configure(bg="white") 
        # ===== Sidebar ===== 
        self.sidebar = Frame(self.root, bg="#2c3e50", width=220) 
        self.sidebar.pack(side=LEFT, fill=Y) 
        Label( 
            self.sidebar, 
            text="BlueBird Hotel", 
            bg="#2c3e50", 
            fg="white", 
            font=("Arial", 18, "bold") 
        ).pack(pady=20) 
        Button( 
            self.sidebar, 
            text="Rooms", 
            width=20, 
            command=self.rooms 
 ).pack(pady=8) 
        Button( 
            self.sidebar, 
            text="Reservation", 
            width=20, 
            command=self.reserve 
        ).pack(pady=8) 
        Button( 
            self.sidebar, 
            text="Bookings", 
            width=20, 
            command=self.bookings 
        ).pack(pady=8) 
        Button( 
            self.sidebar, 
            text="Billing", 
            width=20, 
            command=self.billing 
        ).pack(pady=8) 
        Button( 
            self.sidebar, 
            text="Checkout", 
            width=20,     
  command=self.checkout 
        ).pack(pady=8) 
        Button( 
            self.sidebar, 
            text="Logout", 
            width=20, 
            bg="red", 
            fg="white", 
            command=self.logout 
        ).pack(pady=25) 
        # ===== Main Dashboard Area ===== 
        self.main = Frame(self.root, bg="white") 
        self.main.pack(fill=BOTH, expand=True) 
        Label( 
            self.main, 
            text="Dashboard", 
            font=("Arial", 26, "bold"), 
            bg="white" 
        ).pack(pady=20) 
        # ===== Stats Cards ===== 
        stats_frame = Frame(self.main, bg="white") 
        stats_frame.pack(pady=10) 
        self.rooms_card = Label( 
            stats_frame, 
            width=20, 
            height=5, 
            bg="#3498db", 
            fg="white", 
            font=("Arial", 14, "bold") 
        ) 
        self.rooms_card.grid(row=0, column=0, padx=20)   
  self.available_card = Label( 
            stats_frame, 
            width=20, 
            height=5, 
            bg="#2ecc71", 
            fg="white", 
            font=("Arial", 14, "bold") 
        ) 
    self.available_card.grid(row=0, column=1, padx=20) 
        self.bookings_card = Label( 
            stats_frame, 
            width=20, 
            height=5, 
            bg="#e67e22", 
            fg="white", 
            font=("Arial", 14, "bold") 
        ) 
        self.bookings_card.grid(row=0, column=2, padx=20) 
        # ===== Dashboard Image ===== 
        try: 
            bg = Image.open(f"{IMAGE_PATH}\\hotel4.jpg.jpeg") 
            bg = bg.resize((900, 400)) 
            self.bg = ImageTk.PhotoImage(bg) 
            Label( 
                self.main, 
                image=self.bg, 
                bg="white" 
            ).pack(pady=20) 
        except Exception as e: 
            Label( 
                self.main, 
                text=f"Image Error: {e}", 
                bg="white", 
                fg="red" 
            ).pack() 
        # ===== Load stats ===== 
        self.refresh_stats() 
    def refresh_stats(self): 
        db = connect_db() 
   cursor = db.cursor() 
        try: 
            cursor.execute("SELECT COUNT(*) FROM rooms") 
            total_rooms = cursor.fetchone()[0] 
            cursor.execute("SELECT COUNT(*) FROM rooms WHERE status='Available'") 
            available_rooms = cursor.fetchone()[0] 
            cursor.execute("SELECT COUNT(*) FROM bookings") 
            total_bookings = cursor.fetchone()[0] 
            self.rooms_card.config(text=f"Rooms\n{total_rooms}") 
            self.available_card.config(text=f"Available\n{available_rooms}") 
            self.bookings_card.config(text=f"Bookings\n{total_bookings}") 
        except: 
            self.rooms_card.config(text="Rooms\n0") 
            self.available_card.config(text="Available\n0") 
            self.bookings_card.config(text="Bookings\n0") 
        db.close() 
    def rooms(self): 
        room_window = Toplevel(self.root) 
        Rooms(room_window) 
  def reserve(self): 
        reserve_window = Toplevel(self.root) 
        Reservation(reserve_window) 
    def bookings(self): 
        booking_window = Toplevel(self.root) 
        Bookings(booking_window) 
    def billing(self): 
        billing_window = Toplevel(self.root) 
        Billing(billing_window) 
    def checkout(self): 
        checkout_window = Toplevel(self.root) 
        Checkout(checkout_window)     
def logout(self): 
   room login import Login 
        for widget in self.root.winfo_children(): 
            widget.destroy() 
        self.root.geometry("1550x800") 
        Login(self.root) 
