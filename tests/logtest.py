from _import import *

logger=Logger(name=__name__,format=['lineno','message','asctime'],logfile=True,lclear='once').get_logger()
logger.debug('デバッグログ')
logger.info('情報ログ')
logger.warning('警告ログ')
logger.error('エラーログ')
logger.critical('重大エラー')