import unittest
from nose.tools import eq_

from celery import current_app

import saruman.tasks.kernel.modprobe


class KernelModprobeTest(unittest.TestCase):
    def setUp(self):
        current_app.conf.CELERY_ALWAYS_EAGER = True

    def test_check(self):
        rst = saruman.tasks.kernel.modprobe.Check().apply(args=('dummy',)).get()
        assert isinstance(rst, bool) and rst is not None, "%r doesnt return a boolean or return None" % rst

    def test_add(self):
        rst = saruman.tasks.kernel.modprobe.Add().apply(args=('dummy',)).get()
        assert rst is  None, "%r doesnt return None" % rst
