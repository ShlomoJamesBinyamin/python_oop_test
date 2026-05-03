import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

format = '%(asctime)s | (%(levelname)s)->| %(message)s |'

def handler(filename, level):
    handler = logging.FileHandler(filename)
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(format))
    return handler

log.addHandler(handler('app.logfile', logging.INFO))
log.addHandler(handler('app.errorfile', logging.ERROR))
# log.error('===============start of log stream')

line = "————————"
arrow = "————————>"
notify= "————————|< !!! >"
success = "————————|< V >"
failure = "————————|< X >"
