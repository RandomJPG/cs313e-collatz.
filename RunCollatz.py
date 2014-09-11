#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2014
# -------------------------------
# Jacob Garcia
# jg56492
# -------------------------------

# -------
# imports
# -------

import sys
import random

from Collatz import collatz_solve

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)

def acceptance_test_gen():
	"""
	Creates acceptance tests by 
	generating random paired numbers
	"""
	
	for x in range(2000):
		i = random.randint(1, 1000000)
		j = random.randint(1, 1000000)
		
		if (i == j) :
			j = random.randint(1,1000000)
	
		line = str(i) + " " + str(j)
	
		print (line)

acceptance_test_gen()		
"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
"""
