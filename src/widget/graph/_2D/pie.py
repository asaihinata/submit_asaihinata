from ...developer import Number
from .._graphhelp import *


class Pie(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._dataarr(kw.get('data'))
  self.colorlist=self._list_loop(self.colorlist,self.max_depth)
  self.label=self.pielabel(self.data,kw.get('label'))
  self.startangle=nums(kw.get('startangle'),0)
  self.startangletype=bols(kw.get('startangletype'))
  self.shadow=bols(kw.get('shadow'),False)
  self.counterclock=bols(kw.get('counterclock'),False)
  self.labeldistance=num0(kw.get('labeldistance'),1.1)
  explode=kw.get('explode')
  if isinstance(explode,(list,tuple)) and all(isinstance(i,(int,float,Number))for i in explode):self.explode=list(map(float,explode))
  elif isinstance(explode,(int,float,Number)):self.explode=[float(explode) for _ in range(self.max_depth)]
  else:self.explode=None
  self.plot(self.data,startangle=self.startangle,shadow=self.shadow,counterclock=self.counterclock,label=self.label,labeldistance=self.labeldistance,explode=self.explode,startangletype=self.startangletype)
 def plot(self,data,startangle=0.0,shadow=False,counterclock=True,label=None,labeldistance=1.1,explode=None,startangletype=True):
  self.clear()
  if not startangletype:startangle=float(Angle(startangle,now='radian',do='degrees'))
  self.graphdata=list(self.ax.pie(data,labels=label,startangle=90-startangle,shadow=shadow,counterclock=counterclock,labeldistance=labeldistance,explode=explode))
  self.legend(anchor=(1,1),loc='upper left')
 def update(self,data=None,**kw):
  self._updates(**kw)
  if isinstance(data,NpArraytype):self.data=self._dataarr(data)
  self.colorlist=self._list_loop(self.colorlist,self.max_depth)
  explode=kw.get('explode',self.explode)
  if isinstance(explode,(list,tuple)) and all(isinstance(i,(int,float,Number))for i in explode):self.explode=list(map(float,explode))
  elif isinstance(explode,(int,float,Number)):self.explode=[float(explode) for _ in range(self.max_depth)]
  else:self.explode=None
  self.label=self.pielabel(self.data,kw.get('label',self.label))
  self.startangle=nums(kw.get('startangle'),self.startangle)
  self.startangletype=bols(kw.get('startangletype'),self.startangletype)
  self.shadow=bols(kw.get('shadow'),self.shadow)
  self.counterclock=bols(kw.get('counterclock'),self.counterclock)
  self.labeldistance=num0(kw.get('labeldistance'),self.labeldistance)
  self.plot(self.data,startangle=self.startangle,shadow=self.shadow,counterclock=self.counterclock,label=self.label,labeldistance=self.labeldistance,explode=self.explode,startangletype=self.startangletype)
  self._redraw()
 def get(self):return self.graphdata[0]
 def getdata(self):return self.data