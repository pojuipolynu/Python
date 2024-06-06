import tkinter as tk
from tkinter import messagebox

tourist_spots = {
            "1": "Київ-Чернігів, 29.09, 120 грн.",
            "2": "Житомир-Миколаїв, 09.09, 230 грн.",
            "3": "Хмельницький-Краматорськ, 01.06, 110 грн.",
            "4": "Вінниця-Львів, 03.02, 340 грн.",
            "5": "Херсон-Харків, 29.09, 120 грн.",
            "6": "Одеса-Київ, 19.09, 250 грн."
        }

class TouristCompanyApp:
    def __init__(self, master):
        self.master = master
        master.title("Туристична компанія")

        self.label = tk.Label(master, text="Ласкаво просимо до туристичної компанії")
        self.label.pack()

        self.search_label = tk.Label(master, text="Введіть номер маршруту:")
        self.search_label.pack()

        self.search_entry = tk.Entry(master)
        self.search_entry.pack()

        self.search_button = tk.Button(master, text="Пошук", command=self.search)
        self.search_button.pack()

        self.information_label = tk.Label(master, text="")
        self.information_label.pack()

        self.create_place_button = tk.Button(self.master, text="Створити новий маршрут", command=self.admin)
        self.create_place_button.pack()

    def admin(self):
        self.username_label = tk.Label(text="Ім'я користувача:")
        self.username_label.pack()

        self.username_entry = tk.Entry()
        self.username_entry.pack()

        self.password_label = tk.Label(text="Пароль:")
        self.password_label.pack()

        self.password_entry = tk.Entry(show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(text="Увійти", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Успішний вхід!")
            self.create_place_button = tk.Button(self.master, text="Створити новий маршрут", command=self.create_place)
            self.create_place_button.pack()
        else:
            messagebox.showerror("Помилка", "Невірне ім'я користувача або пароль.")

    def create_place(self):
        messagebox.showinfo("Створення місця", "Ви можете розпочати процес створення нового місця тут.")
        self.label = tk.Label(text="Введіть номер маршруту:")
        self.label.pack()
        self.entry = tk.Entry()
        self.entry.pack()
        self.name = tk.Label(text="Введіть назву маршруту:")
        self.name.pack()
        self.nameentry = tk.Entry()
        self.nameentry.pack()
        self.data = tk.Label(text="Введіть дату маршруту:")
        self.data.pack()
        self.dataentry = tk.Entry()
        self.dataentry.pack()
        self.price = tk.Label(text="Введіть ціну маршруту:")
        self.price.pack()
        self.priceentry = tk.Entry()
        self.priceentry.pack()
        self.search_button = tk.Button(text="Створити", command=self.add)
        self.search_button.pack()
    
    def add(self):
        number = self.entry.get()
        name = self.nameentry.get()
        data = self.dataentry.get()
        price = self.priceentry.get()
        if not number or not name or not data or not price:
            messagebox.showerror("Помилка", "Всі поля повинні бути заповнені!")
        tourist_spots[number] = f'{name}, {data}, {price}.'
        messagebox.showinfo("Успіх", "Оголошення оновлено!")
        self.entry.delete(0, tk.END)
        self.nameentry.delete(0, tk.END)
        self.dataentry.delete(0, tk.END)
        self.priceentry.delete(0, tk.END)

    def search(self):
        query = self.search_entry.get()
        information = tourist_spots.get(query, "Вибачте інформацію не знайдено {}".format(query))
        self.information_label.config(text=information)

def main():
    root = tk.Tk()
    app = TouristCompanyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()