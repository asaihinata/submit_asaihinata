from math import ceil, floor
from os import system as sys
from platform import system
from sys import getsizeof

from numpy import ndarray
from numpy.random import default_rng

from ..types import Numbertype

__all__=['clear','LIST','Number','random','sort','zips']
class clear:
 def __init__(self):sys('cls' if system()=='Windows'else'clear')
class random:
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,random)
 @classmethod
 def normal(cls,loc=0,scale=1,lenght=1,hierarchy=1):
  try:
   if not isinstance(scale,Numbertype):scale=loc
   return default_rng().normal(loc,scale,(hierarchy,lenght))
  except:
   raise ValueError('error')
 @classmethod
 def rand(cls,mins=0,maxs=1,lenght=1,hierarchy=1,number=True):
  try:
   if maxs<mins:mins,maxs=maxs,mins
   if number:return default_rng().integers(low=mins,high=maxs,size=(hierarchy,lenght))
   return default_rng().uniform(low=mins,high=maxs,size=(hierarchy,lenght))
  except:
   raise ValueError('error')
class LIST:
 __slots__=('lists')
 def __init__(self,lists=None,*arg):
  if isinstance(lists,list):self.lists=lists
  elif isinstance(lists,(tuple,range)):self.lists=list(lists)
  elif isinstance(lists,ndarray):self.lists=lists.tolist()
  else:self.lists=[lists]
  for i in arg:self.lists.append(i)
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,LIST)
 def __contains__(self,val):return val in self.lists
 def __len__(self):return len(self.lists)
 def __iter__(self):return iter(self.lists)
 def __reversed__(self):
  self.lists=reversed(self.lists)
  return self
 def __getitem__(self,val):
  if isinstance(val,int)and 0<=val<len(self):return self.lists[val]
  return self.lists[0]
 def __eq__(self,lists):
  lens,judge=len(self),True
  if isinstance(lists,LIST)and(len(lists)==lens):
   lists=list(lists)
   for i in range(lens):
    if self.lists[i]!=lists[i]:
     judge=False
     break
  else:judge=False
  return judge
 def __ne__(self,lists):
  lens,judge=len(self),False
  if isinstance(lists,LIST)and(len(lists)==lens):
   lists=list(lists)
   for i in range(lens):
    if self.lists[i]!=lists[i]:
     judge=True
     break
  else:judge=True
  return judge
 def __add__(self,val):
  if isinstance(val,LIST):self.lists=self.lists+list(val)
  elif isinstance(val,(list,tuple)):
   for i in val:self.lists.append(i)
  else:self.lists.append(val)
  return self
 def __radd__(self,val):
  if isinstance(val,LIST):val=list(val)+self.lists
  else:
   if isinstance(val,tuple):val=list(val)
   elif not isinstance(val,list):val=[val]
   for i in self.lists:val.append(i)
  self.lists=val
  return self
 def __iadd__(self,val):
  self.lists.append(val)
  return self
 def __mul__(self,val):
  if isinstance(val,int)and 1<=val:
   lin=self.lists
   for _ in range(val-1):self.lists=self.lists+lin
  return self
 def __delattr__(self,item):
  if item=='lists':
   raise AttributeError(r'The \'lists\' attribute can\'t be deleted.')
  super().__delattr__(item)
 def __getattribute__(self,name):return super().__getattribute__(name)
 def _flatten(self,lists):
  for i in lists:
   if isinstance(i,list):yield from self._flatten(i)
   else:yield i
 def append(self,*arg):
  for i in arg:self.lists.append(i)
 def clear(self):self.lists=[]
 def flatten(self):return list(self._flatten(self.lists))
 def get(self,val):
  if not isinstance(val,int):return self.lists[0]
  elif val<=0:val=abs(val)
  return(self.lists*(val//len(self.lists)+1))[:val]
 def sort(self,type=True):
  if not isinstance(type,bool):type=True
  self.lists=sort(self.lists,type)
  return self
class sort:
 __slots__=('order','data')
 def __init__(self,data,types=True):
  if not isinstance(data,(list,tuple,LIST)):
   raise ValueError('配列を指定する必要がある。')
  self.order=types if isinstance(types,bool) else True
  self.data=sorted(data,key=sort._ascending) if self.order else sorted(data,key=sort._descending)
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,sort)
 def __contains__(self,val):return val in self.data
 def __iter__(self):return iter(self.data)
 def __bool__(self):return bool(self.order)
 def __len__(self):return len(self.data)
 def __reversed__(self):
  self.order=not self.order
  self.data=sorted(self.data,key=sort._ascending) if self.order else sorted(self.data,key=sort._descending)
  return self
 def __delattr__(self,item):
  if item in ['order','data']:
   raise AttributeError(f'The \'{item}\' attribute can\'t be deleted.')
  super().__delattr__(item)
 def __eq__(self,lists):
  lens,judge=len(self),True
  if isinstance(lists,sort)and(len(lists)==lens):
   lists=list(lists)
   for i in range(lens):
    if self.data[i]!=lists[i]:
     judge=False
     break
  else:judge=False
  return judge
 def __ne__(self,lists):
  lens,judge=len(self),False
  if isinstance(lists,sort)and(len(lists)==lens):
   lists=list(lists)
   for i in range(lens):
    if self.data[i]!=lists[i]:
     judge=True
     break
  else:judge=True
  return judge
 @staticmethod
 def _ascending(item):
  if isinstance(item,(int,float)):return(0,item,'')
  item_str=str(item)
  if item_str.isdigit():return(1,int(item_str),'')
  if item_str.isascii() and item_str.isalpha():return(2,[(i.lower(),0 if i.islower() else 1) for i in item_str])
  if any(i.isdigit() for i in item_str):
   has_ascii,has_japanese=any(i.isascii() for i in item_str),any(ord(i)>127 for i in item_str)
   if has_ascii and not has_japanese:return(3,item_str,'')
   elif has_japanese and has_ascii:return(5,item_str,'')
   return(4,item_str,'')
  if all(ord(i)>127 or i.isspace() for i in item_str):return(4,item_str,'')
  return(5,item_str,'')
 @staticmethod
 def _descending(item):
  if isinstance(item,(int,float)):return(5,item,'')
  item_str=str(item)
  if item_str.isdigit():return(4,int(item_str),'')
  if item_str.isascii() and item_str.isalpha():return(3,[(i.lower(),5 if i.islower() else 4) for i in item_str])
  if any(i.isdigit() for i in item_str):
   has_ascii,has_japanese=any(i.isascii() for i in item_str),any(ord(i)>127 for i in item_str)
   if has_ascii and not has_japanese:return(2,item_str,'')
   elif has_japanese and has_ascii:return(0,item_str,'')
   return(1,item_str,'')
  if all(ord(i)>127 or i.isspace() for i in item_str):return(1,item_str,'')
  return(0,item_str,'')
class Number:
 __slots__=('val','_type_')
 def __init__(self,val=None):
  if not isinstance(val,(Number,int,float)):
   raise TypeError('数値を指定しなさい。')
  if isinstance(val,Number):self.val=float(val) if val._types()==float else int(val)
  self.val,self._type_=val,type(val)
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,Number)
 def __delattr__(self,item):
  if item in ['val','_type_']:
   raise AttributeError(f'The \'{item}\' attribute can\'t be deleted.')
  super().__delattr__(item)
 def __getattribute__(self,name):return super().__getattribute__(name)
 def __int__(self):return int(self.val)
 def __float__(self):return float(self.val)
 def __str__(self):return str(self.val)
 def __add__(self,val):
  self.val=self.val+self._maths_(val)
  return self
 def __sub__(self,val):
  self.val=self.val-self._maths_(val)
  return self
 def __mul__(self,val):
  self.val=self.val*self._maths_(val)
  return self
 def __pow__(self,val):
  self.val=self.val**self._maths_(val)
  return self
 def __ipow__(self,val):
  self.val**=self._maths_(val)
  return self
 def __truediv__(self,val):
  self.val=self.val/self._maths_(val)
  return self
 def __radd__(self,val):
  self.val=self._maths_(val)+self.val
  return self
 def __rsub__(self,val):
  self.val=self._maths_(val)-self.val
  return self
 def __rmul__(self,val):
  self.val=self._maths_(val)*self.val
  return self
 def __rtruediv__(self,val):
  self.val=self._maths_(val)/self.val
  return self
 def __floordiv__(self,val):
  self.val=self.val//self._maths_(val)
  return self
 def __iadd__(self,val):
  self.val+=self._maths_(val)
  return self
 def __isub__(self,val):
  self.val-self._maths_(val)
  return self
 def __imul__(self,val):
  self.val*=self._maths_(val)
  return self
 def __itruediv__(self,val):
  self.val/=self._maths_(val)
  return self
 def __abs__(self):
  self.val=abs(self.val)
  return self
 def __eq__(self,val):return self.val==self._maths_(val)
 def __ne__(self,val):return self.val!=self._maths_(val)
 def __lt__(self,val):return self.val<self._maths_(val)
 def __le__(self,val):return self.val<=self._maths_(val)
 def __gt__(self,val):return self.val>self._maths_(val)
 def __ge__(self,val):return self.val>=self._maths_(val)
 def __round__(self,n=0):
  self.val=round(self.val,self._maths_(n))
  return self
 def __ceil__(self):
  self.val=ceil(self.val)
  return self
 def __floor__(self):
  self.val=floor(self.val)
  return self
 def __neg__(self):
  self.val=-self.val
  return self
 def __pos__(self):return self
 def __sizeof__(self):return super().__sizeof__()+getsizeof(self.val)
 def _types(self):return self._type_
 def _maths_(self,val):
  if isinstance(val,Number):return float(val) if val._types()==float else int(val)
  try:Number(val)
  except Exception as e:
   raise ValueError(e)
  return val
class zips:
 def __init__(self,iterables=(),fillvalues=()):self.it,self.fi=iterables,fillvalues
 def __iter__(self):return zip(*[list(i)+[v]*(max(len(i)for i in self.it)-len(i))for i,v in zip(self.it,self.fi)])