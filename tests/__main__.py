from __future__ import absolute_import, print_function

import unittest
import logging

from .test_trees import TestTrees
from .test_tools import TestStandalone

try:
    from .test_nearley.test_nearley import TestNearley
except ImportError:
    pass

# from .test_selectors import TestSelectors
# from .test_grammars import TestPythonG, TestConfigG

from .test_parser import (
        TestLalrStandard,
        TestEarleyStandard,
        TestCykStandard,
        TestLalrContextual,
        # TestEarleyScanless,
        TestEarleyDynamic,

        # TestFullEarleyScanless,
        TestFullEarleyDynamic,

        TestParsers,
        )

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    unittest.main()
