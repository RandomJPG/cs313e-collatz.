# -------------------------------
# Jacob Garcia
# jg56492
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, cycle_length, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

	# Given
    def test_read_1 (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
	
	# Tests second line
    def test_read_2 (self) :
        r    = StringIO("10 100\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        i, j = collatz_read(r)		
        self.assertEqual(i,  100)
        self.assertEqual(j,  200)

	# Tests extra spacing between numbers	
    def test_read_3 (self) :
        r    = StringIO("1    10")
        i, j = collatz_read(r)
        j    = collatz_read(r)		
        self.assertEqual(i, 1)
        self.assertEqual(j, False)

	# Tests extra spacing after numbers
    def test_read_4 (self) :
        r    = StringIO("1 10    ")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

	# Tests same string
    def test_read_5 (self) :
        r    = StringIO("10 10")
        i, j = collatz_read(r)
        self.assertEqual(i, 10)
        self.assertEqual(j, 10)	
		
    # ----
    # eval
    # ----

	# Given
    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

	# Given	
    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

	# Given	
    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

	# Given	
    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

	# Tests same numbers
    def test_eval_5 (self) :
        v = collatz_eval(900, 900)
        self.assertEqual(v, 55)
		
	# Tests reverse order
    def test_eval_6 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)
		
	# Tests corner case
    def test_eval_7 (self) :
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)
			
	# -----
    # cycle_length
    # -----
	
    def test_cycle_length_1 (self) :
        v = cycle_length(1)
        self.assertEqual(v, 1)
	
    def test_cycle_length_2 (self) :
        v = cycle_length(10)
        self.assertEqual(v, 7)
		
    def test_cycle_length_3 (self) :
        v = cycle_length(999999)
        self.assertEqual(v, 259)		
	
    # -----
    # print
    # -----

	# Given
    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
	
	# Test corner case	
    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 999999, 525)
        self.assertEqual(w.getvalue(), "1 999999 525\n")
	
	# Tests same number
    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 900, 900, 55)
        self.assertEqual(w.getvalue(), "900 900 55\n")	
   
	# Tests reverse order
    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")			
    
	# -----
    # solve
    # -----

	# Given
    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
	
	# Tests empty string	
    def test_solve_2 (self) :
        r = StringIO("")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")
    
	# Tests corner case
    def test_solve_3 (self) :
        r = StringIO("1 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 999999 525\n")
		
	# Tests same number	
    def test_solve_4 (self) :
        r = StringIO("900 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "900 900 55\n")
		
	# Tests reverse order	
    def test_solve_5 (self) :
        r = StringIO("10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n")		
# ----
# main
# ----

main()