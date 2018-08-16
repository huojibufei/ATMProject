from db import db_handler
from lib import common

bank_logger = common.get_logger('bank')

#检查余额接口
def check_balance_interface(name):
    user_dic = db_handler.select(name)
    bank_logger.info('%s查询了余额' %name)
    return user_dic['balance']

#转账接口
def transfer_interface(name,payee,money):
    user_dic = db_handler.select(name)
    user_dic1 = db_handler.select(payee)
    if user_dic['balance'] >= money:
        user_dic['balance'] -= money
        user_dic['bankflow'].append('您给%s转账%s元' %(payee,money))
        user_dic1['balance'] += money
        user_dic['bankflow'].append('%s给您转账%s元' %(name,money))
        db_handler.save(user_dic1)
        db_handler.save(user_dic)
        bank_logger.info('%s给%s转账%s元' %(name,payee,money))
        return True,'转账成功!'

    else:
        return False,'余额不足!'




# 还款接口
def repay_interface(name,money):
    user_dic = db_handler.select(name)
    user_dic['balance'] += money
    user_dic['bankflow'].append('您还款%s元' % money)
    db_handler.save(user_dic)
    bank_logger.info('%s还款%s元' % (name,money))
    return True,'还款成功!'


# 取款接口
def withdraw_interface(name,money):
    user_dic = db_handler.select(name)
    if user_dic['balance'] >= money:
        user_dic['balance'] -= money
        user_dic['bankflow'].append('您取款%s元' %money)
        db_handler.save(user_dic)
        bank_logger.info('%s取款%s元' % (name, money))
        return True,'取款成功!'
    else:
        return False,'余额不足!'





# 查看流水接口
def check_record_interface(name):
    user_dic = db_handler.select(name)
    bank_logger.info('%s查看了流水' %name)
    return user_dic['bankflow']


# 扣款接口
def consume_interface(name,money):
    user_dic = db_handler.select(name)
    if user_dic['balance'] >= money:
        user_dic['balance'] -= money
        user_dic['bankflow'].append('您消费%s元' %money)
        db_handler.save(user_dic)
        bank_logger.info('%s消费%s元' %(name,money))
        return True,'扣款成功!'
    else:
        return False,'余额不足!'





