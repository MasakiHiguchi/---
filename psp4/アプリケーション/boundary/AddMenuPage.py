import tkinter as tk
from tkinter import messagebox
from DAO.StockDAO import StockDAO
from entity.Inventory import Inventory

class AddMenuPage(tk.Toplevel):  # Toplevelを使ってAddMenuPageを子ウィンドウにします
    def __init__(self, parent):  # 親ウィンドウを受け取るように変更
        super().__init__(parent)

        self.title("Add Menu Page")
        self.geometry("800x400")

        self.parent = parent  # 親ウィンドウを保持

        self.menu_name_var = tk.StringVar()
        self.kind_var = tk.StringVar()
        self.price_var = tk.DoubleVar()
        self.quantity_var = tk.IntVar()

        self.create_widgets()


    def return_to_inventory_page(self):
        self.destroy()
        from InventoryPage import InventoryPage
        self.inventory_page = InventoryPage()
        self.inventory_page.mainloop()

    def add_menu(self):
        menu_name = self.menu_name_var.get()
        kind = self.kind_var.get()
        price = self.price_var.get()
        quantity = self.quantity_var.get()

        new_menu = Inventory(menu_name, kind, quantity, price)
        self.stock_dao.add_item(new_menu)

        # 親ウィンドウ（InventoryPage）のupdate_inventoryメソッドを呼び出して更新
        self.parent.update_inventory()

    def create_widgets(self):
        self.stock_dao = StockDAO()

        # 左側のフレームを作成
        frame_left = tk.Frame(self, padx=10, pady=10)
        frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 右側のフレームを作成
        frame_right = tk.Frame(self, padx=10, pady=10)
        frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # 左側のラベルと右側の入力欄を作成
        lbl_menu_name = tk.Label(frame_left, text="メニュー名")
        lbl_menu_name.pack(pady=5)

        entry_menu_name = tk.Entry(frame_right, textvariable=self.menu_name_var)
        entry_menu_name.pack(pady=5)

        lbl_kind = tk.Label(frame_left, text="ジャンル")
        lbl_kind.pack(pady=5)

        entry_kind = tk.Entry(frame_right, textvariable=self.kind_var)
        entry_kind.pack(pady=5)

        lbl_price = tk.Label(frame_left, text="値段")
        lbl_price.pack(pady=5)

        entry_price = tk.Entry(frame_right, textvariable=self.price_var)
        entry_price.pack(pady=5)

        lbl_quantity = tk.Label(frame_left, text="在庫")
        lbl_quantity.pack(pady=5)

        entry_quantity = tk.Entry(frame_right, textvariable=self.quantity_var)
        entry_quantity.pack(pady=5)

        # 下部のボタン
        btn_confirm = tk.Button(self, text="確定", command=self.add_menu)
        btn_confirm.pack(side=tk.BOTTOM, pady=10, fill=tk.X)

        btn_return = tk.Button(self, text="戻る", command=self.return_to_inventory_page)
        btn_return.pack(side=tk.BOTTOM, pady=10, fill=tk.X)

if __name__ == "__main__":
    app = AddMenuPage()
    app.mainloop()
