from db import db_handler
from lib import common

bank_log = common.get_logger('bank')

def check_balance_interface(name):
    user_dic = db_handler.select(name)
    return user_dic['balance']


def withdraw_interface(name,money):
    user_dic = db_handler.select(name)
    if user_dic['balance'] >= money * 1.05:
        user_dic['balance'] -= money * 1.05
        user_dic['bankflow'].append('[您取款%s元]' %money)
        db_handler.save(user_dic)
        bank_log.info('[%s取款%s元]' %(name,money))
        return True,'取款成功!'
    else:
        return False,'余额不足!'


def transfer_interface(name,payee,transfer_amount):
    user_dic = db_handler.select(name)
    user_dic1 = db_handler.select(payee)
    if user_dic['balance'] >= transfer_amount:
        user_dic['balance'] -= transfer_amount
        user_dic1['balance'] += transfer_amount
        user_dic['bankflow'].append('[您向%s转账%s元]' %(payee,transfer_amount))
        user_dic1['bankflow'].append('[%s向您转账%s元]' %(name,transfer_amount))
        db_handler.save(user_dic)
        db_handler.save(user_dic1)
        bank_log.info('[%s给%s转账%s元]' %(name,payee,transfer_amount))

        return True,'转账成功!'
    else:
        return False,'余额不足!'


def check_record_interface(name):
    user_dic = db_handler.select(name)
    return user_dic['bankflow']







