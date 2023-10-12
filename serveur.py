#!/usr/bin/env python
# coding: utf-8


from http.server import BaseHTTPRequestHandler, HTTPServer
import CGIHTTPServer

import cgitb; cgitb.enable() # enable CGI error reporting

PORT = 8080
server_address = ('', PORT)

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
handler.cgi_directories = ['cgi-bin']


httpd = server(server_address, handler)

httpd.serve_forever()