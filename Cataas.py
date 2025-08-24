from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except tException as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None


def open_new_window():
    tag = tag_entry.get()
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_with_tag)

    if img:
        new_window = Toplevel()
        new_window.title("Cat Image")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.image = img
        label.pack()


def exit_app():
    window.destroy()


window = Tk()
…
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_app)

# Поле ввода для тегов
tag_entry = Entry()
tag_entry.pack()

# Кнопка для загрузки изображения с тегом
load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()

window.mainloop()






