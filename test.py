import tkinter as tk

# Hàm sẽ được gọi khi nút được nhấn
def on_button_click():
    label.config(text="Nút đã được nhấn!")

# Tạo cửa sổ chính của ứng dụng
root = tk.Tk()
root.title("Ứng dụng với Nút")

# Tạo một nhãn (label) để hiển thị thông tin
label = tk.Label(root, text="Chưa nhấn nút.")
label.pack()

# Tạo một nút và gắn hàm vào nút đó
button = tk.Button(root, text="Nhấn tôi", command=on_button_click)
button.pack()

# Chạy vòng lặp chính của Tkinter
root.mainloop()
