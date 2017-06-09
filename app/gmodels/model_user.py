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
from werkzeug.security import (generate_password_hash, check_password_hash)
from ..utils.db import (Base, Column, Integer, String, DateTime, BigInteger, TEXT, BIGINT, FLOAT, ForeignKey, JSONB,
                        relationship)

class _User(Base):
    __tablename__ = 't_user'

    _id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    _username = Column('username', String(50), nullable=True, unique=True)
    _username_zh = Column('username_zh', String(50), nullable=False)
    _user_age = Column('user_age', Integer, nullable=False)
    _password =  Column('password', String(150), nullable=False)
    _role =  Column('role', Integer, ForeignKey('t_role.id'))

    def __init__(self, **kwargs):
        super(_User, self).__init__(**kwargs)

    # def __repr__(self):
    #     mes = '<_User %s, %s)>' % (self._username, self._role)
    #     return mes

    # @property
    # def id(self):
    #     return self._id

    # @id.setter
    # def id(self, value):
    #     raise AttributeError('id( is not a writeable attribute.')

    @property
    def user_age(self):
        return self._user_age

    @user_age.setter
    def user_age(self, value):
        self._user_age = value

    @property
    def username_zh(self):
        return self._username_zh

    @username_zh.setter
    def username_zh(self, value):
        self._username_zh = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, value):

        if not isinstance(value, str):
            raise ValueError('password must be a string.')

        if len(value) > 16 and len(value) < 6:
            raise ValueError('password\'s length must between 6 to 16.')

        self._password = generate_password_hash(value)

    @property
    def role(self):
        return self._role

    @password.setter
    def role(self, value):
        self._role = value

    def verify_password(self, password):
        return check_password_hash(password)
