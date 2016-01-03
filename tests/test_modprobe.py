import unittest
from nose.tools import eq_

from celery import current_app

import saruman.tasks.kernel.modprobe


class KernelModprobeTest(unittest.TestCase):
    def setUp(self):
        current_app.conf.CELERY_ALWAYS_EAGER = True

    def test(self):
        saruman.tasks.kernel.modprobe.Add().apply(args=('dummy',)).get()
        rst = saruman.tasks.kernel.modprobe.Check().apply(args=('dummy',)).get()
        eq_(rst, True)
        saruman.tasks.kernel.modprobe.Remove().apply(args=('dummy',)).get()
        rst = saruman.tasks.kernel.modprobe.Check().apply(args=('dummy',)).get()
        eq_(rst, False)
