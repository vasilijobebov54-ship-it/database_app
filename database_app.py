import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Поиск в базе данных")

        self.data = None

        # Кнопка для загрузки файла
        self.load_button = tk.Button(root, text="Загрузить файл", command=self.load_file)
        self.load_button.pack(pady=10)

        # Поле для ввода запроса
        self.query_entry = tk.Entry(root, width=50)
        self.query_entry.pack(pady=10)

        # Кнопка для поиска
        self.search_button = tk.Button(root, text="Поиск", command=self.search_data)
        self.search_button.pack(pady=10)

        # Текстовое поле для вывода результатов
        self.result_text = tk.Text(root, width=80, height=20)
        self.result_text.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")])
        if file_path:
            try:
                if file_path.endswith('.csv'):
                    self.data = pd.read_csv(file_path)
                elif file_path.endswith('.txt'):
                    self.data = pd.read_csv(file_path, sep="\t")  # Предполагаем, что текстовый файл разделен табуляцией
                messagebox.showinfo("Успех", "Файл загружен успешно!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")

    def search_data(self):
        if self.data is not None:
            query = self.query_entry.get()
            results = self.data[self.data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
            self.result_text.delete(1.0, tk.END)  # Очистить текстовое поле
            if not results.empty:
                self.result_text.insert(tk.END, results.to_string(index=False))
            else:
                self.result_text.insert(tk.END, "Нет результатов.")
        else:
            messagebox.showwarning("Предупреждение", "Сначала загрузите файл.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
