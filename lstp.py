
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 01:09:20 2021

@author: Daniel
"""
def minLsl2(*lists):
    return min([(len(i)) for i in lists])

minLsLen = lambda *lists : min([len(i) for i in lists])


def allSame(ls):
    t=ls[0]
    boolLs=[i==t for i in ls]
    return(all(boolLs))

def listTypes(*lists):
    simInds=[]
    simStrs=[]
    simInts=[]
    simFloats=[]
    for i in range(minLsLen(*lists)):
        temp=[]
        for lst in lists: #append all lst[?] for each list
            temp.append(lst[i])
        if(allSame(temp)):
            simInds.append(i) #if allSame in all lists -> append that index
        
    simStrs=[i for i in lists[0] if type(i)==str] #strs of first ls
    simInts=[i for i in lists[0] if type(i)==int] 
    simFloats=[i for i in lists[0] if type(i)==float]


    for lst in lists:
        for i in simStrs:
                    if i not in lst:
                        simStrs.remove(i) #if not in firststrings , remove it as it won't be common
                    
        for i in simInts:
            if i not in lst:
                simInts.remove(i) #if not in firstInt , remove it as it won't be common
            
        for i in simFloats:
            if i not in lst:
                simFloats.remove(i) #if not in firstFloats , remove it as it won't be common
            
    return (simInds,simStrs,simInts,simFloats)
            
        


        
            
def main():
    l1=[2,5,'yofi',9.2,10,'tofi',8,'@$',66,'krm']
    l2=[2,5,7,9.2,77,'tofi',100,'@$','krm']
    l3=[2,5,11,9.2,83,'tofi',67,'@$','lola',1,2,3,4,'krm']
    print(listTypes(l1,l2,l3))
    

           
main()