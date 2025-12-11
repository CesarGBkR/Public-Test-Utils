import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "."
class LoggingRequestHandler(http.server.SimpleHTTPRequestHandler):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, directory=DIRECTORY, **kwargs)
  def do_GET(self):
    print(f"[MI LOG] IP: {self.client_address[0]}, Petición: \"{self.requestline}\"")
   super().do_GET()
   
with socketserver.TCPServer(("", PORT), LoggingRequestHandler) as httpd:
  server_dir = os.path.abspath(DIRECTORY)
  print(f"✅ Servidor iniciado en http://localhost:{PORT}")
  print(f"📂 Sirviendo archivos desde el directorio: {server_dir}")
  print("------------------------------------------------------")
  print("Presiona Ctrl+C para detener el servidor.")

  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    print("\n🚫 Servidor detenido por el usuario.")
    httpd.shutdown()
