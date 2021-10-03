class UnionFind:

    def __init__(self,arr):


        self.rep=[0]*(len(arr)+1)
        self.sizeof=[0]*(len(arr)+1)
        for e in arr:
            self.rep[e]=e 
            self.sizeof[e]=1
        return 
    def find(self,a):
        if a>(len(self.rep)-1):
            raise ValueError("Element out of bounds")
            return -1
        r=a 
        if self.rep[a]!=a:
            r=self.find(self.rep[a])

        self.rep[a]=r 
        return r 
    
    def union(self,a,b):

        self.rep1=self.find(a) 
        self.rep2=self.find(b) 
        
        if (self.rep1==self.rep2):
            return  
        
        if self.sizeof[self.rep1]>self.sizeof[self.rep2]:
            self.rep1,self.rep2=self.rep2,self.rep1
        self.rep[self.rep1]=self.rep2 
        self.sizeof[self.rep2]+=self.sizeof[self.rep1]
        return 



