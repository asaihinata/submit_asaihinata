import numpy as np

from .._graphhelp import *


class Step(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._manyarr(kw.get('data'))
  self.range=self._steprange(kw.get('range'),self.data)
  self.fill=bols(kw.get('fill'),False)
  self.baseline=num0s(kw.get('baseline'))
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'])
  self.colorlist=self._list_loop(self.colorlist,self.max_depth)
  self.label=self.labels(kw.get('label'))
  self.linewidth=num0(kw.get('linewidth'),2)
  self.plot(self.data,xlabel=self.xlabel,ylabel=self.ylabel,range=self.range,fill=self.fill,baseline=self.baseline,orientation=self.orientation)
 def plot(self,data,xlabel=None,ylabel=None,linewidth=2,range=None,fill=False,baseline=0,orientation='vertical'):
  self.clear()
  self.graphdata=[self.ax.stairs(d,linewidth=linewidth,baseline=baseline,fill=fill,color=self.colorlist[i],edgecolor=self.colorlist[i],facecolor=self.colorlist[i],orientation=orientation,label=self.label[i])for i,d in enumerate(data)]
  self.ax.set_xticks(ticks=np.arange(data.shape[1]+1),labels=range.astype('U5'))
  self._apply_labels(xlabel,ylabel)
  self.legend()
 def update(self,data=None,**kw):
  self._updates(**kw)
  if isinstance(data,NpArraytype):self.data=self._manyarr(data)
  self.range=self._steprange(kw.get('range',self.range),self.data)
  self.linewidth=num0(kw.get('linewidth'),self.linewidth)
  self.fill=bols(kw.get('fill',self.fill),self.fill)
  self.baseline=num0s(kw.get('baseline'),self.baseline)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'],self.orientation)
  self.colorlist=self._list_loop(self.colorlist,self.max_depth)
  self.plot(self.data,xlabel=None,ylabel=None,linewidth=self.linewidth,range=self.range,fill=self.fill,baseline=self.baseline,orientation=self.orientation)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data
 def _steprange(self,ranges=None,data=None):
  len1=data.shape[1]+1
  def _array(min,max):
   if max<min:min,max=max,min
   step=(max-min)/(len1-1)
   return np.array([float(step*i+min)for i in range(len1)])
  if isinstance(ranges,np.ndarray) and len(ranges.shape)==1 and ranges.shape[0]==len1:return ranges
  elif isinstance(ranges,(tuple,list)):
   lens=len(ranges)
   if lens==2 and all(isinstance(ranges[i],(int,float))for i in range(2)):return _array(ranges[0],ranges[1])
   elif len1==lens:return np.array([str(i) for i in ranges],dtype=np.str_)
  elif isinstance(ranges,(int,float)):return _array(0,ranges)
  return np.arange(len1)