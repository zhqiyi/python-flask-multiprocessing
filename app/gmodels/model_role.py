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
from ..utils.db import (Base, Column, Integer, String, DateTime, BigInteger, TEXT, BIGINT, FLOAT, ForeignKey, JSONB,
                        relationship)


class _Role(Base):
    __tablename__ = 't_role'

    _id = Column('id', Integer, autoincrement=True, primary_key=True, nullable=False)
    _role = Column('role', String(50), nullable=False, unique=True)

    def __init__(self, **kwargs):
        super(_Role, self).__init__(**kwargs)


    # def __repr__(self):
    #     return '<_Role %r, %r>' % (self._id, self._role)

    @property
    def id(self):
        return self._id

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value