from tkinter import Tk, filedialog
from PIL import Image

def open_file_dialog():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])
    return file_path

def save_file_dialog():
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".bmp", filetypes=[("BMP files", "*.bmp")])
    return file_path

def convert_to_bmp(input_file, output_file):
    img = Image.open(input_file)
    img.save(output_file)

# Открываем файл jpg
jpg_file_path = open_file_dialog()

# Конвертируем и сохраняем в bmp
if jpg_file_path:
    bmp_file_path = save_file_dialog()
    if bmp_file_path:
        convert_to_bmp(jpg_file_path, bmp_file_path)
        print("Конвертация завершена. Файл сохранен как", bmp_file_path)