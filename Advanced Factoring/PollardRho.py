from CryptographyMethods import *;
import random;
import math;
import time;

def f( x, a ) :
	return x * x + a;

def PollardRho( n ) :
	iterations = int( math.sqrt( math.sqrt( n ) ) );

	factored = False;
	cnt = 0;

	while not factored :
		cnt += 1;
		random.seed();
		x = random.randrange( 0, n-1, 1 );
		y = x;

		random.seed();
		a = random.randrange( 0, n-1, 1 );
		
		for i in range( iterations ) :
			x = findMod( f( x, a ), n );

			y = findMod( f( y, a ), n );
			y = findMod( f( y, a ), n );

			t = findMod( abs( x - y ), n );
			g = gcd( n, t );

			if g != 1 and g != n :
				p = gcd( t, n );
				q = int( n / p );

				factored = True;
				break;

	return p, q;

#	Driver Code
n = 982451653 * 961748941;

start = time.time();
p, q = PollardRho( n );
end  = time.time();

print( n, "=", p, "*", q );
print( "Time Elapsed:", end - start );