def findMod( x, n ) :
	while x < 0 :
		x += n;

	return x % n;

def findInverse( x, n ) :
	for i in range( n ) :
		if findMod( x * i, n ) == 1 :
			return i;

	return -1;

class Number :
	def __init__( self, a, alpha, p, alphaSq ) :
		if a == float( "inf" ) or alpha == float( "inf" ) :
			self.a = float( "inf" );
			self.alpha = float( "inf" );

		else :
			self.a = findMod( a, p );
			self.alpha = findMod( alpha, p );
		
		self.p = p;
		self.alphaSq = alphaSq;

	def __str__( self ) :
		return str( self.a ) + " + " + str( self.alpha ) + " alpha";

	def __eq__( self, other ) :
		return findMod( self.a - other.a, self.p ) == 0 and findMod( self.alpha - other.alpha, self.p ) == 0;

	def __ne__( self, other ) :
		return not self == other;

	def __add__( self, other ) :
		return Number( self.a + other.a, self.alpha + other.alpha, self.p, self.alphaSq );

	def __sub__( self, other ) :
		return Number( self.a - other.a, self.alpha - other.alpha, self.p, self.alphaSq );

	def __neg__( self ) :
		return Number( - self.a, - self.alpha, self.p, self.alphaSq );

	def __mul__( self, other ) :
		a = self.a * other.a + ( self.alpha * other.alpha ) * self.alphaSq;
		alpha = self.a * other.alpha + self.alpha * other.a;

		return Number( a, alpha, self.p, self.alphaSq );

	def __truediv__( self, other ) :
		A = self;
		B = other;

		conB = B.findConjugate();

		num = A * conB;
		den = B * conB;

		invDen = Number( findInverse( den.a, A.p ), 0, A.p, A.alphaSq );

		return num * invDen;

	def findMod( self ) :
		return Number( findMod( self.a, self.p ), findMod( self.alpha, self.p ), self.p, self.alphaSq );

	def findConjugate( self ) :
		return Number( self.a, - self.alpha, self.p, self.alphaSq );

	def isInfinity( self ) :
		return self.a == float( "inf" ) or self.alpha == float( "inf" );

class EllipticCurve :
	def __init__( self, p, a, b, c, alphaSq ) :
		self.p = p;
		self.a = a;
		self.b = b;
		self.c = c;
		self.alphaSq = alphaSq;

	def f( self, x ) :
		A = Number( self.a, 0, self.p, x.alphaSq );
		B = Number( self.b, 0, self.p, x.alphaSq );
		C = Number( self.c, 0, self.p, x.alphaSq );

		res = x * x * x + A * x * x + B * x + C;

		return res.findMod();

	def findPoints( self ) :
		pts = [ Point( float( "inf"), float( "inf"), float( "inf"), float( "inf"), self ) ];

		for i in range( self.p ) :
			x = Number( i, 0, self.p, self.alphaSq );

			for j in range( int( self.p / 2 ) ) :
				y = Number( j, 0, self.p, self.alphaSq );
				P = Point( x.a, x.alpha, y.a, y.alpha, self );

				if self.isPoint( P ) :
					pts.append( P );
					
					if j != 0 :
						ty = - y;
						pts.append( Point( x.a, x.alpha, ty.a, ty.alpha, self ) );

		return pts;

	def isPoint( self, P ) :
		return P.y * P.y == self.f( P.x );

class Point :
	def __init__( self, x, xAlpha, y, yAlpha, curve ) :
		if x == float( "inf" ) or xAlpha == float( "inf" ) or y == float( "inf" ) or yAlpha == float( "inf" ) :
			x = float( "inf" );
			xAlpha = float( "inf" );
			y = float( "inf" );
			yAlpha = float( "inf" );

		self.x = Number( x, xAlpha, curve.p, curve.alphaSq );
		self.y = Number( y, yAlpha, curve.p, curve.alphaSq );
		self.curve = curve;

	def __str__( self ) :
		if self.isInfinity() :
			return "inf";

		return "( " + str( self.x ) + ", " + str( self.y ) + " )";

	def __eq__( self, other ) :
		return self.x == other.x and self.y == other.y;

	def __ne__( self, other ) :
		return not self == other;

	def __add__( self, other ) :
		A = self;
		B = other;

		if A.isInfinity() and B.isInfinity() :
			return A;

		if A.isInfinity() :
			return B;

		if B.isInfinity() :
			return A;

		p = self.curve.p;
		alphaSq = self.curve.alphaSq;

		if A.x != B.x:
			dy = A.y - B.y;
			dx = A.x - B.x;

			m = dy / dx;

			x3 = m * m - Number( self.curve.a, 0, p, alphaSq ) - A.x - B.x;
			t3 = m * ( x3 - A.x ) + A.y;
			y3 = Number( - t3.a, - t3.alpha, p, alphaSq );

			x3 = x3.findMod();
			y3 = y3.findMod();

			return Point( x3.a, x3.alpha, y3.a, y3.alpha, self.curve );

		if A.y == - B.y :
			return Point( float( "inf" ), float( "inf" ), float( "inf" ), float( "inf" ), self.curve );

		num = Number( 3, 0, p, alphaSq ) * A.x * A.x + Number( 2, 0, p, alphaSq ) * Number( self.curve.a, 0, p, alphaSq ) * A.x + Number( self.curve.b, 0, p, alphaSq );
		den = Number( 2, 0, p, alphaSq ) * A.y;
		
		m = num / den;

		x3 = m * m - Number( self.curve.a, 0, p, alphaSq ) - A.x - B.x;
		t3 = m * ( x3 - A.x ) + A.y;
		y3 = Number( - t3.a, - t3.alpha, p, alphaSq );

		x3 = x3.findMod();
		y3 = y3.findMod();

		return Point( x3.a, x3.alpha, y3.a, y3.alpha, self.curve );

	def __sub__( self, other ) :
		return self + ( - other );

	def __neg__( self ) :
		y = - self.y;

		return Point( self.x.a, self.x.alpha, y.a, y.alpha, self.curve );

	def isInfinity( self ) :
		return self.x.isInfinity() or self.y.isInfinity();

	def multiply( self, p ) :
		res = Point( float( "inf" ), float( "inf" ), float( "inf" ), float( "inf" ), self.curve );

		for i in range( p ) :
			res = res + self;

		return res;

# print( findKoblitzX( 'G', 47, 5 ) );

E = EllipticCurve( 23, 2, 7, -1, 0 );
# print( E.findPoints() );
P = Point( 7, 0, 11, 0, E );
print( P.multiply( 25 ) );

''' Q = Point( 2, 0, 11, 0, E );
print( Q.multiply( 25 ) );

k = 19;

message = "PRO";

for c in message :
	C1 = P.multiply( k );

	t = Q.multiply( k );
	C2 = t.x + Number( ord( c ) - ord( 'A' ) + 1, 0, P.curve.p, P.curve.alphaSq );

	print( C1, C2 );

print( p, P, "=", P.multiply( p ) );
print( p, Q, "=", Q.multiply( p ) );

E = EllipticCurve( 47, 5, 8, 11, 0 );
p = 8;
P = Point( 6, 0, 19, 0, E );
Q = Point( 16, 0, 43, 0, E );
print( p, P, "=", P.multiply( p ) );
print( p, Q, "=", Q.multiply( p ) );

E = EllipticCurve( 13, 3, 2, 7, 2 );

P = Point( 2, 0, 0, 3, E );
Q = Point( 11, 0, 0, 6, E );
res = P + Q;
print( P, "+", Q, "=", res ); '''