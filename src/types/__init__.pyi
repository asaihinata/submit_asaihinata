'''基本的な型ヒント'''
from os import PathLike
from typing import *

import numpy as np
from numpy import ndarray
from numpy.typing import NDArray

type StrPathtype=str|PathLike[str]
'''StrPathtype型

フォルダやファイルのパス名の型ヒント'''
type Colortype=str
'''Colortype型

色名の型ヒント'''
type Linktype=str
'''Linktype型

URLのリンクの型ヒント'''
type fontname=str
'''fontname型

フォント名の型ヒント'''
type Numbertype=int|float
'''Numbertype型

int型,float型の型ヒント'''
type Arraytype=list|tuple
'''Arraytype型

list型,tuple型の型ヒント'''
type nArraytype=list|tuple|None
'''Arraytype型

list型,tuple型,Noneの型ヒント'''
type NpArraytype=ndarray|list|tuple
'''NpArraytype型

ndarray型,list型,tuple型の型ヒント'''
type nNpArraytype=ndarray|list|tuple|None
'''nNpArraytype型

ndarray型,list型,tuple型,Noneの型ヒント'''
type TupleNumbertype2=tuple[Numbertype,Numbertype]
'''TupleNumbertype2型

tuple(Numbertype,Numbertype)の型ヒント'''
type TupleInt2=tuple[int,int]
'''TupleInt2型

tuple(int,int)の型ヒント'''
type TupleFloat2=tuple[float,float]
'''TupleFloat2型

tuple(float,float)の型ヒント'''
type ListNumbertype2=list[Numbertype,Numbertype]
'''ListNumbertype2型

list(Numbertype,Numbertype)の型ヒント'''
type ListInt2=list[int,int]
'''ListInt2型

tuple(int,int)の型ヒント'''
type ListFloat2=list[float,float]
'''ListFloat2型

list(float,float)の型ヒント'''
def _f()->None:pass
FunctionType=type(_f)
type labeltype=str|list|tuple|None
'''labeltype型

グラフのラベルに関する型ヒント(str|list|tuple|None)'''
type o_array=list[int,float,str]|tuple[int,float,str]|NDArray[np.str_]|NDArray[np.int_]|NDArray[np.floating]
'''o_array型

グラフで`x`,`y`,`z`,`data`を指定するさい一次元配列のみを指定するさいの型ヒント'''
type n_array=list|tuple|NDArray
'''n_array型

グラフで`x`,`y`,`z`,`data`を指定するさい一次元配列を含む多次元配列を指定するさいの型ヒント'''