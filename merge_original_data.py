# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 00:51:34 2021

@author: 卢鹏宇
"""

datelist=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
timelist=['000000','010000','020000','030000','040000','050000','060000','070000','080000','090000','100000','110000','120000','130000','140000','150000','160000','170000','180000','190000','200000','210000','220000','230000']
w=open("testdata1","a",encoding='utf-8',errors='ignore')
for date in ["01","02","03"]:
    print(date)
    for time in ['000000']:
        print(time)
        name="pageviews-201611"+date+"-"+time
        r=open(name,'r',encoding='utf-8',errors='ignore')
        for line in r.readlines():
            content=('201611'+date+' '+line)
            w.write(content)

w.close()
