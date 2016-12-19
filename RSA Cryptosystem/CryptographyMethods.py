def findMod( x, n ) :
	m = 1;

	while x < 0 :
		x += m * n;
		m <<= 1;

	return x % n;

def extendedEuclid( a, b ) :
	prevx, prevy = 1, 0;
	x, y = 0, 1;

	while b > 0 :
		q = int( a / b );

		prevx, x = x, prevx - x * q;
		prevy, y = y, prevy - y * q;
		
		a, b = b, a % b;

	gcd = a;

	return gcd, prevx, prevy;

def gcd( a, b ) :
	if b == 0 :
		return a;

	return gcd( b, a % b );

def multiplicativeInverse( x, n ) :
	gcd, tn, tx = extendedEuclid( n, findMod( x, n ) );

	return findMod( tx, n ) if gcd == 1 else -1;

def phi( n ) :
	sieve = [ True for i in range( n ) ];

	ret = 1;

	for i in range( 2, n ) :
		if n < i :
			break;

		if sieve[ i ] == True :
			j = i * i;

			while j < n :
				sieve[ j ] = False;
				j += i;

			if n % i == 0 :
				ret = ( i - 1 ) * ret / i;

				while n % i == 0 :
					n /= i;

	if n != 1 :
		ret = ( n - 1 ) * ret / n;

	return ret;

def modularExponentiation( base, exp, mod ) :
	ret = 1;
	mult = findMod( base, mod );

	while exp != 0 :
		if exp % 2 == 1 :
			ret = ( ret * mult ) % mod;

		exp /= 2;
		mult = ( mult * mult ) % mod;

	return ret;

def embedMessage( message ) :
	return [ embed( c ) for c in message ];

def embed( c ) :
	if c == ' ' :
		return 26;

	return ord( c ) - ord( 'A' );

def embedInverse( t ) :
	if t == 26 :
		return ' ';

	return chr( t + ord( 'A' ) );
