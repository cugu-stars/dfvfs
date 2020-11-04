#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the HFS resolver helper implementation."""

from __future__ import unicode_literals

import unittest

from dfvfs.resolver_helpers import hfs_resolver_helper

from tests.resolver_helpers import test_lib


class HFSResolverHelperTest(test_lib.ResolverHelperTestCase):
  """Tests for the HFS resolver helper implementation."""

  def testNewFileObject(self):
    """Tests the NewFileObject function."""
    resolver_helper_object = hfs_resolver_helper.HFSResolverHelper()
    self._TestNewFileObject(resolver_helper_object)

  def testNewFileSystem(self):
    """Tests the NewFileSystem function."""
    resolver_helper_object = hfs_resolver_helper.HFSResolverHelper()
    self._TestNewFileSystem(resolver_helper_object)


if __name__ == '__main__':
  unittest.main()
