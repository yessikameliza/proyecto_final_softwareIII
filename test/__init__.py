#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from test import mymoodule


class TestMyModule(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(mymoodule.sum(5, 7), 12)


if __name__ == "__main__":
    unittest.main()
