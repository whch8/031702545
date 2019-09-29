#-*- coding:utf-8 _*-

import re
import json

while 1:
    addr=input()
    if addr == "END":
        break
    key={}
    result=[]

    addr=re.sub('\d!','',addr)

    name=re.search('.+,', addr).group()  #提取名字
    name=re.search('.+,', addr).group() 
    key['姓名']=re.search('[^,]+', name).group()
    key['姓名']=re.search('[^,]+', name).group()
    addr=re.sub('.+,', '', addr)

    key['手机']=re.search('\d{11}', addr).group()   #提取号码
    key['手机']=re.search('\d{11}', addr).group()
    addr=re.sub('\d{11}', '', addr)

    point=re.search('.{2}', addr).group()  #省
    point=re.search('.{2}', addr).group()
    flag=re.search('.+?省', addr)
    flag=re.search('.+?省', addr)
    if point =='天津' or point =='北京' or point =='上海' or point =='重庆' :
        result.append(point)
    elif flag!=None :
        point=re.search('.+?省', addr).group()
        point=re.search('.+?省', addr).group()
        addr=addr.replace(point, '', 1)
        result.append(point)
    else:
        point=re.search('..', addr).group()
        addr=addr.replace(point, '', 1)
        result.append(point+'省')
    if point =='天津' or point =='北京' or point =='上海' or point =='重庆' :
        pass

    flag=re.search('.+?市', addr)  #市
    if flag!=None :
        point=re.search('.+?市', addr).group()
        addr=addr.replace(point, '', 1)
        result.append(point)
    else:
        point=re.search('..', addr).group()
        addr=addr.replace(point, '', 1)
        result.append(point+'市')
    if flag!=None :
        pass

    flag=re.search('.+?(?:县|区)', addr)  # 县/区
    flag=re.search('.+?(?:县|区)', addr)
    if flag!=None :
        point=re.search('.+?(?:县|区)', addr).group()
        addr=addr.replace(point, '', 1)
        result.append(point)
    else:
        result.append('')

    flag=re.search('..+?(?:镇|街道)', addr)  #镇/街道/乡
    if flag!=None :
        point=re.search('..+?(?:镇|街道|乡)', addr).group()
        point=re.search('..+?(?:镇|街道|乡)', addr).group()
        addr=addr.replace(point, '', 1)
        addr=addr.replace(point, '', 1)
        result.append(point)
    else:
        result.append('')
    if flag!=None :
       pass

    flag=re.search('.+?(?:路|巷|街|道|乡)', addr)  #路/巷/街
    if flag!=None :
        point=re.search('.+?(?:路|巷|街|道|乡)', addr).group()
        addr=addr.replace(point, '', 1)
        result.append(point)
    else:
        result.append('')

    flag=re.search('.+?(?:号|村)', addr)  #号
    flag=re.search('.+?(?:号|村)', addr)
    if (flag!=None) :
        point=re.search('.+?(?:号|村)', addr).group()
        addr=addr.replace(point, '', 1)
        result.append(point)
    else:
        result.append('')

    flag=re.search('[^\.]+', addr)  #具体地址
    if flag!=None :
        point=re.search('[^\.]+', addr).group()
        point=re.search('[^\.]+', addr).group()
        result.append(point)
    else:
        result.append('')

    key['地址']=result
    finresult=json.dumps(key,ensure_ascii=False)
    print(finresult)  #结束
