import sys
from unittest import TestCase, main

from flask import Flask

sys.path.append('.')
from app import authorisations, create_app  # noqa


class AppTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_app_create(self):
        app = create_app('testing')
        self.assertIsInstance(app, Flask)

    def test_authorizations(self):
        authorisation = authorisations()
        self.assertIsInstance(authorisation, dict)


if __name__ == '__main__':
    main()
