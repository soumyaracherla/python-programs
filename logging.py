import logging
from logging import handlers
from logging import *

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
print(logging.__file__)
print(threading.__file__)


name = 'DB- logic'
logging.error('%s raised an error', name)
logging.error(f'{name} raised an error')

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)


try:
  c = a / b
except Exception as e:
  logging.exception("div by zero exception occured")


"""
import dis

def foo1(param):
    assert param, "fail"

def foo2(param):
    if not param:
        raise AssertionError("fail")

print(dis.dis(foo1))
print(dis.dis(foo2))
"""
