# coding=utf-8
from .base_settings import *

try:
    from .local_settings import *
except ImportError:
    pass

print(LOCAL)

if not LOCAL:
    try:
        from .remote_settings import *
    except ImportError:
        pass
