#在庫管理
#在庫クラスは [種類、名前、値段、個数]で表示
class stock_data:

    def __init__(self, kind, name, number, price):
        self.kind = kind
        self.name = name
        self.number = number
        self.price = price

    def stock_management_number(self, x):
        self.number += x 
        #これまでの在庫の数からxだけ変化させる

    def stock_management_name(self, x):
        self.name = x
        #これまでの在庫（メニュー）の名前をxに変更する

    def stock_management_price(self, x):
        self.price = x
        #これまでの在庫（メニュー）の価格をxに変更する

    def stock_management_kind(self, x):
        self.name = x
        #これまでの在庫（メニュー）の種類をxに変更する

    def print_data(self):
        print("{},{},{},{}".format(self.kind, self.name, self.number, self.price))
        #商品の情報を表示

    #if 
    #少ない商品は発注・仕込みリストに追加

def create_instance(cls, arg1, arg2, arg3, arg4):
    new_instance = cls(arg1, arg2, arg3, arg4)
    return new_instance
    #新しく[stock_data]クラスのインスタンスを生成

newmenu = create_instance(stock_data, "food", "yakitori", 30, 200)
    #生成したインスタンスを新メニューとする 


beer = stock_data("drink", "beer", 30, 400) 
beer.print_data()
newmenu.print_data()