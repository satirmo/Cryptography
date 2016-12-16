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

	return a, prevx, prevy;

def multiplicativeInverse( x, n ) :
	gcd, tn, tx = extendedEuclid( n, findMod( x, n ) );

	return findMod( tx, n ) if gcd == 1 else -1;

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