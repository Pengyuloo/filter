#!/usr/bin/env python3
import sys
import os
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
    if len(s.split())!=5:
        return 1
    else:
        return 0
def keep_en_enm(s,sign):
    if sign==1:
        return 1
    if s.split()[1]=="en" or s.split()[1]=="en.m":
        return 0
    else:
        return 1 
def removetypes(s,sign):
    if sign==1:
        return 1
    if ':' in s:
        if s.split()[2].split(":")[0] in typelist:
            return 1
        else:
            return 0
    else:
        return sign
def removelowcase(s,sign):
    if sign==1:
        return 1
    if 'a'<s.split()[2][0]<'z':
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
    if s.split()[2]=="404.php" or s.split()[2]=="Main_Page" or s.split()[2]=="-":
        return 1
    else:
        return 0
def dirtydata2(s,sign):    
    if s.split()[3]>'999999' or s.split()[3]<'0':
        return 1
    else:
        return 0
def generate_data(s,sign):
    if sign==1:
        return
    else:
        line=s.split()[2]+'\t'+s.split()[3]+'\t'+s.split()[0]
        resultlist.append(line)
        diction[line.split('\t')[0]+'\t'+line.split('\t')[2]]=0
               #os.environ["mapreduce_map_input_file"]
        #print ('%s\t%s'%(s.split()[1],int(s.split()[2])))
        return
resultlist=list()
diction={}
pp=['20161130 en.m 89th_Academy_Awards 49 0',
'20161130 en.m 89th_Airlift_Wing hallo 0',
'20161130 en.m 89th_Division_(United_States) 1 0',
'20161130 en.m 89th_Grey_Cup 4 0',
'20161130 en 89th_Grey_Cup 3 0',
'20161130 en 89th_Grey_Cup 1 0',
'20161109 en.m 89th_Grey_Cup 1 0',
'20161109 en 89th_Grey_Cup 1 0',
"20161103 en Dffd 34 0"]
#for line in sys.stdin:
for line in sys.stdin:
    line = line.strip()
    sign=0                
    p=dirtydata(line, sign)                        #第一步处理脏数据
    if p:
        continue
    p=keep_en_enm(line, p)                         #第二步只保留以en\en.m开头的数据
    if p:
        continue
    line=decode(line)                                 #第三步对百分号进行解码
    if p:
        continue
    p=removetypes(line,p)                          #第四步除去不相关namespace
    if p:
        continue
    p=removelowcase(line, p)                       #第五步除去英文小写字母开头的信息
    if p:
        continue
    p=removesuffix(line, p)                        #第六步除去指定后缀的信息
    if p:
        continue
    p=removedisambiguation(line, p)                #第七步消除歧义项
    if p:
        continue
    p=removespecial(line, p)                       #第八步消除指定页数据
    if p:
        continue
    p=dirtydata2(line,p)
    generate_data(line,p)

for i in resultlist:
    diction[i.split('\t')[0]+'\t'+i.split('\t')[2]]+=int(i.split('\t')[1])
outlist=list(diction.items())
outlist.sort(key=lambda x:x[1], reverse=True)
for items in outlist:
    print('%s\t%s'%(items[0],items[1]))
