#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

# Sets up a global cache
cache=[0] * 1000000
cache[1]=1

def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return False
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
	
    return the max cycle length of the range [i, j]
    """
	
    return 1
	
	
# ------------
# cycle_length
# ------------

def cycle_length (n) :
    """
    n is an integer >0
	return the cycle length of n
	"""
	
	# Preconditions
    assert n > 0
    global cache
	
	# If n is already in cache
    if (n < 1000000 and cache[n] != 0):
        return cache[n]
	
	# If n is not in cache
    if ((n%2) == 0):
        num=n // 2
        cyclelength= 1 + cycle_length(num)
    else:
        num= n + (n // 2) + 1
        cyclelength= 2 + cycle_length(num)
	
    if (n < 1000000):
        cache[n]= cycle_length

    assert cyclelength > 0
    return cyclelength
	
# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
