import http.client
import json
import threading
import unittest

from tools.preview import build_server


class PreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = build_server(0)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def request(self, method, path, body=None):
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=3)
        try:
            connection.request(method, path, body=body)
            response = connection.getresponse()
            return response.status, dict(response.getheaders()), response.read()
        finally:
            connection.close()

    def test_preview_is_explicit_and_has_no_account_form(self):
        status, headers, body = self.request("GET", "/")
        self.assertEqual(status, 200)
        self.assertIn(b'data-stage="installation-preview"', body)
        self.assertIn(b"Gameplay not connected", body)
        self.assertNotIn(b"<form", body)
        self.assertNotIn(b"<script", body)
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertIn("form-action 'none'", headers["Content-Security-Policy"])
        self.assertEqual(headers["X-Frame-Options"], "DENY")

    def test_health_cannot_be_mistaken_for_game_admission(self):
        status, _, body = self.request("GET", "/health")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)["game_connected"], False)
        self.assertEqual(json.loads(body)["mode"], "installation-preview")

    def test_no_directory_files_or_private_routes_are_served(self):
        for path in ("/README.md", "/PUBLIC_FILES.txt", "/.env", "/../LICENSE", "/%2e%2e/LICENSE", "/api/login", "/ws", "/play/"):
            with self.subTest(path=path):
                self.assertEqual(self.request("GET", path)[0], 404)

    def test_submissions_are_not_accepted(self):
        for method in ("POST", "PUT", "PATCH", "DELETE"):
            with self.subTest(method=method):
                status, _, body = self.request(method, "/", b"synthetic-input")
                self.assertEqual(status, 405)
                self.assertIn(b"no submissions", body)

    def test_head_and_query_have_no_extra_capability(self):
        self.assertEqual(self.request("HEAD", "/")[2], b"")
        status, _, body = self.request("GET", "/health?approved=true")
        self.assertEqual(status, 200)
        self.assertFalse(json.loads(body)["game_connected"])

    def test_listener_is_loopback(self):
        self.assertEqual(self.server.server_address[0], "127.0.0.1")


if __name__ == "__main__":
    unittest.main()
