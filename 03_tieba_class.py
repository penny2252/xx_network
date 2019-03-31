import time,os,requests


class TieBa(object):
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def run(self):
        os.mkdir(self.name)
        os.chdir(self.name)
        headers={'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
        n=0
        while n<self.num:
            url='https://tieba.baidu.com/f?kw={}&np={}'.format(self.name,n*50)
            f=open(self.name+str(n+1),'w')
            q=requests.get(url,headers=headers)
            txt=q.content.decode()
            f.write(txt)
            f.close()
            print('\r爬取进度：%.2f%%'% ((n+1)*100/self.num),end='')
            n+=1
        print()


def main():
    start=time.time()
    tieba_name='李毅吧'
    num=100
    file=TieBa(tieba_name,100)
    file.run()
    end=time.time()
    print(end-start)

if __name__=='__main__':
    main()
