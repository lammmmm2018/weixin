#coding=utf8

TOKEN = 'Token'
APP_ID = 'wx68d57a9432660cb2'
SECRET_KEY = '03481467f2ce08b345a7634d0794a043'
TULING_KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
ADMIN_OAUTH = 'admin_oauth'
WELCOME_WORD = u'''\
欢迎关注我的微信号！
回复下列内容获取对应信息：
目录： 获取文章目录的网址
帮助： 获取本信息
其他： 图灵机器人会陪你聊天'''
INDEX_URL = 'http://mumushow.applinzi.com'
REPLY_DICT = {
    u'目录': '点这里-> ' + INDEX_URL,
    u'帮助': WELCOME_WORD,
}
MENU = {}
ARTICLES_DIR = 'articles'
ARTICLES_NAME = 'articles.json'
BASE_URL = 'https://api.weixin.qq.com/cgi-bin'
#sss