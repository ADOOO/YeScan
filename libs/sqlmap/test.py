#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.dont_write_bytecode = True

from lib.utils import versioncheck  # this has to be the first non-standard import

import bdb
import distutils
import inspect
import logging
import os
import re
import shutil
import sys
import thread
import time
import traceback
import warnings

warnings.filterwarnings(action="ignore", message=".*was already imported", category=UserWarning)
warnings.filterwarnings(action="ignore", category=DeprecationWarning)

from lib.core.data import logger

try:
    from lib.controller.controller import start
    from lib.core.common import banner
    from lib.core.common import createGithubIssue
    from lib.core.common import dataToStdout
    from lib.core.common import getSafeExString
    from lib.core.common import getUnicode
    from lib.core.common import maskSensitiveData
    from lib.core.common import setPaths
    from lib.core.common import weAreFrozen
    from lib.core.data import cmdLineOptions
    from lib.core.data import conf
    from lib.core.data import kb
    from lib.core.data import paths
    from lib.core.common import unhandledExceptionMessage
    from lib.core.exception import SqlmapBaseException
    from lib.core.exception import SqlmapShellQuitException
    from lib.core.exception import SqlmapSilentQuitException
    from lib.core.exception import SqlmapUserQuitException
    from lib.core.option import initOptions
    from lib.core.option import init
    from lib.core.profiling import profile
    from lib.core.settings import IS_WIN
    from lib.core.settings import LEGAL_DISCLAIMER
    from lib.core.settings import VERSION
    from lib.core.testing import smokeTest
    from lib.core.testing import liveTest
    from lib.parse.cmdline import cmdLineParser
    from lib.utils.api import setRestAPILog
    from lib.utils.api import StdDbOut
except KeyboardInterrupt:
    errMsg = "user aborted"
    logger.error(errMsg)

    raise SystemExit

# cmdLineOptions.update(cmdLineParser().__dict__)
