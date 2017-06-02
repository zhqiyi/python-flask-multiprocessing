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
import simplejson as json
from ..utils.db import (Base, Column, Integer, String, DateTime, BigInteger, TEXT, BIGINT, FLOAT, ForeignKey, JSONB,
                        relationship)

class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column('username', String(50), primary_key=False, nullable=False)
    username_zh = Column('username_zh', String(50), primary_key=False, nullable=False)
    user_age = Column('user_age', Integer, primary_key=False, nullable=False)
    password =  Column('password', String(150), primary_key=False, nullable=False)

    def __init__(self, id=None, username=None, username_zh=None, user_age=None, password=None):
        self.id = id
        self.username = username
        self.username_zh = username_zh
        self.user_age = user_age
        self.password = password

    def __repr__(self):
        return "<User('{0}','{1}','{2}','{3}','{4}')>" % self.id, \
               self.username, self.username_zh, self.user_age, self.password

    '''
        API for User
    '''

    @staticmethod
    def add(app=None, db=None, username=None, username_zh=None, user_age=None, password=None):
        '''

        :param g: flask_app's g
        :param username: The english name
        :param username_zh: The chinese name
        :param user_age: User age
        :param password: User's password
        :return:
        '''
        result = {"status": "", "message": ""}

        if app is None or db is None:
            result["status"] = False
            result["message"] = app.lang.com_msg.__getitem__('Err_app_and_db')
            return result

        if username is None or password is None or username == '' or password == '':
            result["status"] = False
            result["message"] = app.lang.com_msg.__getitem__('Err_add_user')
            return result

        return True

    @staticmethod
    def delete():
        return True

    @staticmethod
    def modify():
        return True

    @staticmethod
    def query():
        return True

    '''
        Private method
    '''