class CCError(Exception):
   pass

def error(msg):
   raise CCError(msg)