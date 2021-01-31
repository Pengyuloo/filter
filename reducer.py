#!/usr/bin/env python3

from operator import itemgetter
import sys

totalcount={}
alist=list()
blist=list()
output={}
merge={}
pp=['89th_Academy_Awards\t20161130\t49',
 'Dffd\t20161103\t34',
 '89th_Grey_Cup\t20161111\t2',
 '89th_Grey_Cup\t20161130\t8',
 '89th_Grey_Cup\t20161109\t2',
 '89th_Division_(United_States)\t20161130\t1']
for line in sys.stdin:
    totalcount[line.split('\t')[0]]=0
    alist.append(line)
#将同一天的数据合并
for items in alist:
    merge[items.split('\t')[0]+'\t'+items.split('\t')[1]]=0
for items in alist:
    merge[items.split('\t')[0]+'\t'+items.split('\t')[1]]+=int(items.split('\t')[2])
blist=list(merge.items())
#计算每个条目的总访问量
for items in alist:
    totalcount[items.split('\t')[0]]+=int(items.split('\t')[2])
#每一条的输出信息初始化
for items in alist:
    output[items.split('\t')[0]]=str(totalcount[items.split('\t')[0]])+'\t'+items.split('\t')[0]
blist.sort(key=lambda x:(x[0].split('\t'))[1])
for items in blist:
    output[items[0].split('\t')[0]]+=('\t'+items[0].split('\t')[1]+':'+str(items[1]))
total=list(totalcount.items())
total.sort(key=lambda x:x[1],reverse=True)
for items in total:
    if items[1]>1000:
        print(output[items[0]])
    
