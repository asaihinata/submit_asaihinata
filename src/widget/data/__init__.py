from json import load
from os.path import dirname, join

__all__=['getjson']
def getjson(file:str)->dict|None:
 '''指定されたファイル名のjsonファイルのデータを取得しそれを返す。

 :param file: ファイル名
 :type file: str
 :rtype: dict|None'''
 try:
  with open(join(dirname(__file__),f'{file}.json'),'r',encoding='utf-8')as f:return load(f)
 except:return None