#-*- coding: utf-8 -*-
"""
Created on Wed Jan 20 18:49:12 2021

@author: 卢鹏宇
"""
import json
"""
a='{"-2":{"id":-2,"case":"first-letter","canonical":"Media","*":"Media"},"-1":{"id":-1,"case":"first-letter","canonical":"Special","*":"Special"},"0":{"id":0,"case":"first-letter","content":"","*":""},"1":{"id":1,"case":"first-letter","subpages":"","canonical":"Talk","*":"Talk"},"2":{"id":2,"case":"first-letter","subpages":"","canonical":"User","*":"User"},"3":{"id":3,"case":"first-letter","subpages":"","canonical":"User_talk","*":"User talk"},"4":{"id":4,"case":"first-letter","subpages":"","canonical":"Project","*":"Wikipedia"},"5":{"id":5,"case":"first-letter","subpages":"","canonical":"Project_talk","*":"Wikipedia talk"},"6":{"id":6,"case":"first-letter","canonical":"File","*":"File"},"7":{"id":7,"case":"first-letter","subpages":"","canonical":"File_talk","*":"File talk"},"8":{"id":8,"case":"first-letter","canonical":"MediaWiki","namespaceprotection":"editinterface","*":"MediaWiki"},"9":{"id":9,"case":"first-letter","subpages":"","canonical":"MediaWiki talk","*":"MediaWiki talk"},"10":{"id":10,"case":"first-letter","subpages":"","canonical":"Template","*":"Template"},"11":{"id":11,"case":"first-letter","subpages":"","canonical":"Template talk","*":"Template talk"},"12":{"id":12,"case":"first-letter","subpages":"","canonical":"Help","*":"Help"},"13":{"id":13,"case":"first-letter","subpages":"","canonical":"Help talk","*":"Help talk"},"14":{"id":14,"case":"first-letter","subpages":"","canonical":"Category","*":"Category"},"15":{"id":15,"case":"first-letter","subpages":"","canonical":"Category talk","*":"Category talk"},"100":{"id":100,"case":"first-letter","subpages":"","canonical":"Portal","*":"Portal"},"101":{"id":101,"case":"first-letter","subpages":"","canonical":"Portal_talk","*":"Portal talk"},"108":{"id":108,"case":"first-letter","subpages":"","canonical":"Book","*":"Book"},"109":{"id":109,"case":"first-letter","subpages":"","canonical":"Book_talk","*":"Book talk"},"118":{"id":118,"case":"first-letter","subpages":"","canonical":"Draft","*":"Draft"},"119":{"id":119,"case":"first-letter","subpages":"","canonical":"Draft_talk","*":"Draft talk"},"446":{"id":446,"case":"first-letter","canonical":"Education_Program","*":"Education Program"},"447":{"id":447,"case":"first-letter","subpages":"","canonical":"Education_Program_talk","*":"Education Program talk"},"710":{"id":710,"case":"first-letter","canonical":"TimedText","*":"TimedText"},"711":{"id":711,"case":"first-letter","canonical":"TimedText_talk","*":"TimedText talk"},"828":{"id":828,"case":"first-letter","subpages":"","canonical":"Module","*":"Module"},"829":{"id":829,"case":"first-letter","subpages":"","canonical":"Module_talk","*":"Module talk"},"2300":{"id":2300,"case":"first-letter","canonical":"Gadget","namespaceprotection":"gadgets-edit","*":"Gadget"},"2301":{"id":2301,"case":"first-letter","canonical":"Gadget_talk","*":"Gadget talk"},"2302":{"id":2302,"case":"case-sensitive","canonical":"Gadget_definition","namespaceprotection":"gadgets-definition-edit","defaultcontentmodel":"GadgetDefinition","*":"Gadget definition"},"2303":{"id":2303,"case":"case-sensitive","canonical":"Gadget_definition_talk","*":"Gadget definition talk"}}'
t=json.loads(a)
x=t.keys()
for i in x :
    if t[str(i)]['id']==0:
        continue
    typelist.append(t[str(i)]['canonical'])
"""
typelist=['Media',
 'Special',
 'Talk',
 'User',
 'User_talk',
 'Project',
 'Project_talk',
 'File',
 'File_talk',
 'MediaWiki',
 'MediaWiki_talk',
 'Wikipedia',
 'Wikipedia_talk',
 'Template',
 'Template_talk',
 'Help',
 'Help_talk',
 'Category',
 'Category_talk',
 'Portal',
 'Portal_talk',
 'Book',
 'Book_talk',
 'Draft',
 'Draft_talk',
 'Education_Program',
 'Education_Program talk',
 'TimedText',
 'TimedText_talk',
 'Module',
 'Module_talk',
 'Gadget',
 'Gadget_talk',
 'Gadget_definition',
 'Gadget_definition_talk']
def decode(encoded):
    def getHexValue(b):
        if '0' <= b <= '9':
            return (ord(b) - 0x30)
        elif 'A' <= b <= 'F':
            return (ord(b) - 0x37)
        elif 'a' <= b <= 'f':
            return (ord(b) - 0x57)
        return -1

    if encoded is None:
        return None
    encodedChars = encoded
    encodedLength = len(encodedChars)
    decodedChars = ''
    encodedIdx = 0
    while encodedIdx < encodedLength:
        if encodedChars[encodedIdx] == '%' and (encodedIdx + 2 )< encodedLength and getHexValue(encodedChars[encodedIdx + 1]) >= 0 and getHexValue(encodedChars[encodedIdx + 2]) >= 0:
            #  current character is % char
            value1 = getHexValue(encodedChars[encodedIdx + 1])
            value2 = getHexValue(encodedChars[encodedIdx + 2])
            decodedChars += chr((value1 << 4) + value2)
            encodedIdx += 2
        else:
            decodedChars += encodedChars[encodedIdx]
        encodedIdx += 1
    return str(decodedChars)
def dirtydata(s,sign):    
    if len(s.split())!=4:
        return 1
    else:
        return 0
def keep_en_enm(s,sign):
    if sign==1:
        return 1
    if s.split()[0]=="en" or s.split()[0]=="en.m":
        return 0
    else:
        return 1 
"""
def decodepercent(s,sign):
    if '%' in temp:
        s=decode(s)
    return sign
"""
def removetypes(s,sign):
    if sign==1:
        return 1
    if ':' in s:
        if s.split()[1].split(":")[0] in typelist:
            return 1
        else:
            return 0
    else:
        return sign
def removelowcase(s,sign):
    if sign==1:
        return 1
    if 'a'<s.split()[1][0]<'z':
        return 1
    else:
        return sign
def removesuffix(s,sign):
    if sign==1:
        return 1
    suflist=['.png','.gif','.jpg','.jpeg','.tiff','.tif','.xcf','.mid','.ogg','.ogv','.svg','.djvu','.oga','.flac','.opus','.wav','.webm','.ico','.txt']
    if '.' in s:
        idx=s.find('.')
        if idx+3 <= len(s):
            word0=s[idx]+s[idx+1]+s[idx+2]
            word1=word0+s[idx+3]
            if (word0 in suflist) or (word1 in suflist):
                return 1
    return 0
def removedisambiguation(s,sign):
    if sign==1:
        return 1
    if '_(disambiguation)' in s or '_(Disambiguation)' in s:
        return 1
    else:
        return 0
def removespecial(s,sign):
    if sign==1:
        return 1
    if s.split()[1]=="404.php" or s.split()[1]=="Main_Page" or s.split()[1]=="-":
        return 1
    else:
        return 0
def generate_data(s,sign):
    if sign==1:
        return
    else:
        resultlist.append(s.split()[1]+'\t'+s.split()[2])
        diction[s.split()[1]]=0       #将所有title（唯一）记录到字典里
        return
def sort_output():
    outlist=list(diction.items())
    outlist.sort(key=lambda x:x[1], reverse=True)
    for items in outlist:
        w.write(str(items[0])+'\t'+str(items[1])+'\n')
        
    
#filter start
r=open("original_data.txt",'r',encoding='utf-8',errors='ignore')
w=open("final_data.txt",'w',encoding='utf-8',errors='ignore')
filelen=len(r.readlines())
r.seek(0,0)
resultlist=list()
diction={}
for i in range(filelen):
    sign=0
    s=r.readline()                  
    p=dirtydata(s, sign)                        #第一步处理脏数据
    p=keep_en_enm(s, p)                         #第二步只保留以en\en.m开头的数据
    s=decode(s)                                 #第三步对百分号进行解码
    p=removetypes(s,p)                          #第四步除去不相关namespace
    p=removelowcase(s, p)                       #第五步除去英文小写字母开头的信息
    p=removesuffix(s, p)                        #第六步除去指定后缀的信息
    p=removedisambiguation(s, p)                #第七步消除歧义项
    p=removespecial(s, p)                       #第八步消除指定页数据
    generate_data(s,p)
for i in resultlist:
    diction[i.split()[0]]+=int(i.split()[1])    #第九步统计每个词条的总访问量（客户端+移动端）
sort_output()                                   #第十步排序并输出到文件final_data.txt
r.close()
w.close()