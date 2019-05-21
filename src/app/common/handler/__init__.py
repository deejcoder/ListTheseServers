# singleton

from .pinghandler import PingHandler
from .serverhandler import ServerHandler
from .userhandler import UserHandler
from .ddnshandler import DDnsHandler

# singleton alternative
_initialized = False
if not _initialized:
    pingHandler = PingHandler()
    serverHandler = ServerHandler()
    userHandler = UserHandler()
    ddnsHandler = DDnsHandler()
    _initialized = True
