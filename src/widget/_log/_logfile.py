from logging import FileHandler
from os.path import abspath, dirname, join, normpath

from ._clearsave import clearsave
from ._data import log_clear


class LogFile:
 clearj=False
 log_file_pas=normpath(join(dirname(abspath(__file__)),'data/log.log'))
 def __init__(self,logger,level,format):
  self.c=str(clearsave())
  self._clear_serch()
  file_handler=FileHandler(self.log_file_pas,encoding='utf-8')
  file_handler.setLevel(level)
  file_handler.setFormatter(format)
  logger.addHandler(file_handler)
 def _clear_serch(self):
  for item,key in log_clear.items():
   if self.c in key:
    if item=='do':
     self._log_file_clear()
     break
    elif item=='once' and LogFile.clearj==False:
     self._log_file_clear()
     LogFile.clearj=True
     break
 def _log_file_clear(self):
  with open(self.log_file_pas,'r+')as f:f.truncate(0)