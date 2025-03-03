import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class ShopGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Shop GUI")
        self.root.geometry("1000x600")

        # Top Navigation Bar
        nav_frame = tk.Frame(root, bg="#2E2E2E", height=50)
        nav_frame.pack(fill="x")

        tk.Label(nav_frame, text="Products", fg="#B28DFF", bg="#2E2E2E", font=("Arial", 14, "bold")).pack(side="right", padx=20)
        tk.Label(nav_frame, text="Contact", fg="#B28DFF", bg="#2E2E2E", font=("Arial", 14, "bold")).pack(side="right", padx=20)

        # Sidebar for Categories
        sidebar = tk.Frame(root, bg="#D8A6A6", width=200)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="Product Type:", bg="#D8A6A6", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=10)
        tk.Button(sidebar, text="Monitor", bg="#AAA", font=("Arial", 12)).pack(fill="x", padx=10, pady=5)
        tk.Button(sidebar, text="Windows", bg="#9B6A6A", font=("Arial", 12)).pack(fill="x", padx=10, pady=5)

        # Main Content Frame
        content_frame = tk.Frame(root, bg="#F5F5F5")
        content_frame.pack(expand=True, fill="both")

        # Search Bar and Sorting
        search_sort_frame = tk.Frame(content_frame, bg="#F5F5F5")
        search_sort_frame.pack(fill="x", pady=10)

        search_entry = tk.Entry(search_sort_frame, width=50)
        search_entry.pack(side="left", padx=10)

        sort_label = tk.Label(search_sort_frame, text="Sort by:", bg="#F5F5F5")
        sort_label.pack(side="left", padx=10)

        sort_options = ttk.Combobox(search_sort_frame, values=["Price", "Name", "Rating"], state="readonly")
        sort_options.pack(side="left", padx=10)

        # Product Grid
        product_frame = tk.Frame(content_frame, bg="#FFFFFF")
        product_frame.pack(pady=10)

        products = [
            ("Dell S2719DGF", "image/dell-monitor.png"),
            ("Asus PB278Q", "image/asus.jpg"),
            ("LG 25UM58-P", "image/lg.jpg"),
            ("Samsung Odyssey Neo G8", "image/samsung.png"),
        ]

        for i, (name, img_path) in enumerate(products):
            frame = tk.Frame(product_frame, relief="solid", borderwidth=1)
            frame.grid(row=0, column=i, padx=10)

            # Open the image file using PIL
            img = Image.open(img_path)
            img = img.resize((150, 150))  # Resize the image if needed
            img = ImageTk.PhotoImage(img)

            img_label = tk.Label(frame, image=img)
            img_label.image = img  # Keep a reference to avoid garbage collection
            img_label.pack()

            tk.Label(frame, text=name, font=("Arial", 10)).pack()

        # Come Back Button
        back_button = tk.Button(root, text="Come Back", font=("Arial", 12), bg="#E0E0E0")
        back_button.pack(pady=20)

        # Footer
        footer = tk.Frame(root, bg="#2E2E2E", height=50)
        footer.pack(fill="x", side="bottom")

        tk.Label(footer, text="Terms & Conditions", fg="#FFFFFF", bg="#2E2E2E").pack()
        tk.Label(footer, text="© 2025 Programming Club Society: Design by our Team", fg="#FFFFFF", bg="#2E2E2E").pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = ShopGUI(root)
    root.mainloop()
