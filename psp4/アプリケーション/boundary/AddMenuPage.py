import tkinter as tk
from tkinter import messagebox
from DAO.StockDAO import StockDAO

class AddMenuPage(tk.Tk):
    def __init__(self, inventory_page):
        super().__init__()

        self.title("新メニュー追加")
        self.geometry("800x400")

        self.inventory_page = inventory_page

        self.menu_name_var = tk.StringVar()
        self.kind_var = tk.StringVar()
        self.price_var = tk.DoubleVar()
        self.quantity_var = tk.IntVar()

        self.create_widgets()

    def return_to_inventory_page(self):
        self.destroy()
        self.inventory_page.update_inventory()
        self.inventory_page.deiconify()  # InventoryPageを再表示

    def add_menu(self):
        menu_name = self.menu_name_var.get()
        kind = self.kind_var.get()
        price = self.price_var.get()
        quantity = self.quantity_var.get()

        new_menu = Inventory(menu_name, kind, quantity, price)
        StockDAO().add_item(new_menu)

        messagebox.showinfo("確認", "メニューが追加されました。")
        self.return_to_inventory_page()

    def create_widgets(self):
        lbl_menu_name = tk.Label(self, text="メニュー名")
        lbl_menu_name.pack(pady=5)
        entry_menu_name = tk.Entry(self, textvariable=self.menu_name_var)
        entry_menu_name.pack(pady=5)

        lbl_kind = tk.Label(self, text="ジャンル")
        lbl_kind.pack(pady=5)
        entry_kind = tk.Entry(self, textvariable=self.kind_var)
        entry_kind.pack(pady=5)

        lbl_price = tk.Label(self, text="値段")
        lbl_price.pack(pady=5)
        entry_price = tk.Entry(self, textvariable=self.price_var)
        entry_price.pack(pady=5)

        lbl_quantity = tk.Label(self, text="在庫")
        lbl_quantity.pack(pady=5)
        entry_quantity = tk.Entry(self, textvariable=self.quantity_var)
        entry_quantity.pack(pady=5)

        btn_confirm = tk.Button(self, text="確定", command=self.add_menu)
        btn_confirm.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X)

        btn_return = tk.Button(self, text="戻る", command=self.return_to_inventory_page)
        btn_return.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.X)

if __name__ == "__main__":
    app = AddMenuPage()
    app.mainloop()
