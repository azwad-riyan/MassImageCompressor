import os
from tkinter import Tk, Button, Label, filedialog, Scale, HORIZONTAL, messagebox, StringVar
from PIL import Image

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        selected_folder.set(folder)
        status_label.config(text="Folder Selected: " + folder)

def compress_images():
    folder = selected_folder.get()
    if not folder:
        messagebox.showerror("Error", "Please select a folder first.")
        return

    compress_quality = quality_scale.get()
    new_folder = os.path.join(folder, "compressed_images")
    os.makedirs(new_folder, exist_ok=True)

    supported_exts = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    count = 0

    for filename in os.listdir(folder):
        if filename.lower().endswith(supported_exts):
            image_path = os.path.join(folder, filename)
            try:
                img = Image.open(image_path)
                rgb_img = img.convert("RGB")
                save_path = os.path.join(new_folder, filename)
                rgb_img.save(save_path, optimize=True, quality=compress_quality)
                count += 1
            except Exception as e:
                print(f"Failed to compress {filename}: {e}")

    messagebox.showinfo("Done", f"Compressed {count} images to '{new_folder}'")

# GUI
root = Tk()
root.title("Image Compressor")
root.geometry("400x250")

selected_folder = StringVar()

Label(root, text="Select Folder with Images:").pack(pady=5)
Button(root, text="Browse Folder", command=select_folder).pack(pady=5)

Label(root, text="Select Compression Quality (%)").pack(pady=5)
quality_scale = Scale(root, from_=10, to=95, orient=HORIZONTAL)
quality_scale.set(60)
quality_scale.pack(pady=5)

Button(root, text="Compress Images", command=compress_images, bg="green", fg="white").pack(pady=15)
status_label = Label(root, text="No folder selected.")
status_label.pack()

root.mainloop()
