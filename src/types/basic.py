from os import PathLike

import numpy as np
from numpy import ndarray
from numpy.typing import NDArray

# str type
type StrPathtype=str|PathLike[str]
StrPathtype=(str,PathLike)
type Colortype=str
Colortype=str
type Linktype=str
Linktype=str
type fontname=str
fontname=str
# number type
type Numbertype=int|float
Numbertype=(int,float)
# list like type
type Arraytype=list|tuple
Arraytype=(list,tuple)
type nArraytype=list|tuple|None
nArraytype=(list,tuple,None)
type NpArraytype=ndarray|list|tuple
NpArraytype=(ndarray,list,tuple)
type nNpArraytype=ndarray|list|tuple|None
nNpArraytype=(ndarray,list,tuple,None)
# list like and number type
type TupleNumbertype2=tuple[Numbertype,Numbertype]
type TupleInt2=tuple[int,int]
type TupleFloat2=tuple[float,float]
type ListNumbertype2=list[Numbertype,Numbertype]
type ListInt2=list[int,int]
type ListFloat2=list[float,float]
# function type
def _f():pass
FunctionType=type(_f)
# graph type
type labeltype=str|list|tuple|None
type o_array=list[int,float,str]|tuple[int,float,str]|NDArray[np.str_]|NDArray[np.int_]|NDArray[np.floating]
type n_array=list|tuple|NDArray