import requests
from prettyprinter import cpprint


"""测试一些接口"""

def get_data(url,param=None,headers=None):
    """

    :param url:目标url
    :param param: 传入参数 默认none
    :param headers: 传入的头信息 默认none
    :return:
    """
    res = None
    try:
        res = requests.get(url=url,
                           params=param,
                           headers=headers)
    except:
        return "访问失败"
    if res.status_code == 200:
        return res.json()
    else:
        return "错误: "+ str(res.status_code)



def github():
    url = "https://api.github.com/search/repositories"
    param = {
        'q':'api+language:python',
        'sort':'stars'
    }
    headers = {
        'Accept': 'application/vnd.github.v3.mercy-preview+json',
        'Authorization':'eabf9c57beac7a6ffcd43d89fae2934fce34fc88'
    }
    res = get_data(url,param,headers)
    cpprint(res)


def jikan():
    baseUrl = "https://api.jikan.moe/v3"

    extraUrl = "/character/1/pictures"

    res = get_data(baseUrl+extraUrl)
    cpprint(res)


def book_nomads():
    url = "https://www.booknomads.com/api/v0/isbn/"
    isbn = "9789000010134"
    res = get_data(url+isbn)
    cpprint(res)


def main():
    cpprint(book_nomads())


if __name__ == '__main__':
    main()