import tkinter as tk

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MainPage")
        self.geometry("400x300")

        # ボタンを作成して配置
        self.create_buttons()

    def create_buttons(self):
        # 上半分のボタン
        btn_t1 = tk.Button(self, text="T1", command=self.open_order_page_t1)
        btn_t1.pack(side=tk.TOP, fill=tk.X)

        btn_t2 = tk.Button(self, text="T2", command=self.open_order_page_t2)
        btn_t2.pack(side=tk.TOP, fill=tk.X)

        btn_t3 = tk.Button(self, text="T3", command=self.open_order_page_t3)
        btn_t3.pack(side=tk.TOP, fill=tk.X)

        # 左下のボタン
        btn_inventory = tk.Button(self, text="InventoryPage", command=self.open_inventory_page)
        btn_inventory.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 右下のボタン
        btn_manage_order_product = tk.Button(self, text="ManageOrderProductPage", command=self.open_manage_order_product_page)
        btn_manage_order_product.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # 各ボタンのコマンド
    def open_order_page_t1(self):
        # T1のOrderPageに移動する処理を記述
        print("Moving to OrderPage for T1")

    def open_order_page_t2(self):
        # T2のOrderPageに移動する処理を記述
        print("Moving to OrderPage for T2")

    def open_order_page_t3(self):
        # T3のOrderPageに移動する処理を記述
        print("Moving to OrderPage for T3")

