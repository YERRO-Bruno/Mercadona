import http.server
import socketserver

# Spécifiez le port sur lequel vous souhaitez exécuter le serveur
port = 8080
directory='static'
# Lancer le serveur à partir du répertoire racine où se trouve le répertoire "static"
with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()