import requests
from lxml import etree
class YoudaoSpider(object):
    def __init__(self):
        #准备url地址
        self.trans_url = "http://m.youdao.com/translate"
        #请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        }
    def get_result(self, word, fro):
        #构造一个form表单数据---表单是一个字典
        data = {
            'inputtext': word,
            'type': fro

        }
        response = requests.post(url=self.trans_url, data=data, headers=self.headers)

        html = response.content.decode('utf-8')
        pa = etree.HTML(html)
        # print(html)
        pa_list = pa.xpath("//div[@class='generate']/ul/li/text()")
        for i in pa_list:
            print("翻译为:" + i)



if __name__ == '__main__':
    spider = YoudaoSpider()
    choice = input("1.中翻译英语  2.中翻韩语 3.把中文翻译法语 \n请选择1/2/3:\n")
    if choice == '1':
        fro = 'ZH_CN2EN'
    elif choice == '2':
        fro = 'ZH_CN2SP'
    elif choice == '3':
        fro = 'ZH_CN2FR'
    word = input("请输入你要翻译的单词或句子:")
    result = spider.get_result(word, fro)
