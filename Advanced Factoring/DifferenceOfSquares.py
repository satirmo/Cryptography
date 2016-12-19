from CryptographyMethods import *;
import random;
import math;
import time;

def DifferenceOfSquares( n ) :
	i = 1;
	factored = False;

	while not factored :
		t = n + i ** 2;
		m = int( math.sqrt( t ) );

		if m ** 2 == t :
			p = m - i;
			q = m + i;
			
			factored = True;

		i += 1;

	return p, q;

#	Driver Code
n = 160481219 * 179424673;

start = time.time();
p, q = DifferenceOfSquares( n );
end  = time.time();

print( n, "=", p, "*", q );
print( "Time Elapsed:", end - start );