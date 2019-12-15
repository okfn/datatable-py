# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from . import config
__version__ = config.VERSION


# Module API

from .cli import cli
from .stream import Stream
from .loader import Loader
from .parser import Parser
from .writer import Writer
from .validate import validate
from .exceptions import TabulatorException
from .exceptions import IOError
from .exceptions import HTTPError
from .exceptions import SourceError
from .exceptions import FormatError
from .exceptions import EncodingError

# Deprecated

from . import exceptions
