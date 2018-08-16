from db import db_handler
from interface import bank
from lib import common

shopping_logger = common.get_logger('shopping')

#查看购物车接口
def check_shoppingcart_interface(name):
    user_dic = db_handler.select(name)
    shopping_logger.info('%s查看了购物车' %name)
    return user_dic['shoppingcar']


#购物接口
def shopping_interface(name,cost,shoppingcar):
    flag,msg = bank.consume_interface(name,cost)
    if flag:
        user_dic = db_handler.select(name)
        user_dic['shoppingcar'] = shoppingcar
        db_handler.save(user_dic)
        shopping_logger.info('%s成功购买了商品' %name)
        return True,'购买成功!'
    else:
        return False,msg






