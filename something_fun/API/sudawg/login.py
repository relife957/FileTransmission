import requests
import base64


def get_data(url,param=None,headers=None):
    """

    :param url:目标url
    :param param: 传入参数 默认none
    :param headers: 传入的头信息 默认none
    :return:
    """
    res = None
    try:
        res = requests.post(url=url,
                           data=param,
                           headers=headers)
    except:
        return "访问失败"
    if res.status_code == 200:
        return res.json()
    else:
        return "错误: "+ str(res.status_code)


def main():
    url = 'http://a.suda.edu.cn/index.php/index/login'

    param = {
        'username':'yangzhe',
        'password':base64.b64encode('hata803211'.encode('utf-8'))
    }
    print(get_data(url))

if __name__ == '__main__':
    main()