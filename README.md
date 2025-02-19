# Image Steganography: Secure Message Encoding & Decoding

## 📌 Project Overview
This project implements **image steganography** using **Least Significant Bit (LSB) encoding** combined with **XOR encryption** to securely hide messages within images. It provides a **user-friendly GUI** for encoding and decoding messages while ensuring data secrecy.

## 🚀 Features
- **LSB Steganography**: Hides messages in image pixels without noticeable distortion.
- **XOR Encryption**: Adds an extra security layer to the hidden message.
- **GUI-Based Encoding & Decoding**: Simple interface using Tkinter.
- **Secure Extraction**: Only accessible with the correct password.
- **Undetectable Storage**: No significant image alterations.

## 🛠️ Technologies Used
- **Python**
- **PIL (Pillow)** – Image processing
- **Tkinter** – GUI
- **OS** – File handling
- **NumPy** – Binary manipulation

## 📖 How It Works
### 🔐 **Encoding Process**
1. **User inputs a secret message & password**.
2. **XOR encryption** scrambles the message.
3. **LSB encoding** embeds the encrypted message into the image.
4. The **modified image is saved** as output.

### 🔓 **Decoding Process**
1. **User selects the encoded image & enters the password**.
2. **Extracts binary data** from pixel values.
3. **Detects end marker (`1111111111111110`)** to stop reading.
4. **XOR decryption** recovers the original message.

## 🖥️ Installation & Usage
### 🔧 **Prerequisites**
Ensure Python is installed. Install required dependencies:

```bash
pip install pillow numpy
