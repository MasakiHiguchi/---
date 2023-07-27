# StockDAO.py

# Inventory.pyからInventoryクラスをインポート
from entity.Inventory import Inventory
from Inventory import Inventory

class StockDAO:
    def __init__(self):
        # データベースや永続化されたデータに接続するなどの初期化処理をここに記述
        # このサンプルでは、データベースを使わずに、一時的なリストでデータを管理します
        self.inventory_list = []

    def add_item(self, item):
        # アイテムをデータベースに追加する処理をここに記述
        self.inventory_list.append(item)

    def get_all_items(self):
        # 全てのアイテムを取得する処理をここに記述
        return self.inventory_list

    def get_item_by_name(self, name):
        # 名前でアイテムを検索して取得する処理をここに記述
        for item in self.inventory_list:
            if item.name == name:
                return item
        return None

    def update_item_quantity(self, name, new_quantity):
        # アイテムの数量を更新する処理をここに記述
        for item in self.inventory_list:
            if item.name == name:
                item.update_quantity(new_quantity)
                return True
        return False

    def update_item_price(self, name, new_price):
        # アイテムの価格を更新する処理をここに記述
        for item in self.inventory_list:
            if item.name == name:
                item.update_price(new_price)
                return True
        return False
    
    def add_new_menu(self, name, kind, price):
        # kindの値が"food"か"drink"でない場合はエラーを発生させる
        if kind not in ["food", "drink"]:
            raise ValueError("Invalid kind. Kind must be 'food' or 'drink'.")

        new_menu = Inventory(name, kind, 0, price)
        self.add_item(new_menu)