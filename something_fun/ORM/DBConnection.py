import pymysql
import configparser
import os

class DB:
    path = './db.conf'

    conf = configparser.ConfigParser()

    modifide = ''

    config = 1

    def isConfigModified(self):
        if os.stat(self.path).st_mtime == self.modifide:
            return False
        self.modifide = os.stat(self.path)
        return True

    def read(self):
        DB.conf.read('./db.conf')
        self.config = {'host': self.conf.get('db', 'db_host'), 'port': self.conf.get('db', 'db_port'), 'user': self.conf.get('db', 'db_user'),
              'pass': self.conf.get('db', 'db_pass'), 'db': self.conf.get('db', 'db_database')}

    def getCon(self):
        if self.config == 1 or self.isConfigModified():
            self.read()
        config = self.config
        db = pymysql.connect(host=config['host'],
                             port=int(config['port']),
                             user=config['user'],
                             passwd=config['pass'],
                             db=config['db'],
                             charset='utf8'
                             )
        return db
