import pymysql
import configparser
import os


path = './db.conf'

conf = configparser.ConfigParser()


config = {}

def read():
    conf.read('./db.conf')
    config = {'host': conf.get('db', 'db_host'), 'port': conf.get('db', 'db_port'), 'user': conf.get('db', 'db_user'),
          'pass': conf.get('db', 'db_pass'), 'db': conf.get('db', 'db_database')}
    return config

def getCon():
    config = read()
    db = pymysql.connect(host=config['host'],
                         port=int(config['port']),
                         user=config['user'],
                         passwd=config['pass'],
                         db=config['db'],
                         charset='utf8'
                         )
    return db
