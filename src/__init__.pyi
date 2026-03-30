import logging
from datetime import datetime
from tkinter import StringVar, _Cursor
from typing import Union

from numpy import ndarray

from .types import *
from .widget import *

class sgg:
 @classmethod
 def window(
cls,
layout:list|tuple=...,
title:str='window',
load:function|list[function,]=None,
bg:Colortype='#64778d',
scroll_x:bool=False,
scroll_y:bool=False,
size:TupleNumbertype2=(None,None),
maxmine:bool=False,
location:TupleNumbertype2=(0,0)
)->WindowController:'''ウィンドウを生成する。

 :param layout: ウィンドウで表示されるウィジェットを指定する。各リストがウィンドウのその行に対応し,その中に配置したウィジェットが左から順に並びます。
 :type layout: list|tuple
 :param title: ウィンドウに表示されるタイトル名を指定する。
 :type title: str
 :param load: ウィンドウ表示時に実行される関数を指定する。
 :type load: function|list[function,]
 :param bg: ウィンドウの背景を指定する。
 :type bg: Colortype
 :param scroll_x: ウィンドウのx軸方向にスクロールできるか指定する。
 :type scroll_x: bool
 :param scroll_y: ウィンドウのy軸方向にスクロールできるか指定する。
 :type scroll_y: bool
 :param size: ウィンドウの幅と高さを指定する。
 :type size: TupleNumbertype2
 :param maxmine: ウィンドウ表示時最大化するかを指定する。
 :type maxmine: bool
 :param location: ウィンドウの表示位置を指定する。
 :type location: TupleNumbertype2'''
 @staticmethod
 def Texts(
text:str=...,
size:TupleNumbertype2=(None,None),
bg:Colortype=...,
fg:Colortype=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
takefocus:bool=True,
key:str=...,
bd:Numbertype=0,
pady:Numbertype=...,
padx:Numbertype=...,
wraplength:Numbertype=0,
cursor:_Cursor=...,
justify:Literal['left','center','right']='left',
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='w',
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat'
)->dict:'''テキストを生成する。

 :param text: Textsウィジェットに表記させる文字を指定する。
 :type text: str'''
 @staticmethod
 def Link(
text:str=...,
link:Linktype|None=None,
key:str=...,
takefocus:bool=True,
pady:Numbertype=...,
padx:Numbertype=...,
wraplength:Numbertype=0,
cursor:_Cursor=...,
bd:Numbertype=0,
bg:Colortype=...,
fg:Colortype='#0000ee',
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=True,
overstrike:bool=False,
size:TupleNumbertype2=(None,None),
justify:Literal['left','center','right']='left',
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='w',
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat'
)->dict:'''リンクテキストを生成する。

 :param text: Linkウィジェットに表記させる文字を指定する。
 :type text: str
 :param link: Linkウィジェットが押されたときにブラウザで開くURLのリンクを指定する。
 :type link: Linktype|None'''
 @staticmethod
 def Images(
path:str=...,
byto:bytes=...,
name:str='No Images',
takefocus:bool=True,
key:str=...
)->dict:'''画像を生成する。

 :param path: Imagesウィジェットに表示させる画像のパスを指定する。
 :type path: str
 :param byto: Imagesウィジェットに表示させる画像のバイトデータを指定する。
 :type byto: bytos
 :param name: 指定されたpathもしくはbytoに何らかの例外が出た場合にImagesウィジェットに表示される文字を指定する。
 :type name: str'''
 @staticmethod
 def Buttons(
text:str=...,
function:function=...,
key:str=...,
takefocus:bool=True,
pady:Numbertype=...,
padx:Numbertype=...,
wraplength:Numbertype=0,
cursor:_Cursor=...,
bg:Colortype=...,
fg:Colortype=...,
bd:Numbertype=0,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
size:TupleNumbertype2=(None,None),
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat',
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='w'
)->dict:'''ボタンを生成する。

 :param text: Buttonsウィジェットに表記させる文字を指定する。
 :type text: str
 :param function: Buttonsウィジェットが押された時実行される関数を指定する。
 :type function: function'''
 @staticmethod
 def Input(
text:str=...,
show:str=...,
insertwidth:Numbertype=2,
insertbg:Colortype='#000000',
width:Numbertype=20,
key:str=...,
bd:Numbertype=0,
takefocus:bool=True,
cursor:_Cursor=...,
bg:Colortype=...,
fg:Colortype=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat',
justify:Literal['left','center','right']='left'
)->dict:'''入力欄を生成する。

 :param text: Inputウィジェットに表記させる文字を指定する。
 :type text: str
 :param width: Inputウィジェットの幅の長さを指定する。
 :type width: Numbertype
 :param insertwidth: Inputウィジェットの入力時の挿入ポイントの幅を指定する。
 :type insertwidth: Numbertype
 :param insertbg: Inputウィジェットの入力時の挿入ポイントの色を指定する。
 :type insertbg: Colortype
 :param show: 実際の入力内容の各文字の代わりに表示させる文字を指定する。
 :type show: str'''
 @staticmethod
 def Multiline(
text:str=...,
insertbg:Colortype='#000000',
insertwidth:Numbertype=2,
width:Numbertype=20,
height:Numbertype=5,
key:str=...,
bd:Numbertype=1,
takefocus:bool=True,
padx:Numbertype=...,
pady:Numbertype=...,
cursor:_Cursor=...,
bg:Colortype=...,
fg:Colortype=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
wrap:Literal['none','word','char']='none',
state:Literal['normal','disabled']='normal',
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat',
justify:Literal['left','center','right']='left'
)->dict:'''テキストエリアを生成する。

 :param text: Multilineウィジェットに表記させる文字を指定する。
 :type text: str
 :param insertwidth: Multilineウィジェットの入力時の挿入ポイントの幅を指定する。
 :type insertwidth: Numbertype
 :param insertbg: Multilineウィジェットの入力時の挿入ポイントの色を指定する。
 :type insertbg: Colortype
 :param state: 選択操作の有無を指定する。normalは操作可能にする。disabledは操作不可能にする。
 :type state: Literal['normal','disabled']'''
 @staticmethod
 def Table(
header_fg:Colortype='#000000',
header_bg:Colortype='#cccccc',
values:list=...,
header:list=...,
height:Numbertype=1,
rowheader:list=...,
colwidth:Numbertype=120,
rowheight:Numbertype=50,
bg:Colortype='#e0e0e0',
key:str=...
)->dict:'''表を生成する。

 :param header_fg: Tableウィジェットの見出しの文字色を指定する。
 :type header_fg: Colortype
 :param header_bg: Tableウィジェットの見出しの背景色を指定する。
 :type header_bg: Colortype
 :param values: Tableウィジェット本体に表示させる文字の配列を指定する。
 :type values: list
 :param header: Tableウィジェット見出しに表示させる文字の配列を指定する。
 :type header: list
 :param rowheader: Tableウィジェットの縦列の見出しを配列で指定し,それを設置する。
 :type rowheader: list
 :param colwidth: Tableウィジェットの幅を指定する。
 :type colwidth: Numbertype
 :param rowheight: Tableウィジェットのセルの高さを指定する。
 :type rowheight: Numbertype
 :param height: Tableウィジェットに表示できる行を指定する。
 :type height: Numbertype'''
 @staticmethod
 def Tree(
values:list=...,
header:list=...,
key:str=...,
bg:Colortype='#e0e0e0',
colwidth:Numbertype=120,
header_fg:Colortype='#000000',
header_bg:Colortype='#cccccc',
rowheight:Numbertype=50,
side_header:str=...
)->dict:'''ツリーを生成する。

 :param header_fg: Treeウィジェットの見出しの文字色を指定する。
 :type header_fg: Colortype
 :param header_bg: Treeウィジェットの見出しの背景色を指定する。
 :type header_bg: Colortype
 :param side_header: Treeウィジェットの階層列のテキストを指定する。
 :type side_header: str
 :param values: Treeウィジェット本体に表示させる文字の配列を指定する。
 :type values: list
 :param header: Treeウィジェット見出しに表示させる文字の配列を指定する。
 :type header: list
 :param rowheader: Treeウィジェットの縦列の見出しを配列で指定し,それを設置する。
 :type rowheader: list
 :param colwidth: Treeウィジェットの幅を指定する。
 :type colwidth: Numbertype
 :param rowheight: Treeウィジェットのセルの高さを指定する。
 :type rowheight: Numbertype'''
 @staticmethod
 def Listboxs(
values:Arraytype=...,
width:Numbertype=20,
height:Numbertype=5,
selectfg:Colortype=...,
selectbg:Colortype=...,
select:int=0,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
fg:Colortype='#000000',
bg:Colortype='#e0e0e0',
bd:Numbertype=0,
state:Literal['normal','disabled']='normal',
exportselection:bool=False,
selectmode:Literal['browse','single','multiple','extended']='browse',
key:str=...
)->dict:'''リストボックスを生成する。

 :param values: Listboxウィジェットに表記させるリストを指定する。
 :type values: Arraytype
 :param selectfg: Listboxウィジェットのリストに選択されているリストの文字色を指定する。
 :type selectfg: Colortype
 :param selectbg: Listboxウィジェットのリストに選択されているリストの背景色を指定する。
 :type selectbg: Colortype
 :param select: 選択項目の初期値を指定する。
 :type select: int
 :param exportselection: 選択中の項目のコピー操作を指定する。
 :type exportselection: bool
 :param state: 選択操作の有無を指定する。normalは操作可能にする。disabledは操作不可能にする。
 :type state: Literal['normal','disabled']
 :param selectmode: 選択可能な項目数と操作方法を指定する。
 :type selectmode: Literal['browse','single','multiple','extended']'''
 @staticmethod
 def TCombobox(
values:list=[],
default:str=...,
state:Literal['normal','readonly','disabled']='normal',
key:str=...,
bd:Numbertype=0,
padx:Numbertype=...,
pady:Numbertype=...
)->dict:'''コンボボックスを生成する。

 :param values: 選択項目を指定する。
 :type values: list
 :param default: 入力項目の初期テキストを指定する。
 :type default: str
 :param state: 値の入力制限やTComboboxウィジェットの有効化や無効化について指定する。
 :type state: Literal['normal','readonly','disabled']'''
 @staticmethod
 def Radio(
text:str=...,
group:str='default',
key:str=...,
wraplength:Numbertype=0,
bd:Numbertype=0
)->dict:'''ラジオボタンを生成する。読み込み時,グループの最初のRadioウィジェットが選択される。

 :param text: Radioウィジェットに表記させる文字を指定する。
 :type text: str
 :param group: Radioウィジェットのグループを指定する。同じ名前にすることで,そのグループ内で排他的な選択を実施する。
 :type group: str'''
 @staticmethod
 def Checkbox(
text:str=...,
default:bool=False,
key:str=...,
wraplength:Numbertype=0,
bd:Numbertype=0
)->dict:'''チェックボタンを生成する。

 :param text: Checkboxウィジェットに表記させる文字を指定する。
 :type text: str
 :param default: 読み込み時,Checkboxウィジェットがチェックするかを指定する。
 :type default: bool'''
 @staticmethod
 def Frames(
title:str=...,
layout:list=...,
labelanchor:Literal['nw','n','ne','w','center','e','sw','s','se']='nw',
key:str=...,
takefocus:bool=True,
pady:Numbertype=...,
padx:Numbertype=...,
cursor:_Cursor=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
bg:Colortype=...,
fg:Colortype=...,
relief:Literal['raised','sunken','flat','ridge','solid','groove']='solid',
bd:Numbertype=1
)->dict:'''枠線付きのフレームを生成する。

 :param layout: Framesウィジェットに表示させるウィジェットを指定する。各リストがウィンドウのその行に対応し,その中に配置したウィジェットが左から順に並びます。
 :type layout: list[list]
 :param labelanchor: タイトルを表記する場所を指定する。
 :type labelanchor: Literal['nw','n','ne','w','center','e','sw','s','se']
 :param title: Framesウィジェットのタイトルを指定する。
 :type title: str'''
 @staticmethod
 def Menus(
list:list=...,
tearoff:bool=False,
takefocus:bool=True,
cursor:_Cursor=...,
bg:Colortype=...,
fg:Colortype=...,
bd:Numbertype=0,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat',
key:str=...
)->dict:'''メニューバーを生成する。

 :param list: Menusウィジェットに表示させるメニューを指定する。
 :type list: list
 :param tearoff: メニューウィジェットを独立したウィンドウにするかを指定する。
 :type tearoff: bool'''
 @staticmethod
 def Menubuttons(
list:list=...,
text:str=...,
tearoff:bool=False,
key:str=...,
takefocus:bool=True,
pady:Numbertype=...,
padx:Numbertype=...,
cursor:_Cursor=...,
bg:Colortype=...,
fg:Colortype=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
bd:Numbertype=0,
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='w',
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat'
)->dict:'''メニューボタンを生成する。

 :param text: MenuButtonsウィジェットのボタンに表記させる文字を指定する。
 :type text: str
 :param list: MenuButtonsウィジェットに表示させるメニューを指定する。
 :type list: list
 :param tearoff: メニューウィジェットを独立したウィンドウにするかを指定する。
 :type tearoff: bool'''
 @staticmethod
 def Column(
layout:list[list]=[[]],
key:str=...,
bd:Numbertype=0,
takefocus:bool=True,
pady:Numbertype=...,
padx:Numbertype=...,
cursor:_Cursor=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
bg:Colortype=...,
fg:Colortype=...,
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat'
)->dict:'''フレームを生成する。

 :param layout: Columnウィジェットに表示させるウィジェットを指定する。各リストがウィンドウのその行に対応し,その中に配置したウィジェットが左から順に並びます。
 :type layout: list[list]'''
 @staticmethod
 def Slidebar(
value:Numbertype=0,
digits:int=0,
resolution:Numbertype=1,
length:Numbertype=200,
orientation:Literal['horizontal','vertical']='horizontal',
min:Numbertype=0,
max:Numbertype=100,
key:str=...,
bd:Numbertype=1
)->dict:'''スライダーを生成する。

 :param digits: スケールの値を文字列として取得した際の数値の最大桁数を指定する。
 :type digits: int
 :param resolution: スライダーのステップ数を指定する。
 :type resolution: Numbertype
 :param length: Slidebarウィジェットの長さを指定する。
 :type length: Numbertype
 :param orientation: Slidebarウィジェットの向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param min: Slidebarウィジェットの数値の最小値を指定する。
 :type min: Numbertype
 :param max: Slidebarウィジェットの数値の最大値を指定する。
 :type max: Numbertype
 :param value: Slidebarウィジェットの読み込み時の初期値を指定する。
 :type value: Numbertype'''
 @staticmethod
 def InputNumber(
values:Numbertype=0,
min:Numbertype=0,
max:Numbertype=100,
insertwidth:Numbertype=2,
insertbg:Colortype='#000000',
increment:Numbertype=1,
width:Numbertype=20,
wrap:bool=False,
key:str=...,
bg:Colortype=...,
bd:Numbertype=0,
justify:Literal['left','center','right']='left'
)->dict:'''数値専用の入力欄を生成する。

 :param wrap: 数値が`max`もしくは`min`で指定した範囲外を選択しようとした場合,`max`より大きい数値の場合は`min`へ`min`より小さい数値の場合は`max`へ移動するかを指定する。
 :type wrap: bool
 :param insertwidth: InputNumberウィジェットの入力時の挿入ポイントの幅を指定する。
 :type insertwidth: Numbertype
 :param insertbg: InputNumberウィジェットの入力時の挿入ポイントの色を指定する。
 :type insertbg: Colortype
 :param increment: スライダーのステップ数を指定する。
 :type increment: Numbertype
 :param min: Slidebarウィジェットの数値の最小値を指定する。
 :type min: Numbertype
 :param max: Slidebarウィジェットの数値の最大値を指定する。
 :type max: Numbertype
 :param value: Slidebarウィジェットの読み込み時の初期値を指定する。
 :type value: Numbertype'''
 @staticmethod
 def FileLoad(
text:str='select File',
title:str='select File',
key:str=...,
bg:Colortype=...,
fg:Colortype=...,
wraplength:Numbertype=0,
bd:Numbertype=0,
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='center'
)->dict:'''ファイルパスを取得するダイアログを発生させるボタンを生成する。

 :param text: FileLoadウィジェットのボタンに表示させる文字を指定する。
 :type text: str
 :param title: ファイルを選択するダイアログのタイトルを指定する。
 :type title: str'''
 @staticmethod
 def FolderLoad(
text:str='select Folder',
title:str='select Folder',
key:str=...,
bg:Colortype=...,
wraplength:Numbertype=0,
bd:Numbertype=0,
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='center'
)->dict:'''ファイルパスを取得するダイアログを発生させるボタンを生成する。

 :param text: FolderLoadウィジェットのボタンに表示させる文字を指定する。
 :type text: str
 :param title: フォルダを選択するダイアログのタイトルを指定する。
 :type title: str'''
 @staticmethod
 def Savebtn(
initialfile:str=...,
initialdir:str=...,
filetypes:list[tuple[str,str]]=[('All files','*.*')],
defaultextension:str='.txt',
text:str='Save file',
title:str='Save file',
key:str=...,
bg:Colortype=...,
fg:Colortype=...,
wraplength:Numbertype=0,
bd:Numbertype=0,
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='center'
)->dict:'''ファイルもしくはフォルダを選択し,選択されたパスを取得するダイアログを発生させるボタンを生成する。

 :param text: Savebtnウィジェットのボタンに表示させる文字を指定する。
 :type text: str
 :param title: フォルダを選択するダイアログのタイトルを指定する。
 :type title: str
 :param filetypes: 保存できるファイル形式の選択肢を指定する。
 :type filetypes: list[tuple[str,str]]
 :param initialdir: ダイアログを開く初期ディレクトリを指定する。
 :type initialdir: str
 :param initialfile: ファイル名フィールドの初期値を指定する。
 :type initialfile: str
 :param defaultextension: 拡張子が設定されていない時のデフォルトを指定する。
 :type defaultextension: str'''
 @staticmethod
 def Colorbtn(
color:Colortype='#ffffff',
text:str='select color',
title:str='select color',
key:str=...,
bg:Colortype=...,
fg:Colortype=...,
wraplength:Numbertype=0,
bd:Numbertype=0,
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='center'
)->dict:'''色を選択し,選択された色を取得するダイアログを発生させるボタンを生成する。

 :param color: ダイアログで選択される色の初期値を選択する。
 :type color: Colortype
 :param text: Colorbtnウィジェットのボタンに表示させる文字を指定する。
 :type text: str
 :param title: 色を選択するダイアログのタイトルを指定する。
 :type title: str'''
 @staticmethod
 def Calendars(
date:datetime=...,
selectmode:Literal['none','day']='day',
headersbg:Colortype='gray70',
headersfg:Colortype='black',
othermonthbg:Colortype='gray93',
othermonthfg:Colortype='gray45',
weekendbg:Colortype='gray80',
weekendfg:Colortype='gray30',
locale:str='ja_JP',
firstweekday:Literal['monday','sunday']='sunday',
format:str|Literal['format0','format1','format2','format3']='format0',
showweek:bool=False,
key:str=...,
justify:Literal['left','center','right']='left',
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat',
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='w',
bd:Numbertype=2,
weekenddays:TupleInt2|ListInt2=None,
state:Literal['normal','disabled']='normal',
textvariable:StringVar|None=None,
maxdate:datetime|None=None,
mindate:datetime|None=None,
showotherdays:bool=True
)->dict:'''カレンダーを生成する。

 :param date: Calendarsウィジェットに表示する日付を指定する。
 :type date: datetime
 :param selectmode: ユーザーがマウスクリックで選択した日を変更できるかどうかを指定する。
 :type selectmode: Literal['none','day']
 :param headersbg: 曜日列の背景色を指定する。
 :type headersbg: Colortype
 :param headersfg: 曜日列の文字色を指定する。
 :type headersfg: Colortype
 :param othermonthbg: Calendarsウィジェットで表示しいる月の前月と翌月に属する通常の曜日の背景色を指定する。
 :type othermonthbg: Colortype
 :param othermonthfg: Calendarsウィジェットで表示しいる月の前月と翌月に属する通常の曜日の文字色を指定する。
 :type othermonthfg: Colortype
 :param weekendbg: 週末の背景色を指定する。
 :type weekendbg: Colortype
 :param weekendfg: 週末の文字色を指定する。
 :type weekendfg: Colortype
 :param locale: ロケールを指定する。
 :type locale: str
 :param firstweekday: 週の最初の曜日を指定する。
 :type firstweekday: Literal['monday','sunday']
 :param format: 日付フォーマットを指定する。
 :type format: str|Literal['format0','format1','format2','format3']
 :param showweek: 週番号を表示するか指定する。
 :type showweek: bool
 :param weekenddays: 週末として表示する曜日を指定する。
 :type weekenddays: TupleInt2|ListInt2
 :param maxdate: 最大許容日付を指定する。
 :type maxdate: datetime|None
 :param mindate: 最小許容日付を指定する。
 :type mindate: datetime|None
 :param showotherdays: 前月の日付と翌月以降の日付を表示するか指定する。
 :type showotherdays: bool'''
 @staticmethod
 def Tab(
tabs:list[list[str,list[list]]]=[],
key:str=...,
bg:Colortype=...,
fg:Colortype=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False
)->dict:'''タブを生成する。

 :param tabs: Tabウィジェットに表示させるウィジェットを指定する。配列の最初の要素にタブ名を,次の要素にTabウィジェットに表示させる`layout`を指定する。
 :type tabs: list[list[str,list[list]]]'''
 @staticmethod
 def TProgressbar(
value:Numbertype=0,
max:Numbertype=100,
length:Numbertype=200,
mode:Literal['determinate','indeterminate']='determinate',
orient:Literal['horizontal','vertical']='horizontal',
key:str=...
)->dict:'''プログレスバーを生成する。

 :param length: TProgressbarウィジェットの長さを指定する。
 :type length: Numbertype
 :param orient: TProgressbarウィジェットの向きを指定する。
 :type orient: Literal['horizontal','vertical']
 :param mode: 決定的モード(determinate)か非決定的モード(indeterminate)かを指定する。
 :type mode: Literal['determinate','indeterminate']
 :param max: TProgressbarウィジェットの数値の最大値を指定する。
 :type max: Numbertype
 :param value: TProgressbarウィジェットの読み込み時の初期値を指定する。
 :type value: Numbertype'''
 @staticmethod
 def Barcode(
data:str=...,
data_type:Literal['EAN-8','EAN-13','JAN','Code39','Code128']='Code128',
name:str='No Barcode image',
key:str=...
)->dict:'''バーコードを生成する。

 :param data: バーコードで表示させる値を指定する。
 :type data: str
 :param data_type: バーコードの形式を指定する。
 :type data_type: Literal['EAN-8','EAN-13','JAN','Code39','Code128']
 :param name: 何らかの例外が起こりバーコードが表示されなかった場合に表示する文字を指定する。
 :type name: str'''
 @staticmethod
 def QRcode(
text:str=...,
name:str='No Qrcode image',
key:str=...
)->dict:'''QRコードを生成する。

 :param text: QRコードを読みっとった際に表示させる値を指定する。
 :type text: str
 :param name: QRコードを生成する際,何らかの例外が起こった場合に表示する文字を指定する。
 :type name: str'''
 @staticmethod
 def LineGraph(
x:n_array=...,
y:n_array=...,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
linewidth:Numbertype=2,
alpha:Numbertype=1,
markersize:Numbertype=10,
marker:Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']=None,
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict:'''折線グラフを生成する。

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
 @staticmethod
 def BarGraph(
x:o_array=...,
y:n_array=...,
logs:bool=False,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
linewidth:Numbertype=2,
width:Numbertype=1,
alpha:Numbertype=1,
align:Literal['center','edge']='center',
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict:'''x軸向きにバーを設置した棒グラフを生成する。

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
 :param linewidth: 折線グラフの線の幅を指定する。
 :type linewidth: Numbertype
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
 @staticmethod
 def BarhGraph(
x:o_array=...,
y:n_array=...,
logs:bool=False,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
linewidth:Numbertype=2,
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
alpha:Numbertype=1,
height:Numbertype=1,
align:Literal['center','edge']='center',
key:str=...
)->dict:'''y軸向きにバーを設置した棒グラフを生成する。

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
 :param linewidth: 折線グラフの線の幅を指定する。
 :type linewidth: Numbertype
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
 @staticmethod
 def Pie(
data:o_array=...,
label:labeltype=...,
startangle:Numbertype=0,
startangletype:bool=True,
shadow:bool=False,
counterclock:bool=False,
labeldistance:Numbertype=1.1,
explode:list[int,float,Number]|tuple[int,float,Number]|int|float|Number=...,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
color:Colortype|list[Colortype]|tuple[Colortype]=...,
title:str=...,
dpi:Numbertype=100,
key:str=...
)->dict:'''円グラフを生成する。

 :param labeldistance: 中心からラベルの距離を指定する。
 :type labeldistance: Numbertype
 :param explode: 中心から各セグメントの離す距離を指定する。
 :type explode: list[int,float,Number]|tuple[int,float,Number]|int|float|Number
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 円グラフが順番に表示する色を指定する。
 :type color: Colortype|list[Colortype]|tuple[Colortype]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param data: `data`のデータを指定する。
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
 @staticmethod
 def Boxplot(
data:n_array=...,
label:labeltype=...,
legend:bool=True,
fill:bool=False,
notch:bool=False,
showfliers:bool=True,
orientation:Literal['horizontal','vertical']='vertical',
width:Numbertype=0.15,
whis:float|tuple[float,float]=1.5,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
color:Colortype|list[Colortype]|tuple[Colortype]=...,
title:str=...,
dpi:Numbertype=100,
graph_grid:Colortype='#b7b7b7',
xlabel:str|None=...,
ylabel:str|None=...,
key:str=...
)->dict:'''箱ひげ図を生成する。

 :param data: `data`のデータを指定する。
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
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: Colortype
 :param bg: グラフ内の背景色を指定する。
 :type bg: Colortype
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param width: 箱の幅を指定する。
 :type width: Numbertype
 :param whis: ひげの開始位置を指定する。
 :type whis: float|tuple[float,float]
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: Colortype'''
 @staticmethod
 def Waterfall(
x:o_array=...,
y:o_array=...,
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
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
alpha:Numbertype=1,
key:str=...
)->dict:'''x軸向きにバーを設置された滝グラフを生成する。

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
 @staticmethod
 def Waterfallh(
x:o_array=...,
y:o_array=...,
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
ucolor:Colortype='#156082',
dcolor:Colortype='#e97132',
height:Numbertype=1,
alpha:Numbertype=1,
key:str=...
)->dict:'''y軸向きにバーを設置された滝グラフを生成する。

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
 @staticmethod
 def Scatter(
x:n_array=...,
y:n_array=...,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
marker:Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']='o',
markersize:Numbertype=10,
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict:'''散布図を生成する。

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
 @staticmethod
 def DScatter(
x:n_array=...,
y:n_array=...,
z:n_array=...,
xlabel:str=...,
ylabel:str=...,
zlabel:str=...,
marker:Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']='o',
markersize:Numbertype=10,
alpha:Numbertype=1,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
color:Colortype|list[Colortype]|tuple[Colortype]=...,
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
azim:Numbertype=45,
key:str=...
)->dict:'''3Dの散布図を生成する。

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
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param znumticks: z軸の目盛りの数を指定する。
 :type znumticks: Numbertype|None
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
 @staticmethod
 def Stem(
x:NpArraytype=...,
y:NpArraytype=...,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
orientation:Literal['horizontal','vertical']='vertical',
bottom:Numbertype=0,
size:TupleNumbertype2=(500,400),
fg:Colortype='#000000',
bg:Colortype='#ffffff',
marker:Literal['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']=...,
line:Literal['-','--','-.','-.']=...,
color:Literal['r','g','b','c','m','y','k','w']|list[Literal['r','g','b','c','m','y','k','w']]|tuple[Literal['r','g','b','c','m','y','k','w']]=...,
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict:'''幹図を生成する。

 :param x: `x`のデータを指定する。
 :type x: NpArraytype
 :param y: `y`のデータを指定する。
 :type y: NpArraytype
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
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
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
 @staticmethod
 def Step(
data:n_array=...,
range:int|float|TupleNumbertype2=...,
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
y_verwrit:Literal['horizontal','vertical']='vertical',
label:labeltype=...,
xlabel:str|None=...,
ylabel:str|None=...,
key:str=...
)->dict:'''階段グラフを生成する。

 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param data: `data`のデータを指定する。
 :type data: n_array
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
 @staticmethod
 def Hist(
data:o_array=...,
label:labeltype=...,
width:Numbertype=1,
min:Numbertype=...,
max:Numbertype=...,
decimalpoint:Numbertype=0,
orientation:Literal['horizontal','vertical']='vertical',
bottom:Numbertype=0,
bins:int|list|range|tuple|ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt']=10,
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
y_verwrit:Literal['horizontal','vertical']='vertical',
xlabel:str|None=...,
ylabel:str|None=...,
key:str=...
)->dict:'''ヒストグラムを生成する。

 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param data: `data`のデータを指定する。
 :type data: o_array
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
 :param bins: `bins`を指定する。
 :type bins: int|list|range|tuple|np.ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt']
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
 @staticmethod
 def Stack(
x:n_array=None,
y:n_array=None,
xlabel:labeltype=...,
ylabel:labeltype=...,
label:labeltype=...,
hatch:Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--',r'-\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||']=None,
baseline:Literal['zero','sym','wiggle','weighted_wiggle']='zero',
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict:'''積み上げエリアチャートを生成する。

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
 :param hatch: 塗りつぶし領域内の模様を指定する。
 :type hatch: Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--',r'-\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||']
 :param baseline: 基準値の算出方法を指定する。
 :type baseline: Literal['zero','sym','wiggle','weighted_wiggle']
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param align: x軸の棒グラフバーの配置を指定する。
 :type align: Literal['center','edge']
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
 @staticmethod
 def Bubble(
x:n_array=...,
y:n_array=...,
data:n_array=...,
bubblesize:Numbertype=1,
marker:Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']='o',
markersize:Numbertype=10,
linewidth:Numbertype=2,
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict:'''バブルグラフを生成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param data: バブルグラフのバブルの大きさを指定する。
 :type data: n_array
 :param bubblesize: バブルの大きさの倍率を指定する。
 :type bubblesize: Numbertype
 :param marker: バブルグラフのマーカーを指定する。
 :type marker: Literal['1','2','3','4','8','circle','d','diamond','D','h','hline','H','none','None',None,'o','octagon','p','pentagon','pixel','plus','point','P','s','square','star','triangle','v','vline','x','X','hexagon1','hexagon2',' ','*','+',',','.','<','>',']','^','_','plus-filled','thin_diamond','tri_down','tri_left','tri_right','tri_up','triangle_down','triangle_left','triangle_right','triangle_up','|']
 :param markersize: 散布図のマーカーの大きさを指定する。
 :type markersize: Numbertype
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
 @staticmethod
 def Linefill(
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
):'''2つの水平曲線の間の領域を埋めるグラフを作成する。

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
 @staticmethod
 def Ecdf(
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
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
):'''経験的累積分布関数を作成する。

 :param data: 入力データを指定する。
 :type data: n_array
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
 @classmethod
 def Popup(
cls,
title:str='Information',
message:str='Information message',
icon:Literal['info','warning','error','question']='info'
)->str:'''指定されたタイトルとメッセージを持つ情報メッセージボックスを作成して表示します。

 :param title: 情報メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param icon: 情報メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :param message: 情報メッセージボックスに表示させるメッセージを指定する。
 :type message: str'''
 @classmethod
 def Popupwarning(
cls,
title:str='Warning',
message:str='Warning message',
icon:Literal['info','warning','error','question']='warning'
)->str:'''指定されたタイトルとメッセージを含む警告メッセージボックスを作成して表示します。

 :param title: 警告メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: 警告メッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: 警告メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: str'''
 @classmethod
 def Popupwarningyesno(
cls,
title:str='Warning',
message:str='Warning message',
icon:Literal['info','warning','error','question']='warning'
)->Union[str]:'''指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つ警告メッセージボックスを作成して表示します。

 :param title: 警告メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: 警告メッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: 警告メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: Union[str] ('yes','no')'''
 @classmethod
 def Popuperror(
cls,
title:str='Error',
message:str='Error message',
icon:Literal['info','warning','error','question']='error'
)->str:'''指定されたタイトルとメッセージを持つエラーメッセージボックスを作成して表示します。

 :param title: エラーメッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: エラーメッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: エラーメッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: str'''
 @classmethod
 def Popuperroryesno(
cls,
title:str='Error',
message:str='Error message',
icon:Literal['info','warning','error','question']='error'
)->Union[str]:'''指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つエラーメッセージボックスを作成して表示します。

 :param title: エラーメッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: エラーメッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: エラーメッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: Union[str] ('yes','no')'''
 @classmethod
 def Popupquestion(
cls,
title:str='Question',
message:str='Question message',
icon:Literal['info','warning','error','question']='question'
)->Union[str]:'''「はい(Yes)」か「いいえ(No)」を選択させるダイアログを表示させる。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: Union[str] ('yes','no')'''
 @classmethod
 def Popupokcancel(
cls,
title:str='Question',
message:str='Question message',
icon:Literal['info','warning','error','question']='question'
)->bool:'''「OK」か「キャンセル」を選択させるダイアログを表示させる。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: bool'''
 @classmethod
 def Popupyesno(
cls,
title:str='Question',
message:str='Question message',
icon:Literal['info','warning','error','question']='question'
)->bool:'''「はい(Yes)」か「いいえ(No)」を選択させるダイアログを表示させる。「はい」の場合はTrueを,「いいえ」の場合はFalseを返す。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: bool'''
 @classmethod
 def Popupyesnocancel(
cls,
title:str='Question',
message:str='Question message',
icon:Literal['info','warning','error','question']='question'
)->Union[bool,None]:'''「はい(Yes)」「いいえ(No)」「キャンセル(Cancel)」を選択させるダイアログを表示させる。「はい」の場合はTrueを,「いいえ」の場合はFalseを返す,「キャンセル(Cancel)」もしくはダイアログを閉じた場合Noneを返す。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: Union[bool,None]'''
 @classmethod
 def Popuptry(
cls,
title:str='Question',
message:str='Question message',
icon:Literal['info','warning','error','question']='question'
)->bool:'''操作を再試行するかどうかを尋ねる「再試行」ボタンと「キャンセル」ボタンが設置されたダイアログを表示させる。回答が「再試行」の場合はTrueを,「キャンセル」の場合はFalseを返します。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: bool'''
class Logger:
 def __init__(
self,
name:str='log',
level:int=10,
format:str|list='message',
sep:str='|',
logfile:bool=False,
lclear:Literal['none','once','do',None,'',' ']='none'
)->Logger:'''ログを作成する。

 :param name: ログ名を指定する。
 :type name: str
 :param level: ログレベルを指定する。
 :type level: int
 :param format: ログで表示するテキストを指定する。
 :type format: str|list
 :param sep: formatで複数項目を指定した際の区切り文字を指定する。sepを文字型以外で指定した場合'|'を返す。
 :type sep: str
 :param logfile: ログファイルにログを保存するか指定する。
 :type logfile: bool
 :param lclear: ログファイルに書き込まれたログの削除の仕方を指定する。
 :type lclear: Literal['none','once','do',None,'',' ']'''
 def get_logger(self)->logging.Logger:'''logging.Loggerを返す。'''
 @classmethod
 def clear(cls)->NoReturn:'''コンソールを消す。'''
class GraphOption:
 @staticmethod
 def marker()->list:...
 @staticmethod
 def hatch()->list:...
 @staticmethod
 def solid()->list:...