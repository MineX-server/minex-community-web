#!/usr/bin/env python3
"""Loopback-only installation preview. No login, proxying, or game integration."""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
HEALTH = b'{"status":"ok","mode":"installation-preview","game_connected":false}\n'


class PreviewHandler(BaseHTTPRequestHandler):
    server_version = "MineXPreview"
    sys_version = ""

    def send_content(self, status, content_type, body):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path in ("/", "/index.html"):
            self.send_content(200, "text/html; charset=utf-8", (ROOT / "preview/index.html").read_bytes())
        elif path == "/health":
            self.send_content(200, "application/json; charset=utf-8", HEALTH)
        else:
            self.send_content(404, "text/plain; charset=utf-8", b"Not found\n")

    do_HEAD = do_GET

    def do_POST(self):
        self.close_connection = True
        self.send_content(405, "text/plain; charset=utf-8", b"This preview accepts no submissions.\n")

    do_PUT = do_POST
    do_PATCH = do_POST
    do_DELETE = do_POST

    def log_message(self, *args):
        # No request URLs, addresses, or submitted content are written to logs.
        pass


def build_server(port=8787):
    return ThreadingHTTPServer(("127.0.0.1", port), PreviewHandler)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8787)
    args = parser.parse_args()
    if not 0 <= args.port <= 65535:
        parser.error("port must be between 0 and 65535")
    server = build_server(args.port)
    print(f"Installation preview: http://127.0.0.1:{server.server_port}", flush=True)
    print("No game or account connection. Press Ctrl+C to stop.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
