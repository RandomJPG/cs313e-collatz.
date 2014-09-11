# -------------------------------
# Jacob Garcia
# jg56492
# -------------------------------

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
    
    # Preconditions
    assert (i > 0 and i < 1000000)
    assert (j > 0 and j < 1000000)

	# Swaps i and j if needed
    if (i > j):
        temp = j
        j = i
        i = temp
    assert j >= i		
	
	# Sets max and creates m, the middle of i and j
    max_cycle = 0
    m = j // 2
	
    if (i < m):
        for num in range(m, j + 1):
            cycle= cycle_length(num)
            if (cycle > max_cycle):
                max_cycle = cycle			
    else:
        for num in range(i, j + 1):
            cycle = cycle_length(num)
            if (cycle > max_cycle):
               max_cycle = cycle
	
    assert max_cycle > 0
    return max_cycle
	
	
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
    cyclelength = 1
	
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
	
	# Add to cache
    if (n < 1000000):
        cache[n]= cyclelength
	
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