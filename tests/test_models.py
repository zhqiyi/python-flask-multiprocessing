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
from app.apps import create_app
from app.models import User


class ModelsAPITest(unittest.TestCase):

    def setUp(self):
        app, db = create_app('test_app', 'testing')
        self.app = app
        self.db = db.make_session()
        self.app_context = self.app.app_context()
        self.app_context.push()
        # self.db.create_all()


    def tearDown(self):
        self.db.close()
        # self.db.drop_all()
        self.app_context.pop()

    def test_user_add(self):
        u = User(username='yizhq', username_zh='仪智奇', user_age=15, password='123456789')
        self.db.add(u)
        self.db.commit()
