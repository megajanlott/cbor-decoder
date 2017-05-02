#!/usr/bin/env python3

import pytest
import sys
status = pytest.main(['-x', 'tests'])
sys.exit(status)
