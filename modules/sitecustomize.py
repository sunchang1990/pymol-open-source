# NOTE: This only works for module-based PyMOL builds.
# Embedded versions of PyMOL call PyUnicode_SetDefaultEncoding at startup
import sys
if sys.version_info[0] < 3:
    sys.setdefaultencoding("utf-8")
