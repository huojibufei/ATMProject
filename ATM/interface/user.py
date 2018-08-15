from db import db_handler
from lib import common

user_log = common.get_logger('user')

def register_interface(name, password, balance=15000):
    user = db_handler.select(name)
    if user:
        return False, '用户名已存在,请登录!'

    user_dic = {'name': name, 'password': password, 'balance': balance, 'credit': balance,'lock':False,'bankflow':[],'shoppingcar':[]}

    db_handler.save(user_dic)
    user_log.info('[%s注册了]' %name)
    return True, '注册成功!'

count = 0

def login_interface(name):
    while True:
        user_dic = db_handler.select(name)
        if user_dic:
                password = input('请输入密码:').strip()
                if password == user_dic['password'] and not user_dic['lock']:
                    user_log.info('[%s登录了]' %name)
                    return True,'登录成功!'
                else:
                    global count
                    count += 1
                    if count == 3:
                        user_dic['lock'] = True
                        db_handler.save(user_dic)

                    return False,'密码错误或已被锁定!'

        else:
            return False,'该用户未注册,请前往注册!'
