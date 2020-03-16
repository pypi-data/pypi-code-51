import unittest
from unittest.mock import patch, mock_open

from restit import RestitTestApp, RestitApp, Resource, Response, Request, request_mapping
from restit.static_file_response import StaticFileResponse


@request_mapping("/static-response")
class MyResource(Resource):
    def get(self, request: Request, **path_params) -> Response:
        file_path = request.get_request_body_as_type(dict)["file_path"]
        return StaticFileResponse(file_path)


class StaticFileResourceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.rest_test_app = RestitTestApp(RestitApp(
            resources=[MyResource()]
        ))

    def test_text_file(self):
        m = mock_open(read_data=b"Huhu from file")
        with patch("restit.static_file_response.open", m):
            response = self.rest_test_app.get("/static-response?", json={"file_path": "/some/file/path.txt"})
            self.assertEqual(200, response.get_status_code())
            self.assertEqual("text/plain", response.get_headers()["Content-Type"])
            self.assertEqual("Huhu from file", response.text)

    def test_html_file(self):
        m = mock_open(read_data=b"<title>dummy html</title>")
        with patch("restit.static_file_response.open", m):
            response = self.rest_test_app.get("/static-response?", json={"file_path": "/some/file/path.html"})
            self.assertEqual(200, response.get_status_code())
            self.assertEqual("text/html", response.get_headers()["Content-Type"])
            self.assertEqual("<title>dummy html</title>", response.text)
