# Copyright (c) 2007 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$

import zope.deferredimport

zope.deferredimport.define(
    FileStore = 'gocept.filestore.filestore:FileStore'
    )
