import tkinter as tk

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MainPage")
        self.geometry("400x300")

        # ボタンを作成して配置
        self.create_buttons()

    def create_buttons(self):
        # 上半分のフレーム
        frame_top = tk.Frame(self)
        frame_top.pack(side=tk.TOP, fill=tk.X)

        # T1からT3までのボタンを横に並べる
        btn_t1 = tk.Button(frame_top, text="T1", command=self.open_order_page_t1, width=15, height=7)
        btn_t1.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=10)

        btn_t2 = tk.Button(frame_top, text="T2", command=self.open_order_page_t2, width=15, height=7)
        btn_t2.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=10)

        btn_t3 = tk.Button(frame_top, text="T3", command=self.open_order_page_t3, width=15, height=7)
        btn_t3.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=10)

        # 下半分のフレーム
        frame_bottom = tk.Frame(self)
        frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # 左下のボタン
        btn_inventory = tk.Button(frame_bottom, text="InventoryPage", command=self.open_inventory_page, width=15, height=1)
        btn_inventory.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=30, expand=True)

        # 右下のボタン
        btn_manage_order_product = tk.Button(frame_bottom, text="ManageOrderProductPage", command=self.open_manage_order_product_page, width=15, height=1)
        btn_manage_order_product.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=30, expand=True)

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

    def open_inventory_page(self):
        # InventoryPageに移動する処理を記述
        print("Moving to InventoryPage")

    def open_manage_order_product_page(self):
        # ManageOrderProductPageに移動する処理を記述
        print("Moving to ManageOrderProductPage")

if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
