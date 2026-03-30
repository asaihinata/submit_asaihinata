from tkinter import Misc

from matplotlib.collections import FillBetweenPolyCollection, PathCollection
from matplotlib.container import BarContainer, StemContainer
from matplotlib.lines import Line2D
from matplotlib.patches import StepPatch, Wedge
from matplotlib.text import Text
from numpy import float64, ndarray, object_
from numpy.typing import NDArray

from ...types import *
from ..developer import Number

class LineGraph:
 def __init__(
self,
master:Misc=None,
x:n_array=None,
y:n_array=None,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
linewidth:Numbertype=2,
alpha:Numbertype=1,
markersize:Numbertype=10,
marker:Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']=None,
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
color:Colortype|list[Colortype]|tuple[Colortype]=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['horizontal','vertical']='vertical',
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1
)->None:'''折線グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param linewidth: 折線グラフの線の幅を指定する。
 :type linewidth: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param markersize: 折線グラフのマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param marker: 折線グラフのマーカーを指定する。
 :type marker: Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']
 :param linestyle: 折線グラフの線の種類を指定する。
 :type linestyle: Literal['solid','-','dashed','--','dash-dot','-.','dotted',': ','none',None,' ','']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 折れ線グラフの線の色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:n_array,
y:n_array,
fg:Colortype,
bg:Colortype,
xlabel:str,
ylabel:str,
graph_grid:Colortype,
title:str,
marker:str,
markersize:Numbertype,
linestyle:str,
linewidth:Numbertype,
alpha:Numbertype
)->NoReturn:'''折線グラフを再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[Line2D]:'''`Line2D`の配列を返す。'''
 def getx(self)->NDArray[object_]:'''`x`のデータを取得する。'''
 def gety(self)->NDArray[object_]:'''`y`のデータを取得する。'''
class BarGraph:
 def __init__(
self,
master:Misc=None,
x:o_array=None,
y:n_array=None,
logs:bool=False,
align:Literal['center','edge']='center',
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
width:Numbertype=1,
alpha:Numbertype=1,
color:Colortype|list[Colortype]|tuple[Colortype]=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['horizontal','vertical']='vertical',
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1
)->None:'''x軸向きの棒グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param logs: y軸を対数スケールにするかを指定する。
 :type logs: bool
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param width: 棒グラフのバー幅を指定する。
 :type width: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param align: x軸の棒グラフバーの配置を指定する。
 :type align: Literal['center','edge']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 棒グラフのバーの色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:o_array,
y:n_array,
logs:bool,
fg:Colortype,
bg:Colortype,
xlabel:str,
ylabel:str,
graph_grid:Colortype,
title:str,
width:Numbertype,
align:Literal['center','edge']
)->NoReturn:'''棒グラフを再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->NDArray[object_]:'''`x`のデータを取得する。'''
 def gety(self)->NDArray[object_]:'''`y`のデータを取得する。'''
class BarhGraph:
 def __init__(
self,
master:Misc=None,
x:o_array=None,
y:n_array=None,
logs:bool=False,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
color:Colortype|list[Colortype]|tuple[Colortype]=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['horizontal','vertical']='vertical',
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
alpha:Numbertype=1,
height:Numbertype=1,
align:Literal['center','edge']='center'
)->None:'''y軸向きの棒グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param logs: x軸を対数スケールにするかを指定する。
 :type logs: bool
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param height: 棒グラフのバーの幅を指定する。
 :type height: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param align: x軸の棒グラフバーの配置を指定する。
 :type align: Literal['center','edge']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 横向き棒グラフのバーの色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:o_array,
y:n_array,
logs:bool,
fg:Colortype,
bg:Colortype,
xlabel:str,
ylabel:str,
graph_grid:Colortype,
title:str,
height:Numbertype,
align:Literal['center','edge']
)->NoReturn:'''横向き棒グラフを再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->NDArray[object_]:'''`x`のデータを取得する。'''
 def gety(self)->NDArray[object_]:'''`y`のデータを取得する。'''
class Pie:
 def __init__(
self,
master:Misc=None,
data:o_array=None,
startangle:Numbertype=0,
startangletype:bool=True,
shadow:bool=False,
counterclock:bool=False,
labeldistance:Numbertype=1.1,
explode:list[int,float,Number]|tuple[int,float,Number]|int|float|Number=...,
label:labeltype=...,
color:list[Colortype]|tuple[Colortype]=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100
)->None:'''円グラフを作成する。

 :param labeldistance: 中心からラベルの距離を指定する。
 :type labeldistance: Numbertype
 :param explode: 中心から各セグメントの離す距離を指定する。
 :type explode: list[int,float,Number]|tuple[int,float,Number]|int|float|Number
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 円グラフが順番に表示する色を指定する。
 :type color: list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param data: 円グラフのデータを指定する。
 :type data: o_array
 :param label: ラベルを指定する。
 :type label: labeltype
 :param startangle: 各要素の出力を開始する角度を指定する。
 :type startangle: Numbertype
 :param startangletype: 各要素の出力を開始する角度を度数法(True)か弧度法(False)かを指定する。
 :type startangletype: bool
 :param shadow: 円グラフに影を追加するか指定する。
 :type shadow: bool
 :param counterclock: 時計回りで出力するか指定する。
 :type counterclock: bool'''
 def update(
self,
data:o_array,
labeldistance:Numbertype,
startangletype:bool,
explode:list[int,float,Number]|tuple[int,float,Number]|int|float|Number,
startangle:Numbertype,
shadow:bool,
counterclock:bool,
fg:Colortype,
bg:Colortype,
graph_grid:Colortype,
title:str
)->NoReturn:'''円グラフを再表示させる。'''
 def get(self)->list[list[Wedge],list[Text],list[Text]]|list[list[Wedge],list[Text]]:'''`matplotlib.axes.Axes.pie`の`patches`,`texts`,`autotexts`の配列を返す。'''
 def getdata(self)->NDArray[object_]:'''`data`のデータを取得する。'''
class Boxplot:
 def __init__(
self,
master:Misc=None,
data:n_array=None,
width:Numbertype=0.15,
whis:float|TupleFloat2=1.5,
label:labeltype=...,
legend:bool=True,
fill:bool=False,
notch:bool=False,
showfliers:bool=True,
orientation:Literal['horizontal','vertical']='vertical',
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7'
)->None:'''箱ひげ図を作成する。

 :param data: dataのデータを指定する。
 :type data: n_array
 :param label: 箱ひげ図のデータ名を指定する。指定しなかった場合`box`+データの数になる。例)box0,box1
 :type label: labeltype
 :param legend: 凡例を表示させるか指定する。
 :type legend: bool
 :param fill: 箱内を塗りつぶすかを指定する。
 :type fill: bool
 :param notch: 箱の中央をくびれさすか指定する。
 :type notch: bool
 :param showfliers: 外れ値を表示させるか指定する。
 :type showfliers: bool
 :param orientation: 箱ひげ図の向きを指定する。
 :type orientation: Literal['horizontal','vertical'
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param width: 箱の幅を指定する。
 :type width: Numbertype
 :param whis: ひげの開始位置を指定する。
 :type whis: float|TupleFloat2
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype'''
 def update(
self,
data:n_array,
width:Numbertype,
whis:Numbertype,
label:labeltype,
legend:bool,
fill:bool,
notch:bool,
showfliers:bool,
orientation:Literal['horizontal','vertical'],
fg:Colortype,
bg:Colortype,
xlabel:str,
ylabel:str,
graph_grid:Colortype,
title:str
)->NoReturn:'''箱ひげ図を再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[list]:'''`matplotlib.axes.Axes.boxplot`の戻り値,`boxes`,`medians`,`whiskers`,`caps`,`fliers`,`means`の配列を返す。'''
 def getdata(self)->NDArray[object_]:'''`data`のデータを取得する。'''
class Waterfall:
 def __init__(
self,
master:Misc=None,
x:o_array=None,
y:o_array=None,
sums:bool=False,
sumstext:str='sum',
colorline:Colortype='#4477aa',
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['horizontal','vertical']='vertical',
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
ucolor:Colortype='#156082',
dcolor:Colortype='#e97132',
width:Numbertype=1,
alpha:Numbertype=1
)->None:'''x軸向きの滝グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param sums: 合計値を表示するかを指定する。
 :type sums: bool
 :param sumstext: 合計のラベルを指定する。
 :type sumstext: str
 :param colorline: バーとバーを繋げる線の色を指定する。
 :type colorline: Colortype
 :param linestyle: バーとバーを繋げる線の種類を指定する。
 :type linestyle: Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param ucolor: 上昇バーの色を指定する。
 :type ucolor: Colortype
 :param dcolor: 下降バーの色を指定する。
 :type dcolor: Colortype
 :param width: バーの幅を指定する。
 :type width: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype'''
 def update(
self,
x:o_array,
y:o_array,
colorline:Colortype,
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ',''],
fg:Colortype,
bg:Colortype,
xlabel:str,
ylabel:str,
graph_grid:Colortype,
ucolor:Colortype,
dcolor:Colortype,
width:Numbertype,
align:Literal['center','edge'],
alpha:Numbertype
)->NoReturn:'''滝グラフを再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->NDArray[object_]:'''`x`のデータを取得する。'''
 def gety(self)->NDArray[object_]:'''`y`のデータを取得する。'''
class Waterfallh:
 def __init__(
self,
master:Misc=None,
x:o_array=None,
y:o_array=None,
height:Numbertype=1,
sums:bool=False,
sumstext:str='sum',
colorline:Colortype='#4477aa',
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['horizontal','vertical']='vertical',
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
ucolor:Colortype='#156082',
dcolor:Colortype='#e97132',
alpha:Numbertype=1
)->None:'''y軸向きの滝グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param sums: 合計値を表示するかを指定する。
 :type sums: bool
 :param sumstext: 合計のラベルを指定する。
 :type sumstext: str
 :param colorline: バーとバーを繋げる線の色を指定する。
 :type colorline: Colortype
 :param linestyle: バーとバーを繋げる線の種類を指定する。
 :type linestyle: Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param ucolor: 上昇バーの色を指定する。
 :type ucolor: Colortype
 :param dcolor: 下降バーの色を指定する。
 :type dcolor: Colortype
 :param height: バーの幅を指定する。
 :type height: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype'''
 def update(
self,
x:o_array,
y:o_array,
colorline:Colortype,
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ',''],
fg:Colortype,
bg:Colortype,
xlabel:str,
ylabel:str,
graph_grid:Colortype,
title:str,
ucolor:Colortype,
dcolor:Colortype,
height:Numbertype,
align:Literal['center','edge'],
alpha:Numbertype
)->NoReturn:'''横向きの滝グラフを再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[BarContainer]:'''`BarContainer`の配列を返す。'''
 def getx(self)->NDArray[object_]:'''`x`のデータを取得する。'''
 def gety(self)->NDArray[object_]:'''`y`のデータを取得する。'''
class Scatter:
 def __init__(
self,
master:Misc=None,
x:n_array=None,
y:n_array=None,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
marker:Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']='o',
markersize:Numbertype=10,
alpha:Numbertype=1,
color:Colortype|list[Colortype]|tuple[Colortype]=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['horizontal','vertical']='vertical',
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1
)->None:'''散布図を作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param marker: 散布図のマーカーを指定する。
 :type marker: Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']
 :param markersize: 散布図のマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: マーカーの色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:n_array,
