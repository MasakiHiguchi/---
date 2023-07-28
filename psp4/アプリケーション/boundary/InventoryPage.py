import tkinter as tk
from tkinter import messagebox
from DAO.StockDAO import StockDAO
from AddMenuPage import AddMenuPage

class InventoryPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("在庫ページ")
        self.geometry("800x400")

        self.stock_dao = StockDAO()

        self.create_widgets()

    def create_widgets(self):
        # StockDAOの情報を表示するフレームを作成
        frame_stock_info = tk.Frame(self)
        frame_stock_info.pack(side=tk.TOP, pady=20)

        # StockDAOの情報を表示
        for item in self.stock_dao.get_all_items():
            lbl_item = tk.Label(frame_stock_info, text=f"{item.name}:")
            lbl_item.pack(side=tk.LEFT)
            entry_quantity = tk.Entry(frame_stock_info, width=10)
            entry_quantity.insert(tk.END, item.quantity)
            entry_quantity.pack(side=tk.LEFT, padx=5)

        # 下部にボタンを配置
        btn_confirm = tk.Button(self, text="確定", command=self.confirm)
        btn_confirm.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X)

        btn_add_menu = tk.Button(self, text="新メニュー追加", command=self.open_add_menu_page)
        btn_add_menu.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X)

        btn_return = tk.Button(self, text="戻る", command=self.return_to_main_page)
        btn_return.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.X)

    def return_to_main_page(self):
        self.destroy()
        from MainPage import MainPage
        self.main_page = MainPage()
        self.main_page.mainloop()

    def open_add_menu_page(self):
        self.withdraw()  # InventoryPageを隠す
        add_menu_page = AddMenuPage(self)  # AddMenuPageを開く
        add_menu_page.mainloop()

    def confirm(self):
        # 確定ボタンの処理を行う
        messagebox.showinfo("確認", "在庫が確定されました。")

if __name__ == "__main__":
    app = InventoryPage()
    app.mainloop()
