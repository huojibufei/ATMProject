from db import db_handler
from lib import common

user_logger = common.get_logger('user')

#注册接口
def register_interface(name,password,balance = 15000):
    user_dic = {'name': name, 'password': password, 'balance': balance, 'credit': balance, 'locked': False,
                'bankflow': [], 'shoppingcart': {}}
    db_handler.save(user_dic)
    user_logger.info('%s注册了' %name)
    return True,'注册成功!'


# 登录接口
def login_interface(name,password):
    user_dic = db_handler.select(name)
    if user_dic['password'] == password:
        user_logger.info('%s登录了' % name)
        return True,'登陆成功!'
    else:
        return False,'密码错误或已被锁定!'


# 锁定用户接口
def lock_user(name):
    user_dic = db_handler.select(name)
    user_dic['lock'] = True
    db_handler.save(user_dic)
    user_logger.info('%s被锁定了' %name)
    return '用户已被锁定!'


# 解锁用户接口
def unlock_user(name):
    user_dic = db_handler.select(name)
    user_dic['lock'] = False
    db_handler.save(user_dic)
    user_logger.info('%s被解锁了' %name)
    return '用户已被解锁!'


