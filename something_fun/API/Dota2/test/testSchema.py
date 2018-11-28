import requests
import threading

"""
查看哪些数据库表可以被访问,对应文件./data/reachable.json
"""

class MyThread(threading.Thread):
    def __init__(self,sub_list):
        threading.Thread.__init__(self)
        self.sub_list = sub_list

    def run(self):
        test(self.sub_list)

def getSchema():
    url = "https://api.opendota.com/api/schema"
    param = {
        'api_key': "B6F03F91CD8355AD6856E6DF03854370"
    }
    res = requests.get(url, param)
    return res.json()

def makeSql(table_name,column_name):
    return "select {0} from {1}".format(column_name,table_name)

def visit(sql):
    url = "https://api.opendota.com/api/explorer"
    param = {
        'api_key': "B6F03F91CD8355AD6856E6DF03854370",
        'sql': sql
    }
    res = requests.get(url,param)
    return res.status_code

def test(schemas):
    for schema in schemas:
        # print(type(schema))
        if type(schema) != dict:
            continue
        sql = makeSql(schema['table_name'],schema['column_name'])
        if visit(sql) == 200 :
            print(schema)


def main():
    data = getSchema()
    test(data)
    # block = 40
    # for i in range(8):
    #     if i < 7 :
    #         sub_list = data[i*block:(i+1)*block]
    #     else :
    #         sub_list = data[i*block:]
    #     threads = MyThread(sub_list)
    #     threads.start()
    # for schema in data:
    #     print(type(schema))



if __name__ == '__main__':
    main()
