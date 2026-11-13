import http.server
import socketserver
import os
import sys
import mimetypes

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Prefer dist/ if available (from vite build), otherwise serve root
DIST_DIR = os.path.join(BASE_DIR, "dist")
DIRECTORY = DIST_DIR if os.path.exists(DIST_DIR) else BASE_DIR

mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("image/jpeg", ".jpg")
mimetypes.add_type("image/jpeg", ".jpeg")
mimetypes.add_type("image/png", ".png")
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("image/x-icon", ".ico")

class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        url_path = self.path.split('?')[0].split('#')[0]
        local_path = os.path.join(DIRECTORY, url_path.lstrip('/'))

        # If static file exists, serve it
        if os.path.exists(local_path) and not os.path.isdir(local_path):
            return super().do_GET()

        # If not found in dist, check if it's in public or root (e.g. textures)
        fallback_path = os.path.join(BASE_DIR, "public", url_path.lstrip('/'))
        if os.path.exists(fallback_path) and not os.path.isdir(fallback_path):
            self.directory = os.path.join(BASE_DIR, "public")
            res = super().do_GET()
            self.directory = DIRECTORY
            return res

        # Fallback to root textures if requested
        root_tex_path = os.path.join(BASE_DIR, url_path.lstrip('/'))
        if os.path.exists(root_tex_path) and not os.path.isdir(root_tex_path):
            self.directory = BASE_DIR
            res = super().do_GET()
            self.directory = DIRECTORY
            return res

        # Check for file extension
        _, ext = os.path.splitext(url_path)
        if ext and ext not in ['.html', '.htm']:
            return super().do_GET()

        # SPA fallback: Serve index.html
        index_file = os.path.join(DIRECTORY, "index.html")
        if os.path.exists(index_file):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            with open(index_file, "rb") as f:
                content = f.read()
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        return super().do_GET()

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    # Allow socket reuse
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), SPAHandler) as httpd:
        print(f"🚀 Beyond Andromeda running at http://localhost:{port}", flush=True)
        print(f"🌍 Serving directory: {DIRECTORY}", flush=True)
        print(f"📍 Direct explore: http://localhost:{port}/explore/earth?lat=27.9974&lon=77.9769", flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer terminated.", flush=True)
