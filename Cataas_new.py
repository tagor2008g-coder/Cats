from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import webbrowser

# Список доступных тегов
ALLOWED_TAGS = [
    'sleep', 'jump', 'smile', 'fight', 'black', 'white', 'red', 'siamese', 'bengal'
]

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None

def open_new_window():
    tag = tag_combobox.get()
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_with_tag)
    if img:
        new_window = Toplevel()
        new_window.title("Cat Image")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.image = img
        label.pack()

def open_random_cat():
    """Открывает случайного котика в новой вкладке браузера"""
    webbrowser.open_new_tab('https://cataas.com/cat')

window = Tk()
window.title("Cats!")
window.geometry("600x520")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=window.destroy)

# Фрейм для элементов управления
control_frame = Frame(window)
control_frame.pack(pady=10)

# Метка "Выбери тег"
tag_label = Label(control_frame, text="Выбери тег")
tag_label.grid(row=0, column=0, padx=5)

tag_combobox = ttk.Combobox(control_frame, values=ALLOWED_TAGS, width=15)
tag_combobox.grid(row=0, column=1, padx=5)

# Кнопка "Случайный котик"
random_button = Button(control_frame, text="Случайный котик", command=open_random_cat)
random_button.grid(row=0, column=2, padx=5)

window.mainloop()