from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 9000


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/health":
            self._send(200, {"status": "ok"})
        elif self.path == "/":
            self._send(200, {"message": "pookie backend"})
        else:
            self._send(404, {"error": "not found"})


if __name__ == "__main__":
    print(f"pookie running on port {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
