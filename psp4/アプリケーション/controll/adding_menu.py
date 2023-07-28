from DAO.StockDAO import StockDAO
from entity.Inventory import Inventory

def adding_menu(menu_name, kind, price, quantity):
    new_menu = Inventory(menu_name, kind, quantity, price)
    StockDAO().add_item(new_menu)
