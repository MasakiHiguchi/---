import tkinter as tk
from tkinter import messagebox
from DAO.StockDAO import StockDAO
from AddMenuPage import AddMenuPage

class InventoryPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Inventory Page")
        self.geometry("800x400")

        self.stock_dao = StockDAO()

        self.create_widgets()
        self.display_inventory()

    def create_widgets(self):
        # 在庫情報表示用のフレーム
        self.frame_inventory = tk.Frame(self)
        self.frame_inventory.pack(padx=20, pady=20)

        # 在庫情報のヘッダ
        lbl_name_header = tk.Label(self.frame_inventory, text="商品名", font=("Helvetica", 12, "bold"))
        lbl_name_header.grid(row=0, column=0, padx=5, pady=5)

        lbl_quantity_header = tk.Label(self.frame_inventory, text="数量", font=("Helvetica", 12, "bold"))
        lbl_quantity_header.grid(row=0, column=1, padx=5, pady=5)

        # 戻るボタン
        btn_add_menu = tk.Button(self, text="AddMenuPage", command=self.open_add_menu_page)
        btn_add_menu.pack(side=tk.TOP, pady=10, fill=tk.X)

        btn_back = tk.Button(self, text="戻る", command=self.return_to_main_page)
        btn_back.pack(side=tk.RIGHT, pady=10, fill=tk.X)

        btn_add_menu = tk.Button(self, text="メニュー追加", command=self.open_add_menu_page)
        btn_add_menu.pack(side=tk.BOTTOM, pady=10, fill=tk.X)

    def display_inventory(self):
        # StockDAOの情報を取得して表示する
        inventory_list = self.stock_dao.get_all_items()

        for i, item in enumerate(inventory_list, start=1):
            lbl_name = tk.Label(self.frame_inventory, text=item.name)
            lbl_name.grid(row=i, column=0, padx=5, pady=5)

            quantity_var = tk.IntVar(value=item.quantity)
            entry_quantity = tk.Entry(self.frame_inventory, textvariable=quantity_var)
            entry_quantity.grid(row=i, column=1, padx=5, pady=5)

            # 確定ボタンを押した時に、StockDAOのquantityを更新するコマンドを紐付ける
            btn_confirm = tk.Button(self.frame_inventory, text="確定", command=lambda item=item, quantity_var=quantity_var: self.update_quantity(item, quantity_var))
            btn_confirm.grid(row=i, column=2, padx=5, pady=5)

    def update_quantity(self, item, quantity_var):
        new_quantity = quantity_var.get()
        self.stock_dao.update_item_quantity(item.name, new_quantity)
        messagebox.showinfo("確認", f"{item.name}の数量が更新されました。")

    def return_to_main_page(self):
        self.destroy()

    def open_add_menu_page(self):
        # AddMenuPageを子ウィンドウとして表示
        add_menu_page = AddMenuPage(self)
        add_menu_page.grab_set()

if __name__ == "__main__":
    app = InventoryPage()
    app.mainloop()
