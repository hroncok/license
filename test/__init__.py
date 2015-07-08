import os
import sys


init = os.path.abspath(__file__)
test = os.path.dirname(init)
project = os.path.dirname(test)
sys.path.insert(0, project)
