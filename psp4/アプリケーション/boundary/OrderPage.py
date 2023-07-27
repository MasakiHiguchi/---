import sys
import os

# "main_folder" の絶対パスを取得
main_folder_path = os.path.dirname(os.path.abspath(__file__))
# "DAO" フォルダのパスを取得して、sys.path に追加
dao_folder_path = os.path.join(main_folder_path, "DAO")
sys.path.append(dao_folder_path)
# "boundary" フォルダのパスを取得して、sys.path に追加
boundary_folder_path = os.path.join(main_folder_path, "..")
sys.path.append(boundary_folder_path)
# "entity" フォルダのパスを取得して、sys.path に追加
entity_folder_path = os.path.join(main_folder_path, "..", "entity")
sys.path.append(entity_folder_path)

import sys
import os

# "main_folder" の絶対パスを取得
main_folder_path = os.path.dirname(os.path.abspath(__file__))
# "DAO" フォルダのパスを取得して、sys.path に追加
dao_folder_path = os.path.join(main_folder_path, "DAO")
sys.path.append(dao_folder_path)
# "entity" フォルダのパスを取得して、sys.path に追加
entity_folder_path = os.path.join(main_folder_path, "..", "entity")
sys.path.append(entity_folder_path)

from DAO.StockDAO import StockDAO
from entity.Order import Order
from entity.Total import Total
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# OrderPage.py




class OrderPage(tk.Tk):
    def __init__(self, table_name):
        super().__init__()

        self.title("OrderPage")
        self.geometry("800x600")

        self.table_name = table_name
        self.stock_dao = StockDAO()
        self.order_list = []
        self.total_amount = 0

        self.create_widgets()

    def create_widgets(self):
        # 左上のフレーム
        self.frame_left_top = tk.Frame(self)
        self.frame_left_top.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 右のフレームを横に２分割
        self.frame_right = tk.Frame(self)
        self.frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # 右上のフレーム
        self.frame_right_top = tk.Frame(self.frame_right)
        self.frame_right_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # 右下のフレームを縦に２分割
        self.frame_right_bottom = tk.Frame(self.frame_right)
        self.frame_right_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # 左上のフレームに在庫アイテムのボタンを表示
        self.create_inventory_buttons()

        # 右上のフレームに「注文リスト」とボタンを表示
        self.create_order_list_widgets()

        # 右下のフレームに「合計金額」、キャンセルボタン、決定ボタンを表示
        self.create_total_widgets()

    def create_inventory_buttons(self):
        self.frame_left_top.grid_rowconfigure(0, weight=1)
        self.frame_left_top.grid_rowconfigure(1, weight=1)
        self.frame_left_top.grid_rowconfigure(2, weight=1)
        self.frame_left_top.grid_rowconfigure(3, weight=1)
        self.frame_left_top.grid_rowconfigure(4, weight=1)

        self.frame_left_top.grid_columnconfigure(0, weight=1)

        self.inventory = self.stock_dao.get_all_items()
        for i, item in enumerate(self.inventory):
            btn = tk.Button(self.frame_left_top, text=item.name, command=lambda item=item: self.place_order(item))
            btn.grid(row=i, column=0, sticky=tk.NSEW)

    def place_order(self, item):
        order = next((o for o in self.order_list if o.name == item.name), None)
        if order:
            order.quantity += 1
        else:
            order = Order(item.name, 1, 0)
            self.order_list.append(order)

        item.update_quantity(item.quantity - 1)
        self.update_quantity_display()

    def update_quantity_display(self, event=None):
        selected_index = self.lst_order.curselection()
        if selected_index:
            index = selected_index[0]
            order = self.order_list[index]
            self.lbl_quantity.config(text=f"数量: {order.quantity}")

    def filter_by_kind(self, kind):
        filtered_inventory = [item for item in self.inventory if item.kind == kind]
        self.clear_left_frame()
        for i, item in enumerate(filtered_inventory):
            btn = tk.Button(self.frame_left_top, text=item.name, command=lambda item=item: self.place_order(item))
            btn.grid(row=i, column=0, sticky=tk.NSEW)

    def clear_left_frame(self):
        for widget in self.frame_left_top.winfo_children():
            widget.destroy()

    def create_order_list_widgets(self):
        lbl_order_list = tk.Label(self.frame_right_top, text="注文リスト", font=("Helvetica", 16))
        lbl_order_list.pack(side=tk.TOP, pady=10)

        self.lst_order = tk.Listbox(self.frame_right_top, selectmode=tk.SINGLE)
        self.lst_order.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.lst_order.bind("<<ListboxSelect>>", self.update_quantity_display)

        self.frame_right_top.grid_columnconfigure(0, weight=1)

    def create_total_widgets(self):
        lbl_total_amount = tk.Label(self.frame_right_bottom, text="合計金額", font=("Helvetica", 16))
        lbl_total_amount.pack(side=tk.TOP, pady=5)

        self.lbl_total_amount_value = tk.Label(self.frame_right_bottom, text="", font=("Helvetica", 14))
        self.lbl_total_amount_value.pack(side=tk.TOP)

        btn_cancel = tk.Button(self.frame_right_bottom, text="キャンセル", command=self.cancel_order)
        btn_cancel.pack(side=tk.TOP, padx=10, pady=30, fill=tk.X)

        btn_confirm = tk.Button(self.frame_right_bottom, text="決定", command=self.confirm_order)
        btn_confirm.pack(side=tk.TOP, padx=10, pady=30, fill=tk.X)

        self.frame_right_bottom.grid_columnconfigure(0, weight=1)

    def calculate_total_amount(self):
        total_amount = 0
        for order in self.order_list:
            item = self.stock_dao.get_item_by_name(order.name)
            total_amount += item.price * order.quantity
        self.total_amount = total_amount
        self.lbl_total_amount_value.config(text=f"${total_amount}")

    def cancel_order(self):
        if self.order_list:
            for order in self.order_list:
                item = self.stock_dao.get_item_by_name(order.name)
                item.update_quantity(item.quantity + order.quantity)
            self.order_list = []
            self.lst_order.delete(0, tk.END)
            self.lbl_quantity.config(text="")
            self.total_amount = 0
            self.lbl_total_amount_value.config(text="")
        # MainPageに戻る
        self.destroy()

    def confirm_order(self):
        if not self.order_list:
            messagebox.showwarning("注文エラー", "注文がありません。")
            return

        deposit_amount = 0
        while True:
            try:
                deposit_amount = int(input("お預かり金額を入力してください: "))
                if deposit_amount < self.total_amount:
                    print("お預かり金額が合計金額よりも少ないです。")
                else:
                    break
            except ValueError:
                print("無効な値です。数値を入力してください。")

        change = deposit_amount - self.total_amount

        total = Total(self.table_name, self.total_amount, deposit_amount, change)
        print(total)
        # Tableクラスのtotal_amountに数値を足す処理を実装
        table = self.table_dao.get_table_by_name(self.table_name)
        table.total_amount += self.total_amount
        # 他の処理
        self.cancel_order()
        # 以下を追加してOrderPageを閉じる
        self.destroy()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = OrderPage("T1")
    app.run()