import tkinter as tk
import subprocess
from InventoryPage import InventoryPage
from AddMenuPage import AddMenuPage
from ManageOrderProductPage import ManageOrderProductPage


class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Main Page")
        self.geometry("800x400")

        self.create_widgets()

    def open_inventory_page(self):
        self.destroy()
        self.inventory_page = InventoryPage()
        self.inventory_page.mainloop()

    def open_add_menu_page(self):
        self.destroy()
        self.add_menu_page = AddMenuPage(self)
        self.add_menu_page.mainloop()

    def open_manage_order_product_page(self):
        self.destroy()
        self.manage_order_product_page = ManageOrderProductPage()
        self.manage_order_product_page.mainloop()

    def create_widgets(self):
        lbl_title = tk.Label(self, text="メインメニュー", font=("Helvetica", 20))
        lbl_title.pack(pady=20)

        frame_top = tk.Frame(self)
        frame_top.pack(side=tk.TOP, fill=tk.X)

        # T1からT3までのボタンを横に並べる
        btn_t1 = tk.Button(frame_top, text="T1", command=self.open_order_page_t1, width=15, height=10)
        btn_t1.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=10)

        btn_t2 = tk.Button(frame_top, text="T2", command=self.open_order_page_t2, width=15, height=10)
        btn_t2.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=10)

        btn_t3 = tk.Button(frame_top, text="T3", command=self.open_order_page_t3, width=15, height=10)
        btn_t3.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=10)

        frame_bottom = tk.Frame(self)
        frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # 左下のボタン
        btn_inventory = tk.Button(frame_bottom, text="InventoryPage", command=self.open_inventory_page, width=15, height=1)
        btn_inventory.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=30, expand=True)

        # 右下のボタン
        btn_manage_order_product = tk.Button(frame_bottom, text="ManageOrderProductPage", command=self.open_manage_order_product_page, width=15, height=1)
        btn_manage_order_product.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=30, expand=True)

    def open_order_page_t1(self):
        # T1のOrderPage.pyを実行する
        subprocess.run(["python", "OrderPage.py", "T1"])

    def open_order_page_t2(self):
        # T2のOrderPage.pyを実行する
        subprocess.run(["python", "OrderPage.py", "T2"])

    def open_order_page_t3(self):
        # T3のOrderPage.pyを実行する
        subprocess.run(["python", "OrderPage.py", "T3"])

if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
