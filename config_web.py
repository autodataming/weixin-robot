# coding=utf-8
__author__ = 'ruidong.wang@tsingdata.com'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

SITE_NAME = 'Weixin-Robot'

TEST = 'production'

USER_LOG_PATH = '/var/log/user-log/user_log.log'

UPLOAD_FOLDER = basedir + '/tmp/'
ALLOWED_IMG_EXTENSIONS = ['png','jpg','jpeg','gif','PNG','JPG','JPEG','GIF','bmp','BMP']

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
#
# if os.environ.get('DATABASE_URL') is None:
#     SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'app.db') +
#                                '?check_same_thread=False')
# else:
#     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# SQLALCHEMY_RECORD_QUERIES = True
# WHOOSH_BASE = os.path.join(basedir, 'search.db')


DATABASE_QUERY_TIMEOUT = 0.5
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
SQLALCHEMY_DATABASE_URI = 'mysql://[username]:[password]@[ip]:3306/weixin_robot'
SQLALCHEMY_RECORD_QUERIES = True


# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = ''  # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = ''  # enter your MS translator app secret here



# pagination
POSTS_PER_PAGE = 50
MAX_SEARCH_RESULTS = 50

LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

AIML_SET = os.path.join(os.path.dirname(__file__),'app/aiml_set')
DEBUG = False
BOT_PROPERTIES = {
    "name":"@xdtuxbot",
    "master":"silence",
    "birthday":"地球时间2017年5月10日",
    "orgnization":"计算机工程系",
    "univercity":"太原工业学院",
    "gender":"男生",
    "city":"太原",
    "os":"Linux",
}

#tuling机器人api key
TULING_API_KEY = '[tuling机器人api]'

WEI_XIN_TOKEN= '[weixin_token]'
WEI_XIN_APP_ID = '[weixin_app_id]'
WEI_XIN_APP_SECRET = '[weixin_app_id_secret]'