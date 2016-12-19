from CryptographyMethods import *;

class ExponentialCipher :
	def __init__( self, e, p ) :
		self.e = e;
		self.p = p;

	def encrypt( self, message ) :
		embeddedMessage = embedMessage( message );
		ciphertext = [ modularExponentiation( m, self.e, self.p ) for m in embeddedMessage ];
		
		return ciphertext;

	def decrypt( self, ciphertext ) :
		message = "";
		eInv = multiplicativeInverse( self.e, phi( self.p ) );

		for t in ciphertext :
			ft = modularExponentiation( t, eInv, self.p );
			message += embedInverse( ft );

		return message;

#	Driver Code
EC = ExponentialCipher( 25, 43 );
ciphertext = EC.encrypt( "LIKE NO ONE EVER WAS" );
message = EC.decrypt( ciphertext );

print( "Message:", message );
print( "Ciphertext:", ciphertext );