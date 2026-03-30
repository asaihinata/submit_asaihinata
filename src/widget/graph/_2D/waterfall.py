from .._graphhelp import *


def _waterfall_sum(data):
 arr,set_num=np.array([]),0
 for i,num in enumerate(data):
  arr=np.append(arr,0 if i==0 else set_num)
  set_num=set_num+num
 return arr
def _bar_x_lists(lists,ylen):
 if ylen==None or not isinstance(lists,NpArraytype):return None
 else:
  lists=lists[0]
  xlen=len(lists)
  if xlen==ylen or xlen<ylen:return[str(i) for i in lists]
  else:return[lists[i] for i in range(xlen)]
class Waterfall(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.y=self._dataarr(kw.get('y'),False)
  self.x=_bar_x_lists(self._onearr(kw.get('x')),len(self.y))
  self.bottom=_waterfall_sum(self.y)
  self.label=self.onelabel(kw.get('label'))
  self.ucolor=parsecolor(kw.get('ucolor'),'#156082')
  self.dcolor=parsecolor(kw.get('dcolor'),'#e97132')
  self.color=[(self.dcolor if i<=0 else self.ucolor)for i in self.y]
  self.alpha=range_num(num0s(kw.get('alpha'),1),0,1,1)
  self.width=range_num(num0s(kw.get('width'),1),0,1,1)
  self.sums=bols(kw.get('sums'),False)
  self.sumstext=kw.get('sumstext','sum')
  self.colorline=parsecolor(kw.get('colorline'),'#4477aa')
  self.linestyles=str(Solid(kw.get('linestyles','-')))
  self.plot(self.x,self.y,label=self.label,xlabel=self.xlabel,ylabel=self.ylabel,alpha=self.alpha,width=self.width,sums=self.sums,sumstext=self.sumstext,bottom=self.bottom,color=self.colorline,linestyles=self.linestyles)
 def plot(self,x,y,label=None,xlabel=None,ylabel=None,alpha=1,width=1,sums=False,sumstext='sum',bottom=None,color=None,linestyles='-'):
  self.clear()
  if sums:x,y,bottom=np.append(x,sumstext),np.append(y,y.sum()),np.append(bottom,0)
  self.graphdata=[self.ax.bar(x,y,label=label,color=self.color,alpha=alpha,width=width,align='center',bottom=bottom)]
  self._horiline(np.cumsum(y),width,color,linestyles)
  self._apply_labels(xlabel,ylabel)
  self.legend()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  self.sums=bols(kw.get('sums'),self.sums)
  self.sumstext=kw.get('sumstext',self.sumstext)
  if isinstance(y,NpArraytype):self.y=self._dataarr(kw.get('y'),False)
  if isinstance(x,NpArraytype):self.x=_bar_x_lists(self._onearr(x),len(y))
  self.bottom=_waterfall_sum(self.y)
  self.ucolor=parsecolor(kw.get('ucolor'),self.ucolor)
  self.dcolor=parsecolor(kw.get('dcolor'),self.dcolor)
  self.color=[(self.dcolor if i<=0 else self.ucolor)for i in self.y]
  self.alpha=range_num(num0s(kw.get('alpha'),1),0,1,self.alpha)
  self.width=range_num(num0s(kw.get('width'),1),0,1,self.width)
  self.colorline=parsecolor(kw.get('colorline'),self.colorline)
  self.linestyles=str(Solid(kw.get('linestyles',self.linestyles)))
  self.plot(self.x,self.y,label=self.label,xlabel=self.xlabel,ylabel=self.ylabel,alpha=self.alpha,width=self.width,sums=self.sums,sumstext=self.sumstext,bottom=self.bottom,color=self.colorline,linestyles=self.linestyles)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y
 def _horiline(self,lin,width=1,color=None,linestyles='-'):
  lens,width,xmaxs,xmins=len(lin)-1,width/2,[],[]
  for i in range(lens):
   if lin[i]==lin[i+1]:ma,mi=i+width,i+1.5
   else:ma,mi=i+1-width,i+width
   xmaxs.append(ma)
   xmins.append(mi)
  self.ax.hlines(y=lin,xmin=xmins+[0],xmax=xmaxs+[0],colors=color,linestyles=linestyles)
class Waterfallh(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.y=self._dataarr(kw.get('y'),False)
  self.x=_bar_x_lists(self._onearr(kw.get('x')),len(self.y))
  self.bottom=_waterfall_sum(self.y)
  self.label=self.onelabel(kw.get('label'))
  self.ucolor=parsecolor(kw.get('ucolor'),'#156082')
  self.dcolor=parsecolor(kw.get('dcolor'),'#e97132')
  self.color=[(self.dcolor if i<0 else self.ucolor) for i in self.y]
  self.alpha=range_num(num0s(kw.get('alpha'),1),0,1,1)
  self.height=range_num(num0s(kw.get('height'),1),0,1,1)
  self.sums=bols(kw.get('sums'),False)
  self.sumstext=kw.get('sumstext','sum')
  self.colorline=parsecolor(kw.get('colorline'),'#4477aa')
  self.linestyles=str(Solid(kw.get('linestyles','-')))
  self.plot(self.x,self.y,label=self.label,xlabel=self.xlabel,ylabel=self.ylabel,alpha=self.alpha,height=self.height,sums=False,sumstext='sum',bottom=None,color=self.colorline,linestyles=self.linestyles)
 def plot(self,x,y,label=None,xlabel=None,ylabel=None,alpha=1,height=1,sums=False,sumstext='sum',bottom=None,color=None,linestyles='-'):
  self.clear()
  if sums:x,y,bottom=np.append(x,sumstext),np.append(y,y.sum()),np.append(bottom,0)
  self.graphdata=[self.ax.barh(x,y,label=label,color=self.color,alpha=alpha,height=height,align='center',left=self.bottom)]
  self._vlines(np.cumsum(y),height,color,linestyles)
  self._apply_labels(xlabel,ylabel)
  self.legend()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  self.sums=bols(kw.get('sums'),self.sums)
  self.sumstext=kw.get('sumstext',self.sumstext)
  if isinstance(y,NpArraytype):self.y=self._dataarr(kw.get('y'),False)
  if isinstance(x,NpArraytype):self.x=_bar_x_lists(self._onearr(x),len(self.y))
  self.ucolor=parsecolor(kw.get('ucolor'),self.ucolor)
  self.dcolor=parsecolor(kw.get('dcolor'),self.dcolor)
  self.color=[(self.dcolor if i<=0 else self.ucolor)for i in self.y]
  self.alpha=range_num(num0s(kw.get('alpha'),1),0,1,self.alpha)
  self.height=range_num(num0s(kw.get('height'),1),0,1,self.height)
  self.colorline=parsecolor(kw.get('colorline'),self.colorline)
  self.linestyles=str(Solid(kw.get('linestyles',self.linestyles)))
  self.plot(self.x,self.y,label=self.label,xlabel=self.xlabel,ylabel=self.ylabel,alpha=self.alpha,height=self.height,color=self.colorline,linestyles=self.linestyles)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y
 def _vlines(self,lin,height=1,color=None,linestyles='-'):
  lens,height,xmaxs,xmins=len(lin)-1,height/2,[],[]
  for i in range(lens):
   if lin[i]==lin[i+1]:ma,mi=i+height,i+1.5
   else:ma,mi=i+1-height,i+height
   xmaxs.append(ma)
   xmins.append(mi)
  self.ax.vlines(x=lin,ymin=xmins+[0],ymax=xmaxs+[0],colors=color,linestyles=linestyles)