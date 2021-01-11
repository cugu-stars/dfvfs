#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the encrypted stream resolver helper implementation."""

import unittest

from dfvfs.lib import definitions
from dfvfs.path import factory as path_spec_factory
from dfvfs.resolver_helpers import encrypted_stream_resolver_helper

from tests.resolver_helpers import test_lib


class EncryptedStreamResolverHelperTest(test_lib.ResolverHelperTestCase):
  """Tests for the encrypted stream resolver helper implementation."""

  def testNewFileObject(self):
    """Tests the NewFileObject function."""
    resolver_helper_object = (
        encrypted_stream_resolver_helper.EncryptedStreamResolverHelper())
    self._TestNewFileObject(resolver_helper_object)

  def testNewFileSystem(self):
    """Tests the NewFileSystem function."""
    test_path = self._GetTestFilePath(['syslog.rc4'])
    self._SkipIfPathNotExists(test_path)

    test_os_path_spec = path_spec_factory.Factory.NewPathSpec(
        definitions.TYPE_INDICATOR_OS, location=test_path)
    test_encrypted_stream_path_spec = path_spec_factory.Factory.NewPathSpec(
        definitions.TYPE_INDICATOR_ENCRYPTED_STREAM,
        encryption_method=definitions.ENCRYPTION_METHOD_RC4,
        parent=test_os_path_spec)

    resolver_helper_object = (
        encrypted_stream_resolver_helper.EncryptedStreamResolverHelper())
    self._TestNewFileSystem(
        resolver_helper_object, test_encrypted_stream_path_spec)


if __name__ == '__main__':
  unittest.main()
