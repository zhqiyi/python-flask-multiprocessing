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

from .gmodels.model_user import _User as User
from .gmodels.model_role import _Role as Role

class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80

''' Table's mapping '''
mapped_class_dic = dict(
                        t_role=Role,
                        t_user=User
                        )