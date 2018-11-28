# -*- coding:utf-8 -*-
from export_data.DBConnection import *
import xlwt
from prettyprinter import pprint

accounts = ["sz_xhm", "liushuibbs", "szgmbwg", "zjgdhy", "SZXLHZX", "sz99gy", "yigong0512", "lxeye1",
            "szvorg", "scgylhh", "szjcgyf", "szwxysjlhh", "smartreadclub", "Firely-sz", "lao-lai-ban", "tczyzzh", "sztangmama",
            "da_huanbao", "zjgsertsg", "gh_7372d17b5f24", "gh_72f1216b6f2a", "enislandcn", "cvazjg0703", "gh_487b918866c3",
            "ksaxswx", "huiaijiayuan", "szzqfwzs", "kslxshe", "Suke_xfqx", "fuerguanai", "nuannuanaixingongyi", "yijialegongyi",
            "KSXWGC", "szgxqxy", "LoveZoneCF", "szlvpingguo", "homeinsuzhou0512", "gh_5748fd869191", "ks80she", "suzhanlawyer",
            "gh_095df242e177", "gh_0669683a2ec4", "smgy2000", "YER9958", "gh_89c584ff4316", "qimeng_it", "bbpp2014", "dfsc-sz",
            "xgy_gw", "gh_cfe8ac727ece", "gh_f5681a3998d9"]

account_nickname = {}
def get_nickname():
    conn = getCon()
    for account in accounts:
        sql = "select nickname from wsa_official_account where official_account=\'{0}\'".format(account)
        data = execute_sql(conn,sql)[0]
        account_nickname[account] = data[0]
    conn.close()

def execute_sql(conn,sql):
    cursor = conn.cursor()
    res = []
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        # print("execute successfully")
    except Exception as e:
        print(e)
        conn.rollback()
    return res


def get_articles():
    res = []
    conn = getCon()
    for account in accounts:
        sql = " select * from wsa_article where official_account=\'{0}\' and publish_time between \'2017-11-01\' and \'2018-11-01\' ".format(account)
        print(sql)
        data = execute_sql(conn,sql)
        for row in data:
            temp = (row[0],account_nickname[row[1]],row[1],str(row[2]),row[3])
            res.append(temp)
    conn.close()
    return res

def get_stats():
    articles = get_articles()
    conn = getCon()
    res = []
    for article in articles:
        sql = "select * from wsa_article_stats s where s.article_id ={0} and s.read_count=(select max(a.read_count) from wsa_article_stats a where a.article_id = {1} group by a.article_id)".format(article[0],article[0])
        print(sql)
        data = execute_sql(conn,sql)[0]
        temp = article + (data[2],data[3])
        res.append(temp)
    conn.close()
    return res

def get_article_map():
    res = {}
    conn = getCon()
    for account in accounts:
        sql = " select id,publish_time from wsa_article where official_account=\'{0}\' and publish_time between \'2017-11-01\' and \'2018-11-01\' ".format(account)
        data = execute_sql(conn,sql)
        temp = []
        for row in data:
            month = str(row[1])[5:7]
            temp.append((month,str(row[0])))
        res[account] = temp
    conn.close()
    return res

class month_info:
    def __init__(self,account,month,read_num,like_num):
        self.account = account
        self.month = month
        self.read_num = read_num
        self.like_num = like_num
        self.nickname = account_nickname[account]

def get_stats_sum():
    articles = get_article_map()
    conn = getCon()
    res = []
    for account_article in articles.items():
        base_sql = "select read_count,like_count from wsa_article_stats s where s.article_id ={0} and s.read_count=(select max(a.read_count) from wsa_article_stats a where a.article_id = {1} group by a.article_id)"
        for month_id in account_article[1]:
            sql = base_sql.format(month_id[1],month_id[1])
            data = execute_sql(conn, sql)[0]
            try:
                res.append((account_article[0],int(month_id[0]),int(data[0]),int(data[1])))
            except:
                continue
    conn.close()
    return res

def main():
    get_nickname()
    # article_map = get_stats_sum()
    # res = []
    # for account in accounts:
    #     read_sum_plus = 0
    #     like_sum_plus = 0
    #     for i in range(1,13):
    #         read_sum = 0
    #         like_sum = 0
    #         for t in article_map:
    #             if t[1] == i and t[0] == account:
    #                 read_sum += t[2]
    #                 like_sum += t[3]
    #         res.append((account_nickname[account],account,i,read_sum,like_sum))
    #         read_sum_plus += read_sum
    #         like_sum_plus += like_sum
    #     res.append((account_nickname[account],account,'1-12',read_sum_plus,like_sum_plus))
    res = get_stats()
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet_1',cell_overwrite_ok=True)

    for i in range(0,len(res)):
        for j in range(1,7):
            booksheet.write(i,j,res[i][j])
    workbook.save('data2.xls')


if __name__ == '__main__':
    main()