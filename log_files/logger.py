import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

log_format = '%(asctime)s | (%(levelname)s)->| %(message)s |'

def handler(filename, level):
    loghandler = logging.FileHandler(filename)
    loghandler.setLevel(level)
    loghandler.setFormatter(logging.Formatter(log_format))
    return loghandler

log.addHandler(handler('app.logfile', logging.INFO))
log.addHandler(handler('app.errorfile', logging.ERROR))
# log.error('===============start of log stream')

line = "————————"
arrow = "————————>"
notify= "————————|< !!! >"
success = "————————|< V >"
failure = "————————|< X >"
