from os import getcwd

import matplotlib.pyplot as plt
from matplotlib.axes._axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import array, ndarray

from ...types import Arraytype, Numbertype
from .._function import (bols, listchose, num0s, num1s, nums, parsecolor,
                         range_num)
from .._log import Logger
from .._save import autofile_save
from ..developer import LIST
from .support.Graphhelp import Marker, Solid
from .support.List import Manylist, Onelist

__all__=['twoDElement','threeDElement']
logger=Logger(name='Graph',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
graph_color=['#4477aa','#ee7733','#228833','#aa66cc','#77aadd','#ffa94d','#55aa55','#cc3311','#cc99ff','#ff8888','#444444','#888888','#332288','#88ccee','#44aa99','#117733','#999933','#ddcc77','#cc6677','#882255','#aa4499','#dddddd']
class GElement:
 def __init__(self,master,kw):
  self.master=master
  self.widget=None
  self._canvas_widget=None
  self.max_depth=1
  self.graphdata=[]
  # グラフの基盤
  self.size=self._size(kw.get('size'))
  self.fg=parsecolor(kw.get('fg'),'#000000')
  self.graph_bg=parsecolor(kw.get('bg'),'#ffffff')
  self.graph_grid=parsecolor(kw.get('graph_grid'),'#b7b7b7')
  self.title=kw.get('title')
  self.colorlist=self._color_check(kw.get('color',graph_color))
  # グラフの表示
  self.dpi=num1s(kw.get('dpi'),100)
  self.fig=Figure(figsize=(self.size[0]/100,self.size[1]/100),dpi=self.dpi,facecolor=self.graph_bg)
  self.ax:Axes|Axes3D
  # ラベル
  self.labeljudge=True
  self.labeltitle=kw.get('labeltitle')
  self.labelframe=bols(kw.get('labelframe'))
  self.labelshadow=bols(kw.get('labelshadow'),False)
  self.labelalpha=range_num(num0s(kw.get('labelalpha'),1),0,1,1)
  # 目盛り
  self.ticksshow=bols(kw.get('ticksshow'),False)
 def photo(self,filename='Graph',ex='.png',dpi=100):
  try:self.fig.savefig(str(autofile_save(title='画像を保存する',defaultextension=listchose(ex,['.png','.eps','.jpg','.jpeg','.pdf','.pgf','.ps','.raw','.rgba','.svg','.svgz','.tif','.tiff','.webp']),initialfile=filename,initialdir=getcwd())),dpi=num1s(dpi,100))
  except Exception as e:
   logger.error(f'error:{e}')
 def _pack(self):
  try:
   widget=FigureCanvasTkAgg(self.fig,master=self.master)
   self._canvas_widget=widget
   widget.get_tk_widget().pack(side='left',padx=5,pady=5)
  except Exception as e:
   logger.error(e)
 def _redraw(self):
  try:
   if self._canvas_widget:self._canvas_widget.draw()
  except Exception as e:
   logger.error(f'Graph redraw error:{e}')
 def _size(self,sizes=(500,400)):
  if isinstance(sizes,Arraytype)and len(list(sizes))==2:
   if isinstance(sizes[0],Numbertype)and isinstance(sizes[1],Numbertype):return tuple(sizes)
   else:
    if not isinstance(sizes[0],Numbertype):sizes[0]=500
    if not isinstance(sizes[1],Numbertype):sizes[1]=400
    return sizes
  else:return(500,400)
 def markers(self,serch=None,num=None):return self._list_loop(list(Marker(serch)),num)
 def lines(self,serch=None,num=None):return self._list_loop(list(Solid(serch)),num)
 def legend(self,anchor=None,loc='upper right'):
  if self.labeljudge:self.ax.legend(bbox_to_anchor=anchor,loc=listchose(loc,['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']),title=self.labeltitle,frameon=self.labelframe,shadow=self.labelshadow,framealpha=self.labelalpha)
 def pielabel(self,data,label=None):
  if isinstance(label,(list,tuple)):
   ldt,lla=len(data),len(label)
   if lla<ldt:
    for i in range(ldt-lla):label.append(lla+i+1)
   elif ldt<lla:label=label[:ldt]
  else:self.labeljudge=False
  return label
 def onelabel(self,label):
  if label==None:self.labeljudge=False
  return label if isinstance(label,str) else ''
 def labels(self,label):
  if label==None:self.labeljudge=False
  if isinstance(label,str):lis=LIST(lists=[label])
  elif isinstance(label,(list,tuple)):lis=LIST(lists=label)
  else:lis=LIST(lists='')
  return lis.get(self.max_depth)
 def _arr(self,val,j=True):
  if not isinstance(val,(list,tuple,ndarray)):
   raise ValueError('配列で指定してください。')
  if isinstance(val,ndarray):reval=val
  elif isinstance(val,(list,tuple)):reval=array(val)
  if len(reval.shape)==1:reval=array([reval])
  if j==True:self.max_depth=max(self.max_depth,reval.shape[0])
  return reval
 def _manyarr(self,val,j=True):
  val=self._arr(list(Manylist(val)),j)
  if len(val.shape)==2:return self._arr(val)
  return self._arr([val])
 def _onearr(self,val,j=True):return self._arr(list(Onelist(val)),j)
 def _dataarr(self,val,j=True):
  if not isinstance(val,(list,tuple,ndarray)):
   raise ValueError('配列で指定してください。')
  if isinstance(val,ndarray):reval=val
  elif isinstance(val,(list,tuple)):reval=array(val)
  if j==True:self.max_depth=max(self.max_depth,reval.shape[0])
  return reval
 def _color_check(self,color):
  relist=graph_color
  if isinstance(color,str):relist=[parsecolor(color,graph_color[0])]
  elif isinstance(color,(list,tuple)):
   set_arr,judge=[],False
   for i in color:
    c=parsecolor(i)
    if c!=None:
     judge=True
     set_arr.append(c)
    if judge:relist=set_arr
  return relist
 def _list_loop(self,lin,num):return LIST(lin).get(num)
class twoDElement(GElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  # ラベル
  self.xlabel=kw.get('xlabel')
  self.ylabel=kw.get('ylabel')
  self.y_verwrit=listchose(kw.get('y_verwrit'),['vertical','horizontal'])
  # グリッド線
  self.grid_xy=bols(kw.get('grid_xy'))
  self.grid_x=bols(kw.get('grid_x'),False)
  self.grid_y=bols(kw.get('grid_y'),False)
  self.xmajorint=bols(kw.get('xmajorint'))
  self.ymajorint=bols(kw.get('ymajorint'))
  # グラフの基盤
  self.ax:Axes=self.fig.add_subplot(111)
  # 目盛り
  self.xticksshow=bols(kw.get('xticksshow'),False)
  self.yticksshow=bols(kw.get('yticksshow'),False)
  self.xticksdirection=listchose(kw.get('xticksdirection'),['out','in','inout'])
  self.yticksdirection=listchose(kw.get('yticksdirection'),['out','in','inout'])
  # その他
  self.x:ndarray
  self.y:ndarray
  self.data:ndarray
  self.setxy=bols(kw.get('setxy'))
  self.ax.xaxis.set_major_locator(MaxNLocator(integer=self.xmajorint))
  self.ax.yaxis.set_major_locator(MaxNLocator(integer=self.ymajorint))
 def _apply_theme_colors(self):
  self.ax.set_facecolor(self.graph_bg)
  self.ax.tick_params(colors=self.fg)
  if self.title!=None:
   self.ax.set_title(self.title)
   self.ax.title.set_color(self.fg)
  self.ax.xaxis.label.set_color(self.fg)
  self.ax.yaxis.label.set_color(self.fg)
  if self.grid_xy:self.ax.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
  else:
   self.ax.grid(False)
   if self.grid_x:self.ax.xaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
   if self.grid_y:self.ax.yaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
 def _apply_labels(self,xlabel,ylabel):
  self.ax.set_xlabel(xlabel,color=self.fg)
  self.ax.set_ylabel(ylabel,color=self.fg,rotation=self.y_verwrit)
 def _arys(self,data):
  if any(isinstance(i,(list,tuple))for i in data):return array(data)
  elif isinstance(data,list):return array([data])
  elif isinstance(data,(tuple,LIST)):return array([list(data)])
  elif isinstance(data,ndarray):return data
  raise TypeError('dataは配列を指定してください。')
 def _xys(self,x,y):
  x,y=self._arys(x),self._arys(y)
  if 2<=x.shape[0] and 2<=y.shape[0]:
   if self.setxy:x=x[0]
   else:y=y[0]
  return x,y
 def _updates(self,**kw):
  self.fg=parsecolor(kw.get('fg'),self.fg)
  self.graph_bg=parsecolor(kw.get('bg'),self.graph_bg)
  self.graph_grid=parsecolor(kw.get('graph_grid'),self.graph_grid)
  self.title=kw.get('title',self.title)
  self.xlabel=kw.get('xlabel',self.xlabel)
  self.ylabel=kw.get('ylabel',self.ylabel)
 def _ticks(self):
  if self.ticksshow:
   self.ax.set_xticks([])
   self.ax.set_yticks([])
  else:
   if self.xticksshow:self.ax.set_xticks([])
   if self.yticksshow:self.ax.set_yticks([])
  plt.rcParams['xtick.direction']=self.xticksdirection
  plt.rcParams['ytick.direction']=self.yticksdirection
 def clear(self):
  self.graphdata=[]
  self.ax.clear()
  self._ticks()
  self._apply_theme_colors()
 def invert_all(self):
  self.invert_y()
  self.invert_x()
 def invert_x(self):self.ax.invert_xaxis()
 def invert_y(self):self.ax.invert_yaxis()
 def getbound(self):return(self.getxbound(),self.getybound)
 def getxbound(self):return self.ax.get_xbound()
 def getybound(self):return self.ax.get_ybound()
class threeDElement(GElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  # グラフの基盤
  self.elev=nums(kw.get('elev'),30)
  self.azim=nums(kw.get('azim'),45)
  self.ax:Axes3D=self.fig.add_subplot(111,projection='3d')
  # ラベル
  self.xlabel=kw.get('xlabel')
  self.ylabel=kw.get('ylabel')
  self.zlabel=kw.get('zlabel')
  # グリッド線
  self.grid_xyz=bols(kw.get('grid_xyz'))
  self.grid_x=bols(kw.get('grid_x'),False)
  self.grid_y=bols(kw.get('grid_y'),False)
  self.grid_z=bols(kw.get('grid_z'),False)
  # 目盛り
  self.xmajorint=bols(kw.get('xmajorint'))
  self.ymajorint=bols(kw.get('ymajorint'))
  self.zmajorint=bols(kw.get('zmajorint'))
  self.xticksshow=bols(kw.get('xticksshow'),False)
  self.yticksshow=bols(kw.get('yticksshow'),False)
  self.zticksshow=bols(kw.get('zticksshow'),False)
  self.xticksdirection=listchose(kw.get('xticksdirection'),['out','in','inout'])
  self.yticksdirection=listchose(kw.get('yticksdirection'),['out','in','inout'])
  if bols(kw.get('mouse_rotation')):self.ax.disable_mouse_rotation()
  self.ax.view_init(self.elev,self.azim)
  self._apply_theme_colors()
  self.ax.xaxis.set_major_locator(MaxNLocator(integer=self.xmajorint))
  self.ax.yaxis.set_major_locator(MaxNLocator(integer=self.ymajorint))
  self.ax.zaxis.set_major_locator(MaxNLocator(integer=self.zmajorint))
 def _updates(self,**kw):
  self.fg=parsecolor(kw.get('fg'),self.fg)
  self.graph_bg=parsecolor(kw.get('bg'),self.graph_bg)
  self.graph_grid=parsecolor(kw.get('graph_grid'),self.graph_grid)
  self.title=kw.get('title',self.title)
  self.elev=nums(kw.get('elev'),self.elev)
  self.azim=nums(kw.get('azim'),self.azim)
  self.xlabel=kw.get('xlabel',self.xlabel)
  self.ylabel=kw.get('ylabel',self.ylabel)
  self.zlabel=kw.get('zlabel',self.zlabel)
 def _apply_theme_colors(self):
  self.ax.set_facecolor(self.graph_bg)
  self.ax.tick_params(colors=self.fg)
  self.ax.set_title(self.title)
  self.ax.title.set_color(self.fg)
  self.ax.xaxis.label.set_color(self.fg)
  self.ax.yaxis.label.set_color(self.fg)
  self.ax.zaxis.label.set_color(self.fg)
  self._apply_grid()
 def _apply_grid(self):
  if self.grid_xyz:self.ax.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
  else:
   if self.grid_x:self.ax.xaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
   if self.grid_y:self.ax.yaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
   if self.grid_z:self.ax.zaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
 def _apply_labels(self,xlabel,ylabel,zlabel):
  self.ax.set_xlabel(xlabel,color=self.fg)
  self.ax.set_ylabel(ylabel,color=self.fg)
  self.ax.set_zlabel(zlabel,color=self.fg)
  self._apply_grid()
 def clear(self):
  self.graphdata=[]
  self.ax.clear()
  self._ticks()
  self._apply_theme_colors()
 def _ticks(self):
  if self.ticksshow:
   self.ax.set_xticks([])
   self.ax.set_yticks([])
   self.ax.set_zticks([])
  else:
   if self.xticksshow:self.ax.set_xticks([])
   if self.yticksshow:self.ax.set_yticks([])
   if self.zticksshow:self.ax.set_zticks([])
  plt.rcParams['xtick.direction']=self.xticksdirection
  plt.rcParams['ytick.direction']=self.yticksdirection
 def invert_all(self):
  self.invert_x()
  self.invert_y()
  self.invert_z()
 def invert_x(self):self.ax.invert_xaxis()
 def invert_y(self):self.ax.invert_yaxis()
 def invert_z(self):self.ax.invert_zaxis()