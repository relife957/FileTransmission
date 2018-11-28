import psycopg2


def get_conn():
    conn = None
    output = "数据库连接成功"
    try:
        conn = psycopg2.connect(host='127.0.0.1', port='5432',
                                dbname='postgres', user='postgres', password='123456')
    except psycopg2.OperationalError:
        output = '数据库连接失败！'
    print(output)
    return conn

def get_data():
    filepath = "/home/wangyi/文档/"
    filename = "data.dat"
    f = open(filepath + filename, 'r')

    data = f.readlines()

    f.close()
    return data


def insert(conn,data):
    cur = conn.cursor()

    for line in data:
        param = deal_string(line)
        sql = "INSERT INTO api.dota2 (team,recommend) VALUES (\'{0}\',\'{1}\')".format(param[0].strip(),param[1].strip())
        try:
            cur.execute(sql)
        except:
            print(sql)
            continue
    conn.commit()
    print("insert finished!")

def deal_string(string):
    res = string.strip()[1:-1]
    return res.split(',')


def main():
    conn = get_conn()
    data = get_data()
    insert(conn,data)
    conn.close()


if __name__ == '__main__':
    main()