from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def xor_encrypt(text, password):
    return ''.join(chr(ord(t) ^ ord(password[i % len(password)])) for i, t in enumerate(text))

def hide_text(image_path, output_path, secret_message, password):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    encrypted_message = xor_encrypt(secret_message, password)
    binary_message = text_to_binary(encrypted_message) + '1111111111111110'  # End marker
    pixels = list(img.getdata())
    
    new_pixels = []
    binary_index = 0

    for pixel in pixels:
        r, g, b = pixel
        if binary_index < len(binary_message):
            r = (r & ~1) | int(binary_message[binary_index])
            binary_index += 1
        if binary_index < len(binary_message):
            g = (g & ~1) | int(binary_message[binary_index])
            binary_index += 1
        if binary_index < len(binary_message):
            b = (b & ~1) | int(binary_message[binary_index])
            binary_index += 1
        
        new_pixels.append((r, g, b))
    
    img.putdata(new_pixels)
    img.save(output_path)
    messagebox.showinfo("Success", f"Message hidden successfully in {output_path}")

def encode():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    output_path = "encoded_image.png"
    secret_message = entry_msg.get()
    password = entry_pass.get()
    
    if not secret_message or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return
    
    hide_text(file_path, output_path, secret_message, password)

root = tk.Tk()
root.title("Image Steganography - Encoder")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Encoder UI
tk.Label(frame, text="Enter Secret Message:").pack()
entry_msg = tk.Entry(frame, width=50)
entry_msg.pack()

tk.Label(frame, text="Enter Passcode:").pack()
entry_pass = tk.Entry(frame, width=50, show="*")
entry_pass.pack()

tk.Button(frame, text="Select Image & Encode", command=encode).pack(pady=10)

root.mainloop()
