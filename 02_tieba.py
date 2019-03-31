import os
import request



def web(name,num):
    url='http://www.baidu.com/s?wk={}&nq={}'.format(name,(num-1)*50)
    headers={'User_Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
    q=request.get(url,headers=headers)
    txt=q.content.decode()
    return txt
    

def create_file(forder,num):
    os.mkdir(forder+'/')
    os.chdir(forder+'/')
    n=0
    while n<num:
        n+=1
        f=os.open(forder+'_'+str(n).txt,'wb')
        txt=web(forder,n)
        f.write(txt)
        f.close()
        
def main():
    #创建文件写入爬取的内容
    tieba_name='liyiba'
    num=100
    create_file(tieba_name,100)





if __name__=='__main__':
    mian()

