import sys
from unittest import TestCase, main

import jwt

sys.path.append('.')
from app import create_app  # noqa


class HealthNameSpaceTests(TestCase):

    def setUp(self) -> None:
        self.app = create_app('testing')
        self.test_client = self.app.test_client()
        self.token = jwt.encode({'test': 'payload'},
                                self.app.config['SECRET_KEY'])
        return super().setUp()

    def test_health_status(self):
        rv = self.test_client.get(
            f'/{self.app.name}/health/status',
            headers={'X-API-KEY': self.token})
        self.assertEqual(rv.status, '200 OK')


if __name__ == '__main__':
    main()
