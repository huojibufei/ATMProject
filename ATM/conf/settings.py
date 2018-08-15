import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#数据文件路径
BASE_DB = os.path.join(BASE_DIR, 'db')

#日志模块路径
BASE_LOG = os.path.join(BASE_DIR,'log')

# 日志相关的配置
standard_format = '%(asctime)s - task:%(name)s - %(filename)s:%(lineno)d -' \
                  ' %(levelname)s : [%(message)s]'

simple_format = '%(filename)s:%(lineno)d - %(levelname)s : [%(message)s]'


#如果不存在定义的日志目录就创建一个
if not os.path.isdir(BASE_LOG):
    os.mkdir(BASE_LOG)

#log文件的全路径
logfile_path = os.path.join(BASE_LOG,'log.log')


# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到终端
            'formatter': 'simple'
        },
        #打印到a1.log文件的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件的路径
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        '': {
            'handlers': ['default','console'],
            'level': 'DEBUG',
        },
    },
}
