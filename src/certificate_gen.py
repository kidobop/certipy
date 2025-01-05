import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import csv

class Generate_Certificates:
    def __init__(self, master):
        self.master = master
        self.master.title("Certipy")
        self.master.geometry("1200x800")
        self.master.config(bg="#272727")

        self.button_frame = tk.Frame(self.master, bg="#272727")
        self.button_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=15)

        self.upload_button = tk.Button(self.button_frame, text="Upload Image", command=self.upload_image, relief="flat", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), padx=15, pady=10, activebackground="#45a049")
        self.upload_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(self.button_frame, text="Clear Image", command=self.clear_boxes, state=tk.DISABLED, relief="flat", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), padx=15, pady=10, activebackground="#45a049")
        self.clear_button.pack(side=tk.LEFT, padx=10)

        self.uploadcsv_button = tk.Button(self.button_frame, text="Upload CSV", command=self.upload_csv, relief="flat", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), padx=15, pady=10, activebackground="#45a049")
        self.uploadcsv_button.pack(side=tk.LEFT, padx=10)

        self.generate_bulk_button = tk.Button(self.button_frame, text="Generate Bulk Certificates", relief="flat", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), padx=15, pady=10, activebackground="#45a049")
        self.generate_bulk_button.pack(side=tk.LEFT, padx=10)

        self.canvas = tk.Canvas(self.master, bg="#292929")
        self.canvas.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        self.start_x = None
        self.start_y = None
        self.current_rectangle = None
        self.rectangles = []

        self.coordinate_frame = tk.Frame(self.master, bg="#282828")
        self.coordinate_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=0)
        
        self.coordinate_label = tk.Label(self.coordinate_frame, text="Bounding Boxes", bg="#292929", font=("Helvetica", 14, "bold"))
        self.coordinate_label.pack(side=tk.TOP, padx=10)
        self.coordinate_listbox = tk.Listbox(self.coordinate_frame, height=5, font=("Helvetica", 12), bg="#272727", fg="white",
                                             selectmode=tk.SINGLE, bd=0, highlightthickness=0, activestyle="none", relief="flat")
        self.coordinate_listbox.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.scrollbar = tk.Scrollbar(self.coordinate_listbox)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.coordinate_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.coordinate_listbox.yview)

        self.csv_labels_frame = tk.Frame(self.coordinate_frame, bg="#282828")
        self.csv_labels_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.csv_label_1 = tk.Label(self.csv_labels_frame, text="", bg="#282828", fg="white", font=("Helvetica", 12))
        self.csv_label_1.pack(side=tk.TOP, fill=tk.X)

        self.csv_label_2 = tk.Label(self.csv_labels_frame, text="", bg="#282828", fg="white", font=("Helvetica", 12))
        self.csv_label_2.pack(side=tk.TOP, fill=tk.X)

        self.canvas.bind("<ButtonPress-1>", self.start_box)
        self.canvas.bind("<B1-Motion>", self.draw_box)
        self.canvas.bind("<ButtonRelease-1>", self.end_box)

        self.csv_data = []

    def upload_csv(self):
        ftypes = [("CSV Files", "*.csv")]
        csv_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=ftypes)
        if not csv_path:
            return

        with open(csv_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            self.csv_data = rows 

            if len(rows) > 0:
                self.csv_label_1.config(text=f"Row 1: {', '.join(rows[0])}")
            else:
                self.csv_label_1.config(text="Row 1: No data found.")

            if len(rows) > 1:
                self.csv_label_2.config(text=f"Row 2: {', '.join(rows[1])}")
            else:
                self.csv_label_2.config(text="Row 2: No data found.")

    def upload_image(self):
        ftypes = [("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm"), ("All files", "*.*")]
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=ftypes)
        if not file_path:
            return
        self.clear_boxes()
        self.original_image = Image.open(file_path)
        canvas_width = self.canvas.winfo_width() or 1000
        canvas_height = self.canvas.winfo_height() or 70
        img_ratio = self.original_image.width / self.original_image.height
        canvas_ratio = canvas_width / canvas_height
        if img_ratio > canvas_ratio:
            new_width = min(self.original_image.width, canvas_width)
            new_height = int(new_width / img_ratio)
        else:
            new_height = min(self.original_image.height, canvas_height)
            new_width = int(new_height * img_ratio)
        resized_image = self.original_image.resize((new_width, new_height), Image.LANCZOS)
        self.displayed_image = ImageTk.PhotoImage(resized_image)
        self.canvas.delete("all")
        self.canvas_image = self.canvas.create_image(
            canvas_width // 2,
            canvas_height // 2,
            image=self.displayed_image,
            anchor=tk.CENTER)
        self.clear_button.config(state=tk.NORMAL)

    def start_box(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.current_rectangle = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red", width=2)
    
    def draw_box(self, event):
        curX, curY = event.x, event.y
        self.canvas.coords(self.current_rectangle, self.start_x, self.start_y, curX, curY)

    def end_box(self, event):
        coords = self.canvas.coords(self.current_rectangle)
        x1, y1, x2, y2 = [int(coord) for coord in coords]
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        self.rectangles.append((x1, y1, x2, y2))
        self.coordinate_listbox.insert(tk.END, f"Box {len(self.rectangles)}: ({x1}, {y1}) - ({x2}, {y2})")
        self.current_rectangle = None

    def clear_boxes(self):
        for rect in self.canvas.find_all():
            if rect != getattr(self, 'canvas_image', None):
                self.canvas.delete(rect)
        self.rectangles.clear()
        self.coordinate_listbox.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = Generate_Certificates(root)
    root.mainloop()

if __name__ == "__main__":
    main()
