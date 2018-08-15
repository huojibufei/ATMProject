from interface import user, bank
from db import db_handler
from lib import common

user_info = {'name': None}


#1 注册
def register():
    if user_info['name']:
        print('您已登录!')
        return
    print('注册')
    while True:
        name = input('请输入用户名(输入q退出):').strip()
        if name == 'q': break
        password = input('请输入密码:').strip()
        conf_password = input('请确认密码:').strip()
        if password == conf_password:
            flag, msg = user.register_interface(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break
        else:
            print('两次密码不一致,请重新输入!')


#2 登录
def login():
    if user_info['name']:
        print('您已登录!')
        return
    print('登录')
    while True:
        name = input('请输入用户名(输入q退出):').strip()
        if name == 'q': break
        flag, msg = user.login_interface(name)
        if flag:
            print(msg)
            user_info['name'] = name
            break
        else:
            print(msg)


#3 查看余额
@common.auth
def check_balance():
    print('查看余额')
    balance = bank.check_balance_interface(user_info['name'])
    print('您的余额为%s' % balance)


#4 转账
@common.auth
def transfer():
    print('转账')
    while True:
        payee = input('请输入收款方:').strip()
        transfer_amount = input('请输入转账金额:').strip()
        if transfer_amount.isdigit():
            transfer_amount = int(transfer_amount)
            flag, msg = bank.transfer_interface(user_info['name'], payee, transfer_amount)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输入整数的转账金额!')


#5 还款
@common.auth
def repay():
    print('还款')
    pass


#6 取款
@common.auth
def withdraw():
    print('取款')
    while True:
        money = input('请输入取款金额:').strip()
        if money.isdigit():
            money = int(money)
            flag, msg = bank.withdraw_interface(user_info['name'], money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输入整数的取款金额!')


#7 查看流水
def check_record():
    print('查看流水')
    data = bank.check_record_interface(user_info['name'])
    for item in data:
        print(item)




#8 购物
def shop():
    print('购物')
    pass




#9 查看购买商品
def check_shopping_cart():
    print('查看购买商品')
    pass





func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': transfer,
    '5': repay,
    '6': withdraw,
    '7':check_record,
    '8':shop,
    '9':check_shopping_cart
}


def run():
    while True:
        print('''
        0 退出
        1 注册
        2 登录
        3 查看余额
        4 转账
        5 还款
        6 取款
        7 查看流水
        8 购物
        9 查看购买商品
        
        ''')
        choice = input('请输入您选择的操作:').strip()
        if choice == '0': break
        if choice not in func_dic: continue
        func_dic[choice]()
