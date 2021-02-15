class CCError(Exception):
   pass

def error(msg):
   raise Exception(msg)