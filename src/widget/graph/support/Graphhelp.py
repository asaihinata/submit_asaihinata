from re import fullmatch
from typing import Literal

from numpy import pi

from ....types import Numbertype
from ..._function import listchose

__all__=['Angle','GraphOption','SCapstyle','Hatch','Solid','Marker']
MARKERS=[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','o','p','P','s','v','x','X','$\\alpha$','$\\beta$','$\\gamma$','*','+',',','.','<','>','^','_','|']
HATCH=[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--','-\\\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||']
SOLID={'solid':['-','solid'],'dashed':['--','dashed'],'dashdot':['-.','dashdot'],'dotted':[':','dotted'],'None':['none',None,'None',' ','']}
class GraphOption:
 @staticmethod
 def marker():return MARKERS
 @staticmethod
 def hatch():return HATCH
 @staticmethod
 def solid():return['dashdot','dashed','dotted','none',None,'None','solid','',' ','-','--','-.',':']
class Hatch:
 '''塗りつぶすアイコンの設定に関するクラス'''
 def __init__(self,hatch:Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--','-\\\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||']=None)->None:
  if isinstance(hatch,(list,tuple)):self.hatch=[self._get(i) for i in hatch]
  else:self.hatch=[self._get(hatch)]
 def _get(self,val):return val if val in HATCH else None
 def __iter__(self)->None:return iter(self.hatch)
 def __len__(self)->int:return len(self.hatch)
 def __str__(self):return self.hatch[0]
class Solid:
 '''グラフ内の線の設定に関するクラス'''
 def __init__(self,solid:Literal['dashdot','dashed','dotted','none',None,'None','solid','',' ','-','--','-.',':']=None)->None:self.solid=[self._get(i) for i in solid] if isinstance(solid,(list,tuple)) else [self._get(solid)]
 def _get(self,val):
  for i,key in SOLID.items():
   if val in key:return i
  return None
 def __iter__(self)->None:return iter(self.solid)
 def __len__(self)->int:return len(self.solid)
 def __str__(self):return self.solid[0]
class Marker:
 '''マーカーの設定に関するクラス'''
 def __init__(self,marker:Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','o','p','P','s','v','x','X','$\\alpha$','$\\beta$','$\\gamma$','*','+',',','.','<','>','^','_','|']=None)->None:
  if isinstance(marker,(list,tuple)):self.marker=[self._get(i) for i in marker]
  else:self.marker=[self._get(marker)]
 def _get(self,val):return val if(isinstance(val,str)and fullmatch(r'\$[a-zA-Z]\$',val)or(val in MARKERS)) else None
 def __iter__(self)->None:return iter(self.marker)
 def __len__(self)->int:return len(self.marker)
 def __str__(self):return self.marker[0]
class SCapstyle:
 '''実線の端点の形状を設定する。'''
 def __init__(self,style:Literal['butt','projecting','round']='butt')->None:
  if isinstance(style,(list,tuple)):self.style=[self._get(i) for i in style]
  else:self.style=[self._get(style)]
 def _get(self,val):return listchose(val,['butt','projecting','round'])
 def __iter__(self)->None:return iter(self.style)
 def __len__(self)->int:return len(self.style)
 def __str__(self):return self.style[0]
class Angle:
 '''角度をサポートする。'''
 def __init__(self,val:Numbertype,now:Literal['degrees','radian']='degrees',do:Literal['degrees','radian']='degrees'):
  now,do=listchose(now,['degrees','radian']),listchose(do,['degrees','radian'])
  if not isinstance(val,Numbertype):val=0
  if now==do:self.val=val
  elif now=='degrees' and do=='radian':self.val=val*(pi/180)
  elif now=='radian' and do=='degrees':self.val=val*(180/pi)
 def __int__(self):return int(self.val)
 def __float__(self):return float(self.val)