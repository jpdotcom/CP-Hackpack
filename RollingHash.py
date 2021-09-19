import random
import string
from typing import get_args

class RollingHash:
	def __init__(self) -> None:
	
	    self.value=0 	
	    self.a=719
	    self.b=265252859812191058636308479999999
	def hash(self,s):
		a=self.a 
		b=self.b
		nums=[ord(i) for i in s]
		
		for i in range(len(nums)):

			

			self.value=((self.value*a)%b+nums[i])%b 
		
		
		return self.value
	
	def remove(self,l,n):
		a=self.a 
		b=self.b
		l=ord(l) 
		self.value-=(l*pow(a,n,b))%b
		self.value=(self.value*pow(a,-1,b))%b 
		return self.value 
	def add(self,l):

		a=self.a 
		b=self.b 

		self.value*=a 
		self.value%=b 
		self.value+=ord(l) 
		self.value%=b
		return self.value
	


# printing lowercase
characters = string.ascii_lowercase #+ string.digits + string.punctuation
def getrandomString():
	return ''.join(random.choice(characters) for i in range(10)) 


for i in range(10000):

	s=getrandomString() 
	val1,val2,val3,val4=0,0,0,0
	h=RollingHash() 
	h.hash(s) 
	val1=h.value
	h.remove(s[0],len(s)) 
	val2=h.value
	h.remove(s[1],len(s))-1 
	val3=h.value
	h.add('d') 
	val4=h.value

	check=set((val1,val2,val3,val4))
	if len(check)!=4:
		print('Collision Found') 
		print(s,val1,val2,val3,val4) 
		break 
	
else:
	print('No Collision Found')



	