y:n_array,
fg:Colortype,
bg:Colortype,
xlabel:str,
ylabel:str,
graph_grid:Colortype,
title:str,
marker:str,
markersize:Numbertype,
linewidth:Numbertype
)->NoReturn:'''散布図を再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[PathCollection]:'''`PathCollection`のリストを返す。'''
 def getx(self)->NDArray[object_]:'''`x`のデータを取得する。'''
 def gety(self)->NDArray[object_]:'''`y`のデータを取得する。'''
class DScatter:
 def __init__(
self,
master:Misc=None,
x:n_array=None,
y:n_array=None,
z:n_array=None,
xlabel:str=...,
ylabel:str=...,
zlabel:str=...,
marker:Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']='o',
markersize:Numbertype=10,
alpha:Numbertype=1,
color:Colortype|list[Colortype]|tuple[Colortype]=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xyz:bool=True,
grid_x:bool=False,
grid_y:bool=False,
grid_z:bool=False,
xmajorint:bool=True,
ymajorint:bool=True,
zmajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
zticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
znumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
mouse_rotation:bool=True,
elev:Numbertype=30,
azim:Numbertype=45
)->None:'''3Dの散布図を作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param z: `z`のデータを指定する。
 :type z: n_array
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param zlabel: z軸のラベルを指定する。
 :type zlabel: str
 :param marker: 散布図のマーカーを指定する。
 :type marker: Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']
 :param markersize: 散布図のマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: マーカーの色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xyz: x軸,y軸,z軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`,`grid_z`より優先度が高い。
 :type grid_xyz: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_y: bool
 :param grid_z: z軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_z: bool
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param zmajorint: z軸の目盛りを整数で自動調整させるか指定する。
 :type zmajorint: bool
 :param ticksshow: x軸,y軸,z軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param zticksshow: z軸のグリッド線と目盛り値について表示するかを指定する。
 :type zticksshow: bool
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param znumticks: z軸の目盛りの数を指定する。
 :type znumticks: Numbertype|None
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param mouse_rotation: 表示されているグラフをマウスで操作できるか指定する。
 :type mouse_rotation: bool
 :param elev: 仰角を度数表記で指定する。
 :type elev: Numbertype
 :param azim: 方位角を度数表記で指定する。
 :type azim: Numbertype'''
 def update(
self,
x:n_array,
y:n_array,
z:n_array,
fg:Colortype,
bg:Colortype,
graph_grid:Colortype,
title:str,
marker:str,
markersize:Numbertype,
linewidth:Numbertype,
elev:Numbertype,
azim:Numbertype,
xlabel:str,
ylabel:str,
zlabel:str
)->NoReturn:'''3Dの散布図を再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸,z軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def invert_z(self)->NoReturn:'''z軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸,z軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getzbound(self)->tuple[float64,float64]:
  '''z軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray,ndarray]:
  '''x軸,y軸,z軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def getzticks(self)->ndarray:
  '''z軸の目盛りの位置を座標で返します。'''
 def get(self)->list[PathCollection]:'''`PathCollection`のリストを返す。'''
 def getx(self)->NDArray[object_]:'''`x`のデータを取得する。'''
 def gety(self)->NDArray[object_]:'''`y`のデータを取得する。'''
 def getz(self)->NDArray[object_]:'''`z`のデータを取得する。'''
class Stem:
 def __init__(
self,
master:Misc=None,
x:n_array=None,
y:n_array=None,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
orientation:Literal['horizontal','vertical']='vertical',
bottom:Numbertype=0,
marker:Literal['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']=...,
line:Literal['-','--','-.','-.']=...,
color:Literal['r','g','b','c','m','y','k','w']|list[Literal['r','g','b','c','m','y','k','w']]|tuple[Literal['r','g','b','c','m','y','k','w']]=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['horizontal','vertical']='vertical',
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1
)->None:'''幹図を作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param orientation: 茎の向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param bottom: ベースラインの位置を指定する。
 :type bottom: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param marker: 幹のマーカーの種類を指定する。
 :type marker: Literal['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']
 :param line: 幹の線の種類を指定する。
 :type line: Literal['-','--','-.','-.']
 :param color: 幹の色を指定する。
 :type color: Literal['r','g','b','c','m','y','k','w']|list[Literal['r','g','b','c','m','y','k','w']]|tuple[Literal['r','g','b','c','m','y','k','w']]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:n_array,
y:n_array,
fg:Colortype,
bg:Colortype,
xlabel:str,
ylabel:str,
graph_grid:Colortype,
title:str,
bottom:Numbertype,
orientation:Literal['horizontal','vertical'],
marker:Literal['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']=...,
line:Literal['-','--','-.','-.']=...
)->NoReturn:'''幹図を再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[StemContainer]:'''`StemContainer`のリストを返す。'''
 def getx(self)->NDArray[object_]:'''`x`のデータを取得する。'''
 def gety(self)->NDArray[object_]:'''`y`のデータを取得する。'''
class Hist:
 def __init__(
self,
master:Misc=None,
data:o_array=None,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
width:Numbertype=1,
min:Numbertype=...,
max:Numbertype=...,
decimalpoint:Numbertype=0,
orientation:Literal['horizontal','vertical']='vertical',
bottom:Numbertype=0,
bins:int|list|range|tuple|ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt']=10,
color:Colortype|list[Colortype]|tuple[Colortype]=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
y_verwrit:Literal['horizontal','vertical']='vertical'
)->None:'''ヒストグラムを作成する。

 :param data: dataのデータを指定する。
 :type data: o_array
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param width: ヒストグラムのバーのサイズを指定する。
 :type width: Numbertype
 :param orientation: ヒストグラムの向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param bottom: ヒストグラムのバーの位置を指定する。
 :type bottom: Numbertype
 :param min: ヒストグラムで表示される最小値を指定する。
 :type min: Numbertype
 :param max: ヒストグラムで表示される最大値を指定する。
 :type max: Numbertype
 :param decimalpoint: ヒストグラムのbinの小数点を指定する。
 :type decimalpoint: Numbertype
 :param bins: binsを指定する。
 :type bins: int|list|range|tuple|ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: ヒストグラムの色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']'''
 def update(
self,
data:o_array,
fg:Colortype,
bg:Colortype,
decimalpoint:Numbertype,
graph_grid:Colortype,
title:str,
bins:int|list|range|tuple|ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt'],
min:Numbertype,
max:Numbertype,
bottom:Numbertype,
orientation:Literal['horizontal','vertical'],
width:Numbertype
)->NoReturn:'''ヒストグラムを再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[ndarray,ndarray,BarContainer]:'''`matplotlib.axes.Axes.hist`の戻り値,`n`,`bins`,`patches`を返す。'''
 def getdata(self)->NDArray[object_]:'''`data`のデータを取得する。'''
 def getrange(self,num:bool=True)->tuple[float64,float64]|tuple[float,float]:'''ヒストグラムの`bins`の上限値と下限値をtuple型で返す。

 :param num: 戻り値内の数値がfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :rtype: tuple[float64,float64]|tuple[float,float]'''
 def getmin(self,num:bool=True)->float64|float:'''ヒストグラムの`bins`の下限値を返す。

 :param num: 戻り値をfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :rtype: float64|float'''
 def getmax(self,num:bool=True)->float64|float:'''ヒストグラムの`bins`の上限値を返す。

 :param num: 戻り値をfloat64型(True)で返すかfloat型(False)で返すか指定する。
 :type num: bool
 :rtype: float64|float'''
class Step:
 def __init__(
self,
master:Misc=None,
data:n_array=...,
linewidth:Numbertype=2,
xlabel:str=...,
ylabel:str=...,
range:int|float|ListNumbertype2|TupleNumbertype2=...,
fill:bool=False,
baseline:Numbertype=0,
orientation:Literal['horizontal','vertical']='vertical',
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
color:Colortype|list[Colortype]|tuple[Colortype]=...,
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
y_verwrit:Literal['horizontal','vertical']='vertical',
label:labeltype=...
)->None:'''階段グラフを作成する。

 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param data: dataのデータを指定する。
 :type data: n_array
 :param linewidth: 線の幅を指定する。
 :type linewidth: Numbertype
 :param range: 階段の端の座標を配列もしくは数値で指定する。
 :type range: int|float|ListNumbertype2|TupleNumbertype2
 :param baseline: 階段の下端の開始位置を指定する。
 :type baseline: Numbertype
 :param fill: 階段の下部から`baseline`の間を塗りつぶすかを指定する。
 :type fill: bool
 :param orientation: グラフの向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param label: ラベルを指定する。
 :type label: labeltype
 :param color: 階段グラフの色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']'''
 def update(
self,
data:n_array,
linewidth:Numbertype,
range:int|float|ListNumbertype2|TupleNumbertype2,
fill:bool,
baseline:Numbertype,
orientation:Literal['horizontal','vertical'],
fg:Colortype,
bg:Colortype,
graph_grid:Colortype,
title:str
)->NoReturn:'''円グラフを再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[StepPatch]:'''`StepPatch`を返す。'''
 def getdata(self)->NDArray[object_]:'''`data`のデータを取得する。'''
class Stack:
 def __init__(
self,
master:Misc=None,
x:n_array=None,
y:n_array=None,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
hatch:Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--',r'-\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||']=None,
baseline:Literal['zero','sym','wiggle','weighted_wiggle']='zero',
color:Colortype|list[Colortype]|tuple[Colortype]=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['horizontal','vertical']='vertical',
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1
)->None:'''積み上げエリアチャートを作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param hatch: 塗りつぶし領域内の模様を指定する。
 :type hatch: Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--',r'-\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||']
 :param baseline: 基準値の算出方法を指定する。
 :type baseline: Literal['zero','sym','wiggle','weighted_wiggle']
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: エリア内のバーの色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:n_array,
y:n_array,
hatch:Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--',r'-\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||'],
baseline:Literal['zero','sym','wiggle','weighted_wiggle'],
fg:Colortype,
bg:Colortype,
xlabel:str,
ylabel:str,
graph_grid:Colortype,
title:str
)->NoReturn:'''散布図を再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[FillBetweenPolyCollection]:'''`FillBetweenPolyCollection`のリストを返す。'''
 def getx(self)->NDArray[object_]:'''`x`のデータを取得する。'''
 def gety(self)->NDArray[object_]:'''`y`のデータを取得する。'''
class Bubble:
 def __init__(
self,
master:Misc=None,
x:n_array=None,
y:n_array=None,
data:n_array=None,
bubblesize:Numbertype=1,
xlabel:str=...,
ylabel:str=...,
marker:Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']='o',
alpha:Numbertype=0.5,
color:Colortype|list[Colortype]|tuple[Colortype]=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1
)->None:'''バブルグラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param data: バブルグラフのバブルの大きさを指定する。
 :type data: n_array
 :param bubblesize: バブルの大きさの倍率を指定する。
 :type bubblesize: Numbertype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param marker: バブルグラフのマーカーを指定する。
 :type marker: Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']
 :param markersize: 散布図のマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: マーカーの色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:n_array,
y:n_array,
bubblesize:Numbertype,
fg:Colortype,
bg:Colortype,
graph_grid:Colortype,
title:str,
marker:str,
markersize:Numbertype,
linewidth:Numbertype,
xlabel:str,
ylabel:str
)->NoReturn:'''バブルグラフを再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[PathCollection]:'''`PathCollection`のリストを返す。'''
 def getx(self)->NDArray[object_]:'''`x`のデータを取得する。'''
 def gety(self)->NDArray[object_]:'''`y`のデータを取得する。'''
 def getdata(self)->NDArray[object_]:'''`data`のデータを取得する。'''
class Linefill:
 def __init__(
self,
master:Misc=None,
x:o_array=...,
ymin:n_array=...,
ymax:n_array=...,
linewidth:Numbertype=0,
centerlinewidth:Numbertype=2,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
alpha:Numbertype=1,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
color:Colortype|list[Colortype]|tuple[Colortype]=...,
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['horizontal','vertical']='vertical',
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1
)->None:'''2つの水平曲線の間の領域を埋めるグラフを作成する。

 :param x: 曲線を定義する節点のx座標を指定する。
 :type x: o_array
 :param ymin: 最初の曲線を定義する節点のy座標を指定する。
 :type ymin: n_array
 :param ymax: 2つ目の曲線を定義する節点のy座標を指定する。
 :type ymax: n_array
 :param linewidth: 境界線の太さを指定する。
 :type linewidth: Numbertype
 :param centerlinewidth: 線の太さを指定する。
 :type centerlinewidth: Numbertype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 領域内の色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
x:o_array,
ymin:n_array,
ymax:n_array,
linewidth:Numbertype,
centerlinewidth:Numbertype,
alpha:Numbertype,
xlabel:str,
ylabel:str,
fg:Colortype,
bg:Colortype,
graph_grid:Colortype,
title:str
)->NoReturn:'''バブルグラフを再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[FillBetweenPolyCollection,Line2D]:'''`PathCollection`のリストを返す。'''
 def getx(self)->NDArray[object_]:'''`x`のデータを取得する。'''
 def getymin(self)->NDArray[object_]:'''`ymin`のデータを取得する。'''
 def getymax(self)->NDArray[object_]:'''`ymax`のデータを取得する。'''
class Ecdf:
 def __init__(
self,
master:Misc=None,
data:n_array=...,
complementary:bool=False,
compress:bool=False,
orientation:Literal['horizontal','vertical']='vertical',
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
linewidth:Numbertype=1.5,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
color:Colortype|list[Colortype]|tuple[Colortype]=...,
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['horizontal','vertical']='vertical',
xmajorint:bool=True,
ymajorint:bool=True,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1
)->None:'''経験的累積分布関数を作成する。

 :param complementary: 補累積分布を描画するか指定する。
 :type complementary: bool
 :param compress: 同一値のデータをまとめて最適化するかどうか指定する。
 :type compress: bool
 :param orientation: プロットの向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param linestyle: 線の種類を指定する。
 :type linestyle: Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']
 :param linewidth: 線の太さを指定する。
 :type linewidth: Numbertype
 :param data: 入力データを指定する。
 :type data: n_array
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 線の色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 def update(
self,
data:o_array,
complementary:bool,
compress:bool,
orientation:Literal['horizontal','vertical'],
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ',''],
linewidth:Numbertype,
fg:Colortype,
bg:Colortype,
decimalpoint:Numbertype,
graph_grid:Colortype,
title:str
)->NoReturn:'''ヒストグラムを再表示させる。'''
 def invert(self)->NoReturn:'''x軸,y軸を反転させる。'''
 def invert_x(self)->NoReturn:'''x軸を反転させる。'''
 def invert_y(self)->NoReturn:'''y軸を反転させる。'''
 def getbound(self)->tuple[
tuple[float64,float64],
tuple[float64,float64]
]:
  '''x軸,y軸の下限値と上限値を昇順で返す。'''
 def getxbound(self)->tuple[float64,float64]:
  '''x軸の下限値と上限値を昇順で返す。'''
 def getybound(self)->tuple[float64,float64]:
  '''y軸の下限値と上限値を昇順で返す。'''
 def getticks(self)->tuple[ndarray,ndarray]:
  '''x軸,y軸の目盛りの位置を座標で返します。'''
 def getxticks(self)->ndarray:
  '''x軸の目盛りの位置を座標で返します。'''
 def getyticks(self)->ndarray:
  '''y軸の目盛りの位置を座標で返します。'''
 def get(self)->list[Line2D]:'''`Line2D`の配列を返す。'''
 def getdata(self)->NDArray[object_]:'''`data`のデータを取得する。'''