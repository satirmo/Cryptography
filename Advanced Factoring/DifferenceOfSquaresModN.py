from CryptographyMethods import *;
import random;
import math;
import time;

def isSquare( x ) :
	m = int( math.sqrt( x ) );

	return m * m == x;

def DifferenceOfSquaresModN( n ) :
	i = 1;
	factored = False;
	k = random.randrange( 2, 50 );

	while not factored :
		t = k * n + i ** 2;

		m = int( math.sqrt( t ) );

		if m ** 2 != t :
			i += 1;
			continue;

		p = gcd( n, m - i );
		q = gcd( n, m + i );

		if p != 1 and p != n :
			factored = True;

		i += 1;

	return p, q;

#	Driver Code
n = 160481219 * 179424673;

start = time.time();
p, q = DifferenceOfSquaresModN( n );
end  = time.time();

print( n, "=", p, "*", q );
print( "Time Elapsed:", end - start );