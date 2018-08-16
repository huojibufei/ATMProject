from interface import user, bank, shopping
from db import db_handler
from lib import common

user_info = {
    'name': None
}


def login():
    if user_info['name']:
        print('已登录!')
        return
    print('登录')
    count = 0
    while True:
        name = input('请输入用户名(输入q退出):').strip()
        if name == 'q': break
        password = input('请输入密码:').strip()
        flag, msg = user.login_interface(name, password)
        if flag:
            print(msg)
            user_info['name'] = name
            break
        else:
            print(msg)
            count += 1
            if count >= 3:
                print(user.lock_user(name))


def register():
    if user_info['name']:
        print('已登录!')
        return
    print('注册')
    while True:
        name = input('请输入用户名(输入q退出):').strip()
        if name == 'q': break
        password = input('请输入密码:').strip()
        password1 = input('请确认密码:').strip()
        if password == password1:
            flag, msg = user.register_interface(name, password)
            if flag:
                print(msg)
                user_info['name'] = name
                break
            else:
                print(msg)


@common.auth
def check_balance():
    print('查看余额')
    balance = bank.check_balance_interface(user_info['name'])
    print('您的余额为:%s' % balance)


@common.auth
def transfer():
    print('转账')
    while True:
        payee = input('请输入收款方账户名(输入q退出):').strip()
        if payee == 'q': break
        user_dic = db_handler.select(payee)
        if user_dic:
            money = input('请输入转账金额:!')
            if money.isdigit():
                money = int(money)
                flag, msg = bank.transfer_interface(user_info['name'], payee, money)
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print('请输入整数金额!')
        else:
            print('收款方不存在!')


@common.auth
def repay():
    print('还款')
    money = input('请输入还款金额(输入q退出):').strip()
    if money == 'q': return
    if money.isdigit():
        money = int(money)
        flag, msg = bank.repay_interface(user_info['name'], money)
        if flag:
            print(msg)
    else:
        print('请输入整数金额!')


@common.auth
def withdraw():
    print('取款')
    while True:
        money = input('请输入取款金额(输入q退出):').strip()
        if money == 'q': break
        if money.isdigit():
            money = int(money)
            flag, msg = bank.withdraw_interface(user_info['name'], money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输入整数金额!')


@common.auth
def check_record():
    print('查看流水')
    records = bank.check_record_interface(user_info['name'])
    for record in records:
        print(record)


@common.auth
def shop():
    '''
    1 先循环打印出商品
    2 用户输入数字选择商品（判断是否是数字，判断输入的数字是否在范围内）
    3 取出商品名，商品价格
    4 判断用户余额是否大于商品价格
    5 余额大于商品价格时，判断此商品是否在购物车里
        5.1 在购物车里，个数加1
        5.1 不在购物车里，拼出字典放入（｛‘car’：｛‘price’：1000，‘count’：2｝,‘iphone’：｛‘price’：10，‘count’：1｝｝）
    6 用户余额减掉商品价格
    7 花费加上商品价格
    8 当输入 q时，购买商品
        8.1 消费为0 ，直接退出
        8.2 打印购物车
        8.3 接受用户输入，是否购买 当输入y，直接调购物接口实现购物
    :return:
    '''
    print('购物')
    goods_list = [
        ['coffee', 10],
        ['chicken', 20],
        ['iphone', 8000],
        ['macPro', 15000],
        ['car', 100000]
    ]
    cost = 0
    shoppingcar = {}
    user_balance = bank.check_balance_interface(user_info['name'])

    while True:
        for i, k in enumerate(goods_list):
            print('%s:%s' % (i, k))
        choice = input('请输入购买的商品序号(输入q结算):').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(goods_list):
                good_name = goods_list[choice][0]
                good_price = goods_list[choice][1]
                if user_balance >= good_price:
                    if good_name in shoppingcar:
                        shoppingcar[good_name]['count'] += 1
                    else:
                        shoppingcar[good_name] = {'price': good_price, 'count': 1}
                    user_balance -= good_price
                    cost += good_price


                else:
                    print('余额不足!')

            else:
                print('输入越界,请重新输入!')

        elif choice == 'q':
            if cost == 0:
                print('未购买商品!')
                break
            choice_bool = input('确认购买(y/n)?')
            if choice_bool == 'y':
                flag, msg = shopping.shopping_interface(user_info['name'], cost, shoppingcar)
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
                    break


            elif choice_bool == 'n':
                print('取消购买!')
                break
            else:
                print('请输入y/n !')


        else:
            print('输入非法请重新输入!')


@common.auth
def check_shoppingcart():
    print('查看购买商品')
    shoppingcar = shopping.check_shoppingcart_interface(user_info['name'])
    print(shoppingcar)


def logout():
    user_info['name'] = None


func_dic = {
    '1': login,
    '2': register,
    '3': check_balance,
    '4': transfer,
    '5': repay,
    '6': withdraw,
    '7': check_record,
    '8': shop,
    '9': check_shoppingcart,
    '10': logout
}


def run():
    while True:
        print('''
        0 退出程序
        1 登录
        2 注册
        3 查看余额
        4 转账
        5 还款
        6 取款
        7 查看流水
        8 购物
        9 查看购买商品        
        10 注销        
        ''')
        choice = input('请选择:').strip()
        if choice == '0': break
        if choice not in func_dic: continue
        func_dic[choice]()
