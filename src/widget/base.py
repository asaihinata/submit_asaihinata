from tkinter import Misc

from ..types import (Arraytype, Callable, FunctionType, Numbertype,
                     TupleNumbertype2)
from ._font import fonts
from ._function import bols, font_family, listchose, num0, nums, parsecolor
from ._log import Logger

__all__=['Element']
logger=Logger(name='base',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
class Element:
 def __init__(self,master:Misc,kw:dict)->None:
  self.widget=None
  self.master=master
  self.cursor=kw.get('cursor')
  self.back_bg=kw.get('back_bg')
  self.justify=listchose(kw.get('justify'),['left','right','center'])
  self.padx=num0(kw.get('padx'),1)
  self.pady=num0(kw.get('pady'),1)
  self.relief=listchose(kw.get('relief'),['flat','raised','sunken','ridge','solid','groove'])
  self.fg=parsecolor(kw.get('fg'),'#000000')
  self.bg=parsecolor(kw.get('bg'),'#64778d' if self.back_bg==None else self.back_bg)
  self.borderwidth=num0(kw.get('bd'))
  self.takefocus=bols(kw.get('takefocus'))
  self.family=kw.get('family',font_family)
  self.font_size=kw.get('font_size')
  self.weight=kw.get('weight')
  self.slant=kw.get('slant')
  self.underline=kw.get('underline')
  self.overstrike=kw.get('overstrike')
  self.font=fonts(family=self.family,size=self.font_size,weight=self.weight,slant=self.slant,underline=self.underline,overstrike=self.overstrike,root=self.master)
  self.anchor=listchose(kw.get('anchor'),['w','n','s','e','nw','ne','se','sw','center'])
  self.size=self._size(kw.get('size'))
  self.width,self.height=self.size
 def _size_width(self,val:Numbertype,other:Numbertype=None)->Numbertype:return(val if isinstance(val,(int,float))else other)
 def _size_height(self,val:Numbertype,other:Numbertype=None)->Numbertype:return(val if isinstance(val,(int,float))else other)
 def _size(self,size:Arraytype,other:TupleNumbertype2|list[Numbertype|None,Numbertype|None]=(None,None))->TupleNumbertype2:
  if isinstance(size,(list,tuple))and len(size)==2:return(nums(size[0]),nums(size[1]))
  elif isinstance(size,(list,tuple))and len(size)==2 and(isinstance(size[0],(int,float))or size[0]==None)and(isinstance(size[1],(int,float))or size[1]==None):return other
  else:return(None,None)
 def _exec_funcs(self,funcs:function|list[function]|tuple[function]=None)->Callable|None:
  if isinstance(funcs,FunctionType):
   try:funcs()
   except Exception as e:
    logger.error(f'function({funcs.__name__}) error.\n{e}')
  elif isinstance(funcs,(list,tuple)):
   for f in funcs:
    if isinstance(f,FunctionType):
     try:f()
     except Exception as e:
      logger.error(f'function({funcs}) error.\n{e}')
    else:
     logger.warning(f'{f} is not function type')
  else:return None