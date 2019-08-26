import requests
import json

content = input("请输入你要翻译的内容")


url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

post_form = {
    'i': content,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15665531436478',
    'sign': 'f6e74e20c62145b063e1bd6ea38301de',
    'ts': '1566553143647',
    'bv': '7e3150ecbdf9de52dc355751b074cf60',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}

responst = requests.post(url, data=post_form)

trans_json = responst.text
trans_dict = json.loads(trans_json)
result = trans_dict['translateResult'][0][0]['tgt']
print('%s翻译为：%s' % (content, result))
