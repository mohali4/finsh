import os
import sys
from posixpath import dirname
from pathlib import Path

_here_path = ''
if len(sys.argv) == 2 :_here_path = sys.argv[1]

os.system(f"{Path(dirname(__file__))/'finch'}  {_here_path}")