#!/usr/bin/env python

from distutils.core import setup

import os
def get_build():
	path = "./.build"
	
	if os.path.exists(path):
		fp = open(path, "r")
		build = eval(fp.read())
		if os.path.exists("./.increase_build"):
			build += 1
		fp.close()
	else:
		build = 1
	
	fp = open(path, "w")
	fp.write(str(build))
	fp.close()
	
	return str(build)

setup(name = "pylast",
      version = "0.5." + get_build(),
      author = "Amr Hassan <amr.hassan@gmail.com>, coolkehon <coolkehon[at]gmail>",
	  description = "A Python interface to Last.fm (and other API compatible social networks) using kyotocabinet cache backend",
      author_email = "amr.hassan@gmail.com, coolkehon@gmail.com",
      url = "https://github.com/coolkehon/pylast",
      py_modules = ("pylast", "kyotocabinet"),
	  license = "Apache2"
	)
