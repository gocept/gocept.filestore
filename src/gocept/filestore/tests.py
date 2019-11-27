# Copyright (c) 2006-2019 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$

import unittest

import doctest

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocFileSuite(
        'README.txt',
        optionflags=doctest.ELLIPSIS))
    return suite
