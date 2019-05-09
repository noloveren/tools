#!env python
#author mrhonest
#coding=utf-8
Str=""
f=open("lib_mysqludf_sys.so","rb")
while True:
    tmp=f.read(1)
    if len(tmp)==0:
        break
    else:
        Str+=tmp.encode("hex")
f.close()
print Str
xie=open('hex.txt','a')
xie.writelines(Str)
