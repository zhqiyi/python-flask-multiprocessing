# -*- coding: utf-8 -*-
'''
# Author: Dave
# Email: yizhqi@gmail.com
#             
#                       __------__  
#                     /~           ~\  
#                    |     //^\\//^\|  
#                  /~~\   ||   o| |o|:~\  
#                 | |6    ||___|_|_||:|  
#                  \__.   /       o   \/'  
#                   |    (        O    )  
#          /~~~~\     `\   \          /  
#         | |~~\ |      )   ~------~`\  
#        /' |   | |    /      ____ /~~~)\  
#       (_/'    | | |      /'     |     ( |  
#              | | |      \     /    __)/ \  
#              \   \ \       \/     /' \    `\  
#                \   \|\         /    | |\___|  
#                  \ |   \____/      | |  
#                  /^~>   \         _/ <  
#                 |   |          \        \  
#                 |   | \         \         \  
#                 -^-\   \        |         )  
#                      `\_______/^\______/  
#
#               Please, Do not go wrong!!!
'''
import os
import logging
basedir = os.path.abspath(os.path.dirname(__file__))
workdir = "opt/work/web/xenwebsite/data/"

"""Base settings content"""
import time
import os
from lockfile import LockFile


def delete_old_lock_file(lock_filepath):
    real_path = lock_filepath + ".lock"
    if not os.path.exists(real_path):
        return
    try:
        stat = os.stat(real_path)
        current_time = time.time()
        if (current_time - stat.st_ctime) > 60:
            os.remove(real_path)
    except OSError:
        return

class Config:
    APP_CACHE = {'host': '10.75.0.61', 'port': 6379, 'db': 0}
    APP_SESSION = {'host': '10.75.0.61', 'port': 6379, 'db': 1}

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME=0.5
    '''
        语言设置
    '''
    LANGUAGE_SET = 'ZH'
    '''
        锁文件设置
    '''
    CONFIG_SETTINGS_DIR = basedir
    file_lock_path = os.path.join(CONFIG_SETTINGS_DIR, "file.lock")
    delete_old_lock_file(file_lock_path)
    PROCESS_FILE_LOCK = LockFile(file_lock_path)

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True

    ''' Logging settings '''
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filemode='a')

    ''' System settings '''
    '''
        时间服务器
    '''
    NTP_SERVER = 'pool.ntp.org'

    ''' Database settings '''
    SQLITE_DATABASE_URI = os.environ.get('DEV_SQLITE_URL') or \
                          'sqlite:///' + os.path.join(workdir, 'update.db')
    POSTGRESQL_DATABASE_URI = os.environ.get('DEV_POSTGRESQL_URL') or \
                              'postgresql://postgres:postgres@localhost:5432/pfmV01'


class TestConfig(Config):
    TESTING = True

    ''' Logging settings '''
    logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filemode='a')

    ''' System settings '''
    NTP_SERVER = 'pool.ntp.org'

    ''' Database settings '''
    SQLITE_DATABASE_URI = os.environ.get('DEV_SQLITE_URL') or \
                          'sqlite:///' + os.path.join(workdir, 'update.db')
    POSTGRESQL_DATABASE_URI = os.environ.get('DEV_POSTGRESQL_URL') or \
                              'postgresql://postgres:postgres@localhost:5432/pfmV01'


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


class UnixConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to syslog
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'unix': UnixConfig,

    'default': DevConfig
}