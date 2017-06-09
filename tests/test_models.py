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
import unittest
import random as rd
from app.apps import create_app, db
from app.models import (User, Role)


class ModelsAPITest(unittest.TestCase):

    def setUp(self):
        app = create_app('test_app', 'testing')
        self.app = app
        self.session = db.make_session()
        self.app_context = self.app.app_context()
        self.app_context.push()


    def tearDown(self):
        self.session.remove()
        self.app_context.pop()

    def test_user_add(self):
        # try:
        u = User(username = 'yizhq' + str(rd.randint(1, 100)),
                 username_zh ='仪智奇',
                 user_age = rd.randint(1, 58),
                 password = '123456789',
                 role = rd.randint(1, 3))
        self.session.add(u)
        self.session.commit()
        # except Exception as ex:
        #     print ex

    def test_user_query(self):
        us = self.session.query(User).all()
        for u in us:
            print u.username

    def test_role_add(self):
        r1 = Role(role='admin')
        r2 = Role(role='root')
        r3 = Role(role='oper')
        self.session.add(r1)
        self.session.add(r2)
        self.session.add(r3)
        self.session.commit()

    def test_user_modify(self):
        u = self.session.query(User).filter(User._user_age == 15).first()
        u.user_age = 23
        self.session.merge(u)
        self.session.commit()

    def test_user_delete(self):
        rs = self.session.query(User).filter(User._role == 1).delete(synchronize_session=False)
        print rs
        self.session.commit()