#!/usr/bin/env python
import sys, os.path as ospath
dir = ospath.dirname(__file__)
sys.path.append(ospath.abspath(ospath.join(dir, 'src.zip')))
del sys, ospath, dir
from proxy import main
main()