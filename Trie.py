class Node:


	def __init__(self) -> None:

		self.cnt=0

		self.children=[None]*26
		self.children_cnt=0

class Trie:

	def __init__(self) -> None:
		self.root=Node() 
	
	def insert(self,s,idx=0,curr_node=None):

		if curr_node==None:
			curr_node=self.root 
		
		if idx==len(s):
			curr_node.cnt+=1 
			if curr_node.cnt-1:
				
				return True
			else:
				
				return False	

		letter=ord(s[idx])-97
		
		if curr_node.children[letter]!=None :
			return self.insert(s,idx+1,curr_node.children[letter]) 
		else:
			curr_node.children[letter]=Node()
			curr_node.children_cnt+=1 
			return self.insert(s,idx+1,curr_node.children[letter]) 
		
	def remove(self,s,idx=0,curr_node=None):

		if curr_node==None:
			curr_node=self.root 
		if idx==len(s):
			curr_node.cnt-=1 
			if curr_node.children_cnt==0:
			
				return True 
			else:
				return False
		
		
		
		letter=ord(s[idx])-97 

		if curr_node.children[letter]==None:
			raise Exception('Error: Prefix or word is not in Trie') 
			return 
		
		else:
			r=self.remove(s,idx+1,curr_node.children[letter]) 
			if r:
				curr_node.children[letter]=None 
				curr_node.children_cnt-=1 
			if curr_node.children_cnt==0:
				return True 
			return False 
	def findWord(self,s,idx=0,curr_node=None):

		if curr_node==None:
			curr_node=self.root
		if idx==len(s):
			return True if curr_node.cnt else False
		
		letter=ord(s[idx])-97 
		
		if curr_node.children[letter]==None:
			return False
		else:
			return self.findWord(s,idx+1,curr_node.children[letter])
	
	def findPrefix(self,s,idx=0,curr_node=None):

		if curr_node==None:
			curr_node=self.root 
		if idx == len(s):
			return True 
		
		letter=ord(s[idx])-97 

		if curr_node.children[letter]==None:
			return False 
		else:
			return self.findPrefix(s,idx+1,curr_node.children[letter])




		
		




			










	



