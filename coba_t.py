import tkinter as tk

root = tk.Tk()
root.title("Contoh Tkinter di Sebelah Kiri")

# Membuat widget Text dan meletakkannya di sisi kiri
text_widget = tk.Text(root, height=10, width=30)
text_widget.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()