#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class TinyXorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 tiny-xor — Шифрование файлов")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Путь к бинарнику tiny-xor
        self.tiny_xor_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tiny-xor")
        
        # Создаём интерфейс
        self.create_widgets()
    
    def create_widgets(self):
        # Заголовок
        title = tk.Label(self.root, text="🔐 tiny-xor", font=("Arial", 18, "bold"))
        title.pack(pady=10)
        
        subtitle = tk.Label(self.root, text="Простое шифрование файлов", font=("Arial", 10))
        subtitle.pack(pady=5)
        
        # Разделитель
        tk.Frame(self.root, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=10, pady=10)
        
        # Входной файл
        tk.Label(self.root, text="Исходный файл:", anchor=tk.W).pack(fill=tk.X, padx=20)
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill=tk.X, padx=20, pady=5)
        
        self.input_path = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.input_path, width=45).pack(side=tk.LEFT, padx=(0, 5))
        tk.Button(input_frame, text="Выбрать", command=self.select_input_file).pack(side=tk.LEFT)
        
        # Выходной файл
        tk.Label(self.root, text="Зашифрованный файл:", anchor=tk.W).pack(fill=tk.X, padx=20, pady=(10, 0))
        output_frame = tk.Frame(self.root)
        output_frame.pack(fill=tk.X, padx=20, pady=5)
        
        self.output_path = tk.StringVar()
        tk.Entry(output_frame, textvariable=self.output_path, width=45).pack(side=tk.LEFT, padx=(0, 5))
        tk.Button(output_frame, text="Выбрать", command=self.select_output_file).pack(side=tk.LEFT)
        
        # Пароль
        tk.Label(self.root, text="Пароль (ключ шифрования):", anchor=tk.W).pack(fill=tk.X, padx=20, pady=(10, 0))
        self.password = tk.StringVar()
        tk.Entry(self.root, textvariable=self.password, show="*", width=50).pack(padx=20, pady=5)
        
        # Кнопки
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="🔒 Зашифровать", command=self.encrypt, 
                  bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=15, height=2).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="🔓 Расшифровать", command=self.decrypt, 
                  bg="#2196F3", fg="white", font=("Arial", 11, "bold"), width=15, height=2).pack(side=tk.LEFT, padx=5)
        
        # Статус
        self.status = tk.Label(self.root, text="Готов к работе", fg="green", font=("Arial", 10))
        self.status.pack(pady=10)
    
    def select_input_file(self):
        filename = filedialog.askopenfilename(title="Выберите файл для шифрования")
        if filename:
            self.input_path.set(filename)
            # Автоматически предлагаем имя для выходного файла
            base, ext = os.path.splitext(filename)
            self.output_path.set(base + "_encrypted" + ext)
    
    def select_output_file(self):
        filename = filedialog.asksaveasfilename(title="Сохранить зашифрованный файл как")
        if filename:
            self.output_path.set(filename)
    
    def encrypt(self):
        if not self.validate_inputs():
            return
        
        self.status.config(text="Шифрование...", fg="orange")
        self.root.update()
        
        try:
            result = subprocess.run(
                [self.tiny_xor_path, self.input_path.get(), self.output_path.get(), self.password.get()],
                capture_output=True,
                text=True,
                check=True
            )
            self.status.config(text="✅ Файл успешно зашифрован!", fg="green")
            messagebox.showinfo("Успех", f"Файл зашифрован и сохранён как:\n{self.output_path.get()}")
        except subprocess.CalledProcessError as e:
            self.status.config(text="❌ Ошибка шифрования", fg="red")
            messagebox.showerror("Ошибка", f"Не удалось зашифровать файл:\n{e.stderr}")
        except Exception as e:
            self.status.config(text="❌ Ошибка", fg="red")
            messagebox.showerror("Ошибка", f"Произошла ошибка:\n{str(e)}")
    
    def decrypt(self):
        if not self.validate_inputs():
            return
        
        self.status.config(text="Расшифровка...", fg="orange")
        self.root.update()
        
        try:
            result = subprocess.run(
                [self.tiny_xor_path, self.input_path.get(), self.output_path.get(), self.password.get()],
                capture_output=True,
                text=True,
                check=True
            )
            self.status.config(text="✅ Файл успешно расшифрован!", fg="green")
            messagebox.showinfo("Успех", f"Файл расшифрован и сохранён как:\n{self.output_path.get()}")
        except subprocess.CalledProcessError as e:
            self.status.config(text="❌ Ошибка расшифровки", fg="red")
            messagebox.showerror("Ошибка", f"Не удалось расшифровать файл:\n{e.stderr}")
        except Exception as e:
            self.status.config(text="❌ Ошибка", fg="red")
            messagebox.showerror("Ошибка", f"Произошла ошибка:\n{str(e)}")
    
    def validate_inputs(self):
        if not self.input_path.get():
            messagebox.showwarning("Внимание", "Выберите входной файл")
            return False
        
        if not self.output_path.get():
            messagebox.showwarning("Внимание", "Выберите выходной файл")
            return False
        
        if not self.password.get():
            messagebox.showwarning("Внимание", "Введите пароль")
            return False
        
        if not os.path.exists(self.tiny_xor_path):
            messagebox.showerror("Ошибка", f"Не найден файл tiny-xor по пути:\n{self.tiny_xor_path}\n\nУбедитесь, что вы собрали программу.")
            return False
        
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = TinyXorGUI(root)
    root.mainloop()
