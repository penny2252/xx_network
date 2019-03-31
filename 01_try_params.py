import requests
headers={'user-agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
#带url参数的做法,注意s后面有没有？都一样
# p={'wd':'python'}
# url='http://www.baidu.com/s'
# requests=requests.get(url,headers=headers,params=p)
# print(requests.status_code)
# print(requests.url)
# print(requests.content.decode())


#直接将参数写如url的做法,s后面需要有？和wd=
# url="http://www.baidu.com/s?wd={}".format('python')
# requests=requests.get(url,headers=headers)
# print(requests.status_code)
# print(requests.url)
# print(requests.content.decode())

#format的用法
a="这是一个{}的用法，可以在任意的{}加入'{}'后，利用format方法导入要加入的{}".format('format','地方','{}','字符串、字典、列表等元素不任何改变')
print(a)