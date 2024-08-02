import qrcode
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

cp = Tk()
cp.title('QR Generator')
cp.geometry('700x350')
cp.config(bg='#e52165')

def generate():
    img = qrcode.make(msg.get())
    img.save(f'{save_name.get()}.png')
    Label(cp, text='File Saved!', bg='#e52165', fg='black', font=('Arial Black', 8)).pack()

def show():
    img = qrcode.make(msg.get())
    img.show()

def generate_image():
    qr_data = msg.get()
    img = qrcode.make(qr_data)
    file_path = 'temp_qr_code.png'
    img.save(file_path)

    # Display the image in the Tkinter window
    img_open = Image.open(file_path)
    img_tk = ImageTk.PhotoImage(img_open)

    img_label = Label(cp, image=img_tk, bg='#e52165')
    img_label.image = img_tk  # Keep a reference to the image to prevent garbage collection
    img_label.pack()

    Label(cp, text='QR Code Image Generated!', bg='#e52165', fg='black', font=('Arial Black', 8)).pack()

    # Optional: Remove the temporary image file
    os.remove(file_path)

frame = Frame(cp, bg='#e52165')
frame.pack(expand=True, pady=20)

#------------------ENTER THE TEXT OR URL------------------

Label(frame, text='Enter the Text or URL : ', font=('Arial Black', 16), bg='#e52165', fg='white').grid(row=0, column=0, sticky='w', padx=10, pady=10)

msg = Entry(frame, font=('Arial', 14), width=30)
msg.grid(row=0, column=1, padx=10, pady=10)

#------------------ENTER THE FILE NAME------------------

Label(frame, text='File Name(Save As) : ', font=('Arial Black', 16), bg='#e52165', fg='white').grid(row=1, column=0, sticky='w', padx=10, pady=10)

save_name = Entry(frame, font=('Arial', 14), width=30)
save_name.grid(row=1, column=1, padx=10, pady=10)

#------------------BUTTONS TO SHOW OR SAVE QRCODE------------------

btn_frame = Frame(cp, bg='#e52165')
btn_frame.pack(pady=10)

show_btn = ttk.Button(btn_frame, text='Show QR code', command=show, width=20)
show_btn.grid(row=0, column=0, padx=10)

save_btn = ttk.Button(btn_frame, text='Save QR code', command=generate, width=20)
save_btn.grid(row=0, column=1, padx=10)

generate_img_btn = ttk.Button(btn_frame, text='Generate QR Image', command=generate_image, width=20)
generate_img_btn.grid(row=0, column=2, padx=10)

cp.mainloop()
