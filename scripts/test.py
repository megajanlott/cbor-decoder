import pytest
import sys
status = pytest.main(['-x', 'tests'])
sys.exit(status)
