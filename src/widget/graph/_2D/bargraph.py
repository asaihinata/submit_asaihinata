from itertools import product

from .._graphhelp import *


class BarGraph(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._onearr(kw.get('x'))
  self.y=self._manyarr(kw.get('y'))
  self.colorlist=self._list_loop(self.colorlist,self.max_depth)
  self.label=self.labels(kw.get('label'))
  self.alpha=range_num(num0s(kw.get('alpha'),1),0,1,1)
  self.width=range_num(num0s(kw.get('width'),1),0,1,1)
  self.align=listchose(kw.get('align'),['center','edge'])
  self.plot(self.x,self.y,label=self.label,xlabel=self.xlabel,ylabel=self.ylabel,alpha=self.alpha,width=self.width,align=self.align)
 def plot(self,x,y,label=None,xlabel=None,ylabel=None,alpha=1,width=0.8,align='center'):
  self.clear()
  self.graphdata=[self.ax.bar(xs,ys,label=label[i],color=self.colorlist[i],alpha=alpha,width=width,edgecolor=self.colorlist[i],align=align)for i,(xs,ys) in enumerate(product(x,y))]
  self._apply_labels(xlabel,ylabel)
  self.legend()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,NpArraytype):self.x=self._onearr(x)
  if isinstance(y,NpArraytype):self.y=self._manyarr(y)
  self.colorlist=self._list_loop(self.colorlist,self.max_depth)
  self.alpha=range_num(num0s(kw.get('alpha'),1),0,1,self.alpha)
  self.width=range_num(num0s(kw.get('width'),1),0,1,self.width)
  self.align=listchose(kw.get('align'),['center','edge'],self.align)
  self.plot(self.x,self.y,label=self.label,xlabel=self.xlabel,ylabel=self.ylabel,alpha=self.alpha,width=self.width,align=self.align)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y
class BarhGraph(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._onearr(kw.get('x'))
  self.y=self._manyarr(kw.get('y'))
  self.colorlist=self._list_loop(self.colorlist,self.max_depth)
  self.label=self.labels(kw.get('label'))
  self.alpha=range_num(num0s(kw.get('alpha'),1),0,1,1)
  self.height=range_num(num0s(kw.get('height'),1),0,1,1)
  self.align=listchose(kw.get('align'),['center','edge'])
  self.plot(self.x,self.y,label=self.label,xlabel=self.xlabel,ylabel=self.ylabel,alpha=self.alpha,height=self.height,align=self.align)
 def plot(self,x,y,label=None,xlabel=None,ylabel=None,alpha=1,height=1,align='center'):
  self.clear()
  self.graphdata=[self.ax.barh(xs,ys,label=label[i],color=self.colorlist[i],alpha=alpha,height=height,align=align)for i,(xs,ys) in enumerate(product(x,y))]
  self._apply_labels(xlabel,ylabel)
  self.legend()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,NpArraytype):self.x=self._onearr(x)
  if isinstance(y,NpArraytype):self.y=self._manyarr(y)
  self.colorlist=self._list_loop(self.colorlist,self.max_depth)
  self.alpha=range_num(num0s(kw.get('alpha'),1),0,1,self.alpha)
  self.height=range_num(num0s(kw.get('height'),1),0,1,self.height)
  self.align=listchose(kw.get('align'),['center','edge'],self.align)
  self.plot(self.x,self.y,label=self.label,xlabel=self.xlabel,ylabel=self.ylabel,alpha=self.alpha,height=self.height,align=self.align)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y