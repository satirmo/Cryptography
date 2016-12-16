from CryptographyMethods import *;

class LinearCongruenceCipher :
	def __init__( self, a, b, n ) :
		self.a = a;
		self.b = b;
		self.n = n;

	def encrypt( self, message ) :
		embeddedMessage = embedMessage( message );
		ciphertext = [ findMod( self.a * m + self.b, self.n ) for m in embeddedMessage ];
		
		return ciphertext;

	def decrypt( self, ciphertext ) :
		message = "";
		aInv = multiplicativeInverse( self.a, self.n );

		for t in ciphertext :
			ft = findMod( aInv * t - aInv * self.b, self.n );
			message += embedInverse( ft );

		return message;

#	Driver Code
LCC = LinearCongruenceCipher( 8, 5, 43 );
ciphertext = LCC.encrypt( "WHY HELLO THERE" );
message = LCC.decrypt( ciphertext );

print( "Message:", message );
print( "Ciphertext:", ciphertext );