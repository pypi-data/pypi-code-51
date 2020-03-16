"""Test validation exceptions."""

from dataclasses import dataclass
from pyramid.interfaces import IRouteRequest
from pyramid.interfaces import IView
from pyramid.interfaces import IViewClassifier
from pyramid.request import Request
from pyramid.response import Response
from pyramid.router import Router
from pyramid.testing import DummyRequest
from pyramid.testing import setUp
from pyramid.testing import tearDown
from unittest import TestCase
from zope.interface import Interface

import json
import tempfile
import typing as t

View = t.Callable[[t.Any, Request], Response]


@dataclass
class DummyRoute:
    name: str
    pattern: str


class DummyStartResponse(object):
    def __call__(self, status, headerlist) -> None:
        """WSGI start_response protocol."""
        self.status = status
        self.headerlist = headerlist


class TestRequestValidation(TestCase):
    def setUp(self) -> None:
        """unittest.TestCase setUp for each test method.

        Setup a minimal pyramid configuration.
        """
        self.config = setUp()

        self.config.include("pyramid_openapi3")

        with tempfile.NamedTemporaryFile() as document:
            document.write(
                b'openapi: "3.0.0"\n'
                b"info:\n"
                b'  version: "1.0.0"\n'
                b"  title: Foo API\n"
                b"paths:\n"
                b"  /foo:\n"
                b"    get:\n"
                b"      parameters:\n"
                b"        - name: bar\n"
                b"          in: query\n"
                b"          required: true\n"
                b"          schema:\n"
                b"            type: integer\n"
                b"      responses:\n"
                b"        200:\n"
                b"          description: A foo\n"
                b"        400:\n"
                b"          description: Bad Request\n"
            )
            document.seek(0)

            self.config.pyramid_openapi3_spec(
                document.name, route="/foo.yaml", route_name="foo_api_spec"
            )

    def tearDown(self) -> None:
        """unittest.TestCase tearDown for each test method.

        Tear down everything set up in setUp.
        """
        tearDown()
        self.config = None

    def _add_view(self, view_func=None, openapi=True) -> None:
        """Add a simple example view.

        :param view_func: an optional view callable.
        :param openapi: if True, enable openapi view deriver
        """
        self.config.add_route("foo", "/foo")
        if not view_func:
            view_func = lambda *arg: "foo"  # noqa: E731  # pragma: no branch
        self.config.add_view(
            openapi=openapi, renderer="json", view=view_func, route_name="foo"
        )

    def _get_view(self) -> View:
        """Return wrapped view method registered in _add_view."""
        request_interface = self.config.registry.queryUtility(IRouteRequest, name="foo")
        view = self.config.registry.adapters.registered(
            (IViewClassifier, request_interface, Interface), IView, name=""
        )
        return view

    def _get_request(self, params: t.Dict = None) -> DummyRequest:
        """Create a DummyRequest instance matching example view.

        :param params: Query parameter dictionary
        """
        request = DummyRequest(
            config=self.config, params=params, content_type="text/html"
        )
        request.matched_route = DummyRoute(name="foo", pattern="/foo")
        return request

    def test_view_raises_valid_http_exception(self) -> None:
        """Test View raises HTTPException.

        Example view raises a defined response code.
        """
        from pyramid.httpexceptions import HTTPBadRequest

        def view_func(*args):
            raise HTTPBadRequest("bad foo request")

        self._add_view(view_func)
        view = self._get_view()
        request = self._get_request(params={"bar": "1"})
        with self.assertRaises(HTTPBadRequest) as cm:
            view(None, request)
        response = cm.exception
        # not enough of pyramid has been set up so we need to render the
        # exception response ourselves.
        response.prepare({"HTTP_ACCEPT": "application/json"})
        self.assertIn("bad foo request", response.json["message"])

    def test_request_validation_error(self) -> None:
        """Request validation errors are rendered as 400 JSON responses."""
        self._add_view()
        # run request through router
        router = Router(self.config.registry)
        environ = {
            "wsgi.url_scheme": "http",
            "SERVER_NAME": "localhost",
            "SERVER_PORT": "8080",
            "REQUEST_METHOD": "GET",
            "PATH_INFO": "/foo",
            "HTTP_ACCEPT": "application/json",
        }
        start_response = DummyStartResponse()
        with self.assertLogs(level="INFO") as cm:
            response = router(environ, start_response)

        self.assertEqual(start_response.status, "400 Bad Request")
        self.assertEqual(
            json.loads(response[0]),
            [
                {
                    "exception": "MissingRequiredParameter",
                    "message": "Missing required parameter: bar",
                    "field": "bar",
                }
            ],
        )
        self.assertEqual(
            cm.output, ["INFO:pyramid_openapi3:Missing required parameter: bar"]
        )

    def test_response_validation_error(self) -> None:
        """Test View raises ResponseValidationError.

        Example view raises an undefined response code.
        The response validation tween should catch this as response validation error,
        and return an error 500.
        """
        from pyramid.httpexceptions import HTTPPreconditionFailed

        self._add_view(lambda *arg: HTTPPreconditionFailed())

        # run request through router
        router = Router(self.config.registry)
        environ = {
            "wsgi.url_scheme": "http",
            "SERVER_NAME": "localhost",
            "SERVER_PORT": "8080",
            "REQUEST_METHOD": "GET",
            "PATH_INFO": "/foo",
            "HTTP_ACCEPT": "application/json",
            "QUERY_STRING": "bar=1",
        }
        start_response = DummyStartResponse()
        with self.assertLogs(level="WARN") as cm:
            response = router(environ, start_response)
        self.assertEqual(start_response.status, "500 Internal Server Error")
        self.assertEqual(
            json.loads(response[0]),
            [
                {
                    "exception": "InvalidResponse",
                    "message": "Unknown response http status: 412",
                }
            ],
        )
        self.assertEqual(
            cm.output, ["WARNING:pyramid_openapi3:Unknown response http status: 412"]
        )

    def test_nonapi_view(self) -> None:
        """Test View without openapi validation."""
        self._add_view(openapi=False)
        # run request through router
        router = Router(self.config.registry)
        environ = {
            "wsgi.url_scheme": "http",
            "SERVER_NAME": "localhost",
            "SERVER_PORT": "8080",
            "REQUEST_METHOD": "GET",
            "PATH_INFO": "/foo",
        }
        start_response = DummyStartResponse()
        response = router(environ, start_response)
        self.assertEqual(start_response.status, "200 OK")
        self.assertIn(b"foo", b"".join(response))
