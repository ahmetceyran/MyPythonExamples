class carpma():
	def carp(self,a,b):
		return a*b;

	
class bolme():
	def bol(self,a,b):
		return a/b;

	
class hesap(carpma,bolme):
	def topla(self,a,b):
		return a+b;
	def cikar(self,a,b):
		return a-b;


hm=hesap()
print(hm.carp(15,3))
print(hm.bol(15,3))
print(hm.topla(15,3))
print(hm.cikar(15,3))
