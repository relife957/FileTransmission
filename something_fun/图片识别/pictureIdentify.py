import pytesseract
from PIL import Image
import os
import subprocess

def image_to_string(img, cleanup=True, plus=''):
    # cleanup为True则识别完成后删除生成的文本文件
    # plus参数为给tesseract的附加高级参数
    subprocess.check_output('tesseract ' + img + ' ' +
                            img + ' ' + plus, shell=True)  # 生成同名txt文件
    text = ''
    with open(img + '.txt', 'r') as f:
        text = f.read().strip()
    if cleanup:
        os.remove(img + '.txt')
    return text
image = Image.open("/home/wangyi/图片/steam秘钥.png")
text = pytesseract.image_to_string(image,lang='chi_sim')
print(text)
#print(image_to_string("/home/wangyi/图片/gwent.png",False,'-l chi_sim'))