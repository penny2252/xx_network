
import os
import requests
import time
import multiprocessing



def web(name,num):
    url='http://tieba.baidu.com/f?kw={}&nq={}'.format(name,(num-1)*50)
    headers={'User_Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
    q=requests.get(url,headers=headers)
    txt=q.content.decode()
    return txt
    

def create_file(forder,num):
    os.mkdir(forder+'/')
    os.chdir(forder+'/')
    n=0
    while n<num:
        n+=1
        f=open(forder+'_'+str(n)+'.txt','w')
        txt=web(forder,n)
        f.write(txt)
        f.close()
        print('\r爬取进度：%.2f%%'%(n*100/num),end='')
    print()
        
def main():
    #创建文件写入爬取的内容
    start_time=time.time()
    tieba_name='李毅吧'
    num=100
    # po=multiprocessing.Pool(5)
    #
    # p=po.apply_async(create_file(tieba_name,num))
    # po.close()
    create_file(tieba_name, num)
    end_time=time.time()
    print(end_time-start_time)





if __name__=='__main__':
    main()

