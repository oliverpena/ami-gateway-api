import sys
from unittest import TestCase, main
from unittest.mock import Mock

import jwt

from utils.jwt_utils import jwt_required

sys.path.append('.')
from app import create_app  # noqa


class JwtUtilsTests(TestCase):
    def setUp(self) -> None:
        self.app = create_app('testing')
        self.mock_request = Mock(url='https://test.com')
        token = jwt.encode({'test': 'payload'}, self.app.config['SECRET_KEY'])
        self.mock_request.headers = {
            'X-API-KEY': token}  # noqa
        return super().setUp()

    def test_jwt_required_valid_token(self):
        with self.app.test_request_context(self.mock_request.url,
                                           headers=self.mock_request.headers):
            @jwt_required
            def mock_get():
                return 200
            self.assertEqual(mock_get(), 200)

    def test_jwt_required_invalid_token(self):
        with self.app.test_request_context(self.mock_request.url,
                                           headers={'X-API-KEY': 'invalid'}):
            @jwt_required
            def mock_get():
                return 200
            response = mock_get()
            self.assertEqual(response[1], 401)

    def test_jwt_required_no_token(self):
        with self.app.test_request_context(self.mock_request.url):
            @jwt_required
            def mock_get():
                return 200
            response = mock_get()
            self.assertEqual(response[1], 401)


if __name__ == '__main__':
    main()
