import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Функция для выбора директории
def choose_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_path.set(directory)

# Функция для создания папок по списку
def create_folders():
    directory = directory_path.get()
    folder_names = folder_list.get("1.0", "end-1c").splitlines()
    
    if not os.path.exists(directory):
        messagebox.showerror("Ошибка", "Указанный путь не существует!")
        return
    
    if not folder_names:
        messagebox.showwarning("Предупреждение", "Не указаны имена папок!")
        return
    
    created_folders = []
    for folder in folder_names:
        folder_path = os.path.join(directory, folder)
        try:
            os.makedirs(folder_path, exist_ok=True)
            created_folders.append(folder)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось создать папку: {folder}\nОшибка: {str(e)}")
    
    if created_folders:
        messagebox.showinfo("Успех", f"Созданы папки:\n{', '.join(created_folders)}")

# Функция для создания папок от 1 до N
def create_folders_range():
    directory = directory_path.get()
    try:
        folder_count = int(folder_count_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число для количества папок!")
        return
    
    if not os.path.exists(directory):
        messagebox.showerror("Ошибка", "Указанный путь не существует!")
        return
    
    created_folders = []
    for i in range(1, folder_count + 1):
        folder_path = os.path.join(directory, f"Папка {i}")
        try:
            os.makedirs(folder_path, exist_ok=True)
            created_folders.append(f"Папка {i}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось создать папку: Папка {i}\nОшибка: {str(e)}")
    
    if created_folders:
        messagebox.showinfo("Успех", f"Созданы папки:\n{', '.join(created_folders)}")

# Создание окна приложения
root = tk.Tk()
root.title("Создание папок")

# Переменная для хранения выбранного пути
directory_path = tk.StringVar()

# Элементы интерфейса
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Поле для выбора директории
tk.Label(frame, text="Путь для создания папок:").grid(row=0, column=0, sticky="w")
path_entry = tk.Entry(frame, textvariable=directory_path, width=50)
path_entry.grid(row=1, column=0, padx=5, pady=5, sticky="we")
choose_button = tk.Button(frame, text="Выбрать папку", command=choose_directory)
choose_button.grid(row=1, column=1, padx=5, pady=5)

# Поле для ввода списка папок
tk.Label(frame, text="Введите имена папок (по одной на строку):").grid(row=2, column=0, sticky="w")
folder_list = tk.Text(frame, width=50, height=10)
folder_list.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Кнопка для создания папок по списку
create_button = tk.Button(frame, text="Создать папки по списку", command=create_folders)
create_button.grid(row=4, column=0, columnspan=2, pady=10)

# Поле для ввода количества папок
tk.Label(frame, text="Создать папки от 1 до:").grid(row=5, column=0, sticky="w")
folder_count_entry = tk.Entry(frame, width=10)
folder_count_entry.grid(row=6, column=0, padx=5, pady=5, sticky="w")

# Кнопка для создания папок от 1 до N
create_range_button = tk.Button(frame, text="Создать папки от 1 до N", command=create_folders_range)
create_range_button.grid(row=6, column=1, padx=5, pady=5)

# Запуск приложения
root.mainloop()
