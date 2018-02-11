from inotify_simple import INotify, flags
import importlib
import os
import sys

from libs import g

print('estou no modulo - root')
DYN_LIB_DIR='runtime_lib'

# Define a function for the thread
def monitor(name, delay):
   print('estou no modulo - function monitor')
   inotify = INotify()
   watch_flags = flags.CREATE | flags.DELETE | flags.DELETE_SELF
   wd = inotify.add_watch(DYN_LIB_DIR+'/', watch_flags)
   while True:
      for event in inotify.read():
         if event.name.endswith('.py'):
            module_name = DYN_LIB_DIR + '.' + os.path.splitext(event.name)[0]
            for flag in flags.from_mask(event.mask):
               print('{}, Flag name: {}, Module Name: {}  '.format(event, flag.name, module_name))
            i = importlib.import_module(module_name)
            c = { x:y for x,y in i.__dict__.items() if not x.startswith('__') }
            g.roles.update(c)
