from .._graphhelp import *


class Ecdf(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._manyarr(kw.get('data'))
  self.colorlist=self._list_loop(self.colorlist,self.max_depth)
  self.complementary=bols(kw.get('complementary'),False)
  self.compress=bols(kw.get('compress'),False)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'])
  self.line=self.lines(kw.get('linestyle','-'),self.max_depth)
  self.linewidth=num0(kw.get('linewidth'),1.5)
  self.plot(self.data,xlabel=self.xlabel,ylabel=self.ylabel,complementary=self.complementary,compress=self.compress,orientation=self.orientation,linewidth=self.linewidth,line=self.line)
 def plot(self,data,xlabel=None,ylabel=None,complementary=False,compress=False,orientation='vertical',linewidth=1.5,line='-'):
  self.clear()
  for i in range(self.max_depth):
   color=self.colorlist[i]
   self.graphdata.append(self.ax.ecdf(data[i],compress=compress,color=color,complementary=complementary,orientation=orientation,linewidth=linewidth,linestyle=line[i]))
  self._apply_labels(xlabel,ylabel)
 def update(self,data=None,**kw):
  self._updates(**kw)
  if isinstance(data,NpArraytype):self.data=self._manyarr(data)
  self.colorlist=self._list_loop(self.colorlist,self.max_depth)
  self.complementary=bols(kw.get('complementary'),self.complementary)
  self.compress=bols(kw.get('compress'),self.compress)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'],self.orientation)
  self.line=self.lines(kw.get('linestyle',self.line),self.max_depth)
  self.linewidth=num0(kw.get('linewidth'),self.linewidth)
  self.plot(self.data,xlabel=self.xlabel,ylabel=self.ylabel,complementary=self.complementary,compress=self.compress,orientation=self.orientation,linewidth=self.linewidth,line=self.line)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data