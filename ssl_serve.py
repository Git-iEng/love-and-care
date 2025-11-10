# import os
# import ssl
# from django.core.wsgi import get_wsgi_application
# from wsgiref.simple_server import make_server, WSGIRequestHandler

# # Set Django settings module
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lovecare.settings")

# print("SSL module is loaded from:", ssl.__file__)
# print(dir(ssl))

# # Update this to the actual paths
# cert_file = r"C:/Users/Administrator/Desktop/loveandcarefoundation.org/certificate.crt"
# key_file = r"C:/Users/Administrator/Desktop/loveandcarefoundation.org/private.key"

# application = get_wsgi_application()

# httpd = make_server(
#     '0.0.0.0', 9443, application,
#     handler_class=WSGIRequestHandler
# )

# httpd.socket = ssl.wrap_socket(
#     httpd.socket,
#     certfile=cert_file,
#     keyfile=key_file,
#     server_side=True
# )

# print("Serving on https://0.0.0.0:9443/")
# httpd.serve_forever()

import os
import ssl
from wsgiref.simple_server import make_server, WSGIRequestHandler, WSGIServer
from django.core.wsgi import get_wsgi_application

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lovecare.settings")

# Get WSGI app
application = get_wsgi_application()

# Define certificate file paths (replace with yours)
cert_file = r"C:/Users/Administrator/Desktop/loveandcarefoundation.org/certificate.crt"
key_file = r"C:/Users/Administrator/Desktop/loveandcarefoundation.org/private.key"

# Set up SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=cert_file, keyfile=key_file)

# Create custom HTTPS server using SSLContext
class SecureWSGIServer(WSGIServer):
    def get_request(self):
        socket, addr = super().get_request()
        return context.wrap_socket(socket, server_side=True), addr

httpd = make_server('0.0.0.0', 9443, application, server_class=SecureWSGIServer, handler_class=WSGIRequestHandler)

print("✅ HTTPS server is running at: https://loveandcarefoundation.org:9443/")
httpd.serve_forever()
