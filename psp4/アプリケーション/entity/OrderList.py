class OrderList:
    def __init__(self):
        self.product_name_list = []

    def add_product(self, product_name):
        self.product_name_list.append(product_name)

    def get_low_stock_products(self, stock_dao):
        low_stock_products = []
        for product_name in self.product_name_list:
            item = stock_dao.get_item_by_name(product_name)
            if item and item.quantity <= 5:
                low_stock_products.append(item)
        return low_stock_products
