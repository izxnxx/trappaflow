import tkinter as tk
from tkinter import ttk, messagebox

class Employee:
    def __init__(self, company, position, phone, email, salary):
        self.data = [company, position, phone, email, salary]

class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Працівники")
        self.root.geometry("800x500")

        self.employees = [
            Employee("Google", "Розробник", "380991234567", "dev@google.com", 5000),
            Employee("Microsoft", "Менеджер", "380992345678", "manager@microsoft.com", 4500),
        ]

        fields = ["Фірма", "Посада", "Телефон", "Email", "Оклад"]
        self.entries = []
        for i, field in enumerate(fields):
            ttk.Label(root, text=field).grid(row=0, column=i * 2, padx=5)
            entry = ttk.Entry(root, width=15)
            entry.grid(row=0, column=i * 2 + 1, padx=5)
            self.entries.append(entry)

        ttk.Button(root, text="Додати", command=self.add).grid(row=0, column=10, padx=5)
        ttk.Button(root, text="Показати всіх", command=self.show_all).grid(row=1, column=0, pady=10)
        ttk.Button(root, text="Сортувати", command=self.sort).grid(row=1, column=1, pady=10)
        ttk.Button(root, text="Видалити за", command=self.delete_attr).grid(row=1, column=2, pady=10)
        ttk.Button(root, text="Видалити індекс", command=self.delete_idx).grid(row=1, column=3, pady=10)
        ttk.Button(root, text="Пошук", command=self.search).grid(row=1, column=4, pady=10)

        # Поле для індексу/пошуку
        self.search_entry = ttk.Entry(root, width=15)
        self.search_entry.grid(row=1, column=5, pady=10)

        # Таблиця
        columns = fields
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.grid(row=2, column=0, columnspan=11, sticky="nsew", padx=10, pady=10)

        self.refresh()

    def refresh(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for emp in self.employees:
            self.tree.insert("", tk.END, values=emp.data)

    def add(self):
        values = [e.get() for e in self.entries]
        if all(values[:-1]) and values[-1].isdigit():
            self.employees.append(Employee(*values[:-1], int(values[-1])))
            self.refresh()
            for e in self.entries:
                e.delete(0, tk.END)
        else:
            messagebox.showerror("Помилка", "Невірні дані")

    def show_all(self):
        self.refresh()

    def sort(self):
        attrs = ["Фірма", "Посада", "Телефон", "Email", "Оклад"]
        attr = self.simple_dialog("Сортування", "Сортувати за:", attrs)
        if attr:
            idx = attrs.index(attr)
            self.employees.sort(key=lambda x: x.data[idx])
            self.refresh()

    def delete_attr(self):
        attrs = ["Фірма", "Посада", "Телефон", "Email", "Оклад"]
        attr = self.simple_dialog("Видалення", "Видалити де:", attrs)
        if attr:
            idx = attrs.index(attr)
            value = self.search_entry.get()
            self.employees = [e for e in self.employees if str(e.data[idx]) != value]
            self.refresh()

    def delete_idx(self):
        try:
            idx = int(self.search_entry.get())
            if 0 <= idx < len(self.employees):
                del self.employees[idx]
                self.refresh()
        except:
            messagebox.showerror("Помилка", "Невірний індекс")

    def search(self):
        attrs = ["Фірма", "Посада", "Телефон", "Email", "Оклад"]
        attr = self.simple_dialog("Пошук", "Шукати за:", attrs)
        if attr:
            idx = attrs.index(attr)
            value = self.search_entry.get()
            for item in self.tree.get_children():
                self.tree.delete(item)
            for emp in self.employees:
                if str(emp.data[idx]) == value:
                    self.tree.insert("", tk.END, values=emp.data)

    def simple_dialog(self, title, text, options):
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("300x200")

        ttk.Label(dialog, text=text).pack(pady=10)

        var = tk.StringVar()
        for opt in options:
            ttk.Radiobutton(dialog, text=opt, variable=var, value=opt).pack()

        result = []

        def close():
            result.append(var.get())
            dialog.destroy()

        ttk.Button(dialog, text="OK", command=close).pack(pady=20)
        dialog.wait_window()
        return result[0] if result else None

root = tk.Tk()
app = EmployeeApp(root)
root.mainloop()