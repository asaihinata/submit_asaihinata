from tkinter import Canvas, Frame, Scrollbar, Tk

from ..types import FunctionType
from ._function import bols, parsecolor
from ._log import Logger
from .basic import *
from .graph import *

__all__=['WindowController']
logger=Logger(name='window',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
class WindowController:
 '''ウィンドウを生成する。'''
 count=0
 def __init__(self,kw):
  self.title=kw.get('title','window')
  self.layout=kw.get('layout',[])
  if self.layout==None or not isinstance(self.layout,(list,tuple)):
   raise ValueError('layoutに配列を指定してください。')
  self.bg=parsecolor(kw.get('bg'),'#64778d')
  self.scroll_y=bols(kw.get('scroll_y'),False)
  self.scroll_x=bols(kw.get('scroll_x'),False)
  self.root=Tk()
  parent=self.root
  self.root.title(self.title)
  self.root.protocol('WM_DELETE_WINDOW',self._on_window_close)
  self.root.tk_setPalette(background=self.bg)
  self.size=kw.get('size',(None,None))
  self.maxmine=bols(kw.get('maxmine'),False)
  if self.maxmine:self.maxwin()
  self.location=kw.get('location',(0,0))
  self.widgets={}
  self.closed=False
  self._close_result=None
  self.canvas=None
  if self.scroll_y or self.scroll_x:
   self.canvas=Canvas(self.root,bg=self.bg,highlightthickness=0)
   self._inner_frame=Frame(self.canvas,bg=self.bg)
   self.canvas.create_window((0,0),window=self._inner_frame,anchor='nw')
   self._inner_frame.bind('<Configure>',lambda e:self.canvas.configure(scrollregion=self.canvas.bbox('all')))
   if self.scroll_y:
    ybar=Scrollbar(self.root,orient='vertical',command=self.canvas.yview)
    self.canvas.configure(yscrollcommand=ybar.set)
    ybar.pack(side='right',fill='y')
   if self.scroll_x:
    xbar=Scrollbar(self.root,orient='horizontal',command=self.canvas.xview)
    self.canvas.configure(xscrollcommand=xbar.set)
    xbar.pack(side='bottom',fill='x')
   self.canvas.pack(fill='both',expand=True)
   parent=self._inner_frame
  if self.size==(None,None):
   x,y=self.location
   try:self.root.geometry(f'+{int(x)}+{int(y)}')
   except:pass
  else:
   w,h=self.size
   x,y=self.location
   try:self.root.geometry(f'{int(w)}x{int(h)}+{int(x)}+{int(y)}')
   except:self.root.geometry(f'+{int(x)}+{int(y)}')
  if self.layout:
   self._build_layout(self.layout,parent)
  self.loadfun=kw.get('load')
 def scroll_to(self,key):
  w,y=self.widgets.get(key),0
  if not self.canvas or not w:return
  self.root.update_idletasks()
  try:y=self.canvas.canvasy(w.winfo_rooty()-self.canvas.winfo_rooty())
  except:return None
  scroll_region=self.canvas.bbox('all')
  if not scroll_region:return None
  total_height=scroll_region[3]-scroll_region[1]
  if total_height<=0:return None
  self.canvas.yview_moveto(y/total_height)
 def _build_layout(self,layout,parent,bgcolor=None):
  bg=self.bg if bgcolor==None else bgcolor
  for row in layout:
   row_frame=Frame(parent,bg=bg)
   row_frame.pack(fill='x',padx=5,pady=5)
   for kw in row:self._create_element(kw,row_frame,bg)
 def _create_element(self,kw,parent,bgs=None):
  t,key,widget,kw['back_bg']=kw.get('type'),kw.get('key'),None,bgs
  if key==None:kw['key']=f'widget{self.count}'
  if t=='Menus':widget=Menus(parent,kw)
  elif t=='Menubuttons':widget=Menubuttons(parent,kw)
  elif t=='Texts':widget=Texts(parent,kw)
  elif t=='Link':widget=Link(parent,kw)
  elif t=='Images':widget=Images(parent,kw)
  elif t=='Buttons':widget=Buttons(parent,kw)
  elif t=='Input':widget=Input(parent,kw)
  elif t=='Multiline':widget=Multiline(parent,kw)
  elif t=='Listboxs':widget=Listboxs(parent,kw)
  elif t=='TCombobox':widget=TCombobox(parent,kw)
  elif t=='InputNumber':widget=InputNumber(parent,kw)
  elif t=='Radio':widget=Radio(parent,kw)
  elif t=='Checkbox':widget=Checkbox(parent,kw)
  elif t=='FileLoad':widget=FileLoad(parent,kw)
  elif t=='FolderLoad':widget=FolderLoad(parent,kw)
  elif t=='Colorbtn':widget=Colorbtn(parent,kw)
  elif t=='Savebtn':widget=Savebtn(parent,kw)
  elif t=='TProgressbar':widget=TProgressbar(parent,kw)
  elif t=='Tab':
   widget=Tab(parent,kw)
   for tab in kw.get('tabs',[]):
    if not isinstance(tab,(list,tuple)) or len(tab)==0:continue
    frame=Frame(widget.widget,bg=widget.bg)
    widget._add_tab(frame,tab[0])
    if 1<len(tab) and isinstance(tab[1],list):
     try:self._build_layout(tab[1],frame,kw.get('bg'))
     except Exception as e:logger.error(f'Tabレイアウト構築エラー:{e}')
  elif t=='Frames':
   widget=Frames(parent,kw)
   if kw.get('layout'):self._build_layout(kw.get('layout'),widget.widget,kw.get('bg'))
  elif t=='Column':
   widget=Column(parent,kw)
   if kw.get('layout'):self._build_layout(kw.get('layout'),widget.widget,kw.get('bg'))
  elif t=='Table':widget=Table(parent,kw)
  elif t=='Tree':widget=Tree(parent,kw)
  elif t=='Slidebar':widget=Slidebar(parent,kw)
  elif t=='Calendars':widget=Calendars(parent,kw)
  elif t=='Barcode':widget=Barcode(parent,kw)
  elif t=='QRcode':widget=QRcode(parent,kw)
  elif t=='LineGraph':widget=LineGraph(parent,kw)
  elif t=='BarGraph':widget=BarGraph(parent,kw)
  elif t=='BarhGraph':widget=BarhGraph(parent,kw)
  elif t=='Scatter':widget=Scatter(parent,kw)
  elif t=='DScatter':widget=DScatter(parent,kw)
  elif t=='Pie':widget=Pie(parent,kw)
  elif t=='Boxplot':widget=Boxplot(parent,kw)
  elif t=='Waterfall':widget=Waterfall(parent,kw)
  elif t=='Waterfallh':widget=Waterfallh(parent,kw)
  elif t=='Stem':widget=Stem(parent,kw)
  elif t=='Step':widget=Step(parent,kw)
  elif t=='Stack':widget=Stack(parent,kw)
  elif t=='Hist':widget=Hist(parent,kw)
  elif t=='Bubble':widget=Bubble(parent,kw)
  elif t=='Linefill':widget=Linefill(parent,kw)
  else:widget=Texts(parent,{'text':f'Unknown element:{t}'})
  if widget:
   if t=='Menus':self.root.config(menu=widget.widget)
   elif t in ['BarGraph','BarhGraph','Boxplot','Bubble','DBarGraph','DScatter','hist','Hist','LineGraph','Pie','Scatter','Stack','Stem','Step','Waterfall','Waterfallh','Linefill']:widget._pack()
   else:
    try:widget.widget.pack(side='left',padx=5,pady=5)
    except Exception as e:
     widget=Texts(parent,{'text':f'widget error:{t}'}).widget.pack(side='left',padx=5,pady=5)
   if key:self.widgets[key]=widget
   else:self.widgets[f'widget{self.count}']=widget
  self.count+=1
 def get(self,key):
  try:return self.widgets.get(key)
  except Exception as e:
   logger.error(e)
 def get_title(self):
  try:return self.title
  except Exception as e:
   logger.error(f'Title get error:{e}')
 def set_title(self,title):
  try:
   self.title=title
   self.root.title(title)
  except Exception as e:
   logger.error(f'Title change error:{e}')
 def widgetcount(self):return self.count
 def widgetdict(self):return self.widgets
 def widgetlist(self):return list(self.widgets.keys())
 def widgetall(self):return list(self.widgets.values())
 def winclose(self):return 'winclose'
 def _on_window_close(self):
  self._close_result='winclose'
  self.closed=True
  try:self.root.destroy()
  except Exception as e:
   logger.error(f'close error:{e}')
 def close(self):self.root.quit()
 def maxwin(self):
  try:self.root.state('zoomed')
  except:pass
 def minwin(self):
  try:self.root.iconify()
  except:pass
 def runs(self):
  if self.loadfun:self.win_exec_funcs(funcs=self.loadfun)
  if self.canvas:self.root.after(100,self._update_region)
  self.root.withdraw()
 def run(self):
  if self.loadfun:self.win_exec_funcs(funcs=self.loadfun)
  if self.canvas:self.root.after(100,self._update_region)
  self.root.mainloop()
 def _update_region(self):
  try:self.canvas.configure(scrollregion=self.canvas.bbox('all'))
  except:pass
 def win_exec_funcs(self,funcs=None):
  if isinstance(funcs,FunctionType):
   try:funcs()
   except Exception as e:
    logger.error(f'function({funcs.__name__}) error.\n{e}')
  elif isinstance(funcs,list):
   for f in funcs:
    if isinstance(f,FunctionType):
     try:f()
     except Exception as e:
      logger.error(f'function({funcs}) error.\n{e}')
    else:
     logger.warning(f'{f} is not function type')
  else:
   logger.warning('funcs is not function type')