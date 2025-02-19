from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def binary_to_text(binary_string):
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def xor_decrypt(text, password):
    return ''.join(chr(ord(t) ^ ord(password[i % len(password)])) for i, t in enumerate(text))

def extract_text(image_path, password):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    
    binary_message = ""
    for pixel in pixels:
        r, g, b = pixel
        binary_message += str(r & 1)
        binary_message += str(g & 1)
        binary_message += str(b & 1)
    
    end_marker = "1111111111111110"
    binary_message = binary_message.split(end_marker)[0]
    
    encrypted_message = binary_to_text(binary_message)
    secret_message = xor_decrypt(encrypted_message, password)
    
    messagebox.showinfo("Decoded Message", secret_message)

def decode():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    password = entry_pass_dec.get()
    if not password:
        messagebox.showerror("Error", "Password cannot be empty!")
        return
    
    extract_text(file_path, password)

root = tk.Tk()
root.title("Image Steganography Decoder")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Enter Passcode to Decode:").pack()
entry_pass_dec = tk.Entry(frame, width=50, show="*")
entry_pass_dec.pack()

tk.Button(frame, text="Select Image & Decode", command=decode).pack(pady=10)

root.mainloop()
