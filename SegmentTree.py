import math
import random

def query(l,r,n,tree):
  
  ans=0
  l+=n
  r+=n
  while l<=r:
    if l&1:
      #MODIFY QUERY HERE
      ans|=tree[l] 
      l+=1
    if r&1==0:
      #MODIFY QUERY HERE
      ans|=tree[r]
      r-=1
    l>>=1 
    r>>=1
  return ans 

def update(i,val,n,tree):
  
  i+=n 
  
  tree[i]+=val 
  i>>=1
  
  while i>=1:
    #MODIFY UPDATE HERE
    tree[i]=tree[2*i]|tree[2*i+1]
    i>>=1 




   

    

