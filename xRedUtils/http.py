"""

"""

import http.server
import sys, urllib, http
sys.dont_write_bytecode = True

def start_web_server() -> http.server.HTTPServer:
    with http.server.HTTPServer() as server:
        ...

def kill_web_server() -> bool:
    return 