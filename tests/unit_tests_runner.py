import os
import sys
import unittest

if __name__ == '__main__':
    suite = unittest.TestLoader().discover(
        start_dir='tests/unit_tests', pattern='*test.py')
    resutl = unittest.TextTestRunner(verbosity=2).run(suite)
    if resutl.wasSuccessful():
        try:
            sys.exit()
        except SystemExit:
            os._exit(0)
        except Exception:
            print('Error while running tests.')
    else:
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)
