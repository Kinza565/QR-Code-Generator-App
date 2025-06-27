import qrcode
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# 💻 Create Window
root = Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.config(bg="white")

# 🏷️ Heading
Label(root, text="QR Code Generator", font="Arial 20 bold", bg="white").pack(pady=10)

# 🔗 Entry for data
Label(root, text="Enter Text or URL", font="Arial 12", bg="white").pack(pady=5)
data_entry = Entry(root, width=40, font="Arial 12")
data_entry.pack(pady=5)

# 📝 Entry for file name
Label(root, text="Enter File Name", font="Arial 12", bg="white").pack(pady=5)
file_entry = Entry(root, width=40, font="Arial 12")
file_entry.pack(pady=5)

# 🎯 Function to Generate QR
def generate_qr():
    data = data_entry.get()
    filename = file_entry.get()

    if data == "" or filename == "":
        messagebox.showerror("Error", "Please enter both Text/URL and File Name")
    else:
        qr_img = qrcode.make(data)
        qr_img.save(f"{filename}.png")

        # 🖼️ Display QR code
        img = Image.open(f"{filename}.png")
        img = img.resize((180, 180))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        lbl.image = img

        messagebox.showinfo("Success", f"QR Code saved as {filename}.png")

# 🎯 Button
Button(root, text="Generate QR Code", command=generate_qr, font="Arial 14", bg="black", fg="white").pack(pady=10)

# 🖼️ Label to show QR image
lbl = Label(root, bg="white")
lbl.pack(pady=10)

# 🔥 Run
root.mainloop()
