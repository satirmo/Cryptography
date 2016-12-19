from CryptographyMethods import *;
import time;

class RSACryptosystem :
	def __init__( self, e, p, q ) :
		self.e = e;
		self.p = p;
		self.q = q;
		self.n = p * q;

	def encrypt( self, message ) :
		embeddedMessage = embedMessage( message );
		ciphertext = [ modularExponentiation( m, self.e, self.n ) for m in embeddedMessage ];
		
		return ciphertext;

	def decrypt( self, ciphertext ) :
		message = "";
		phiN = ( self.p - 1 ) * ( self.q - 1 );
		eInv = multiplicativeInverse( self.e, phiN );

		for t in ciphertext :
			ft = modularExponentiation( t, eInv, self.n );
			message += embedInverse( ft );

		return message;

	def decryptOutsider( self, ciphertext ) :
		for i in range( 2, self.n ) :
			if self.n % i == 0 :
				p = i;
				q = self.n / p;

				phiN = ( p - 1 ) * ( q - 1 );

				break;

		message = "";
		eInv = multiplicativeInverse( self.e, phiN );

		for t in ciphertext :
			ft = modularExponentiation( t, eInv, self.n );
			message += embedInverse( ft );

		return message;

#	Driver Code
rsa = RSACryptosystem( 5, 15485863, 32452843 );
ciphertext = rsa.encrypt( "WHAT EVER TOMORROW BRINGS I WILL BE THERE" );

start = time.time();
message = rsa.decrypt( ciphertext );
end = time.time();

startOutsider = time.time();
messageOutsider = rsa.decryptOutsider( ciphertext );
endOutsider = time.time();

print( "Message:", message );
print( "Time:", end - start );

print();
print( "Message:", messageOutsider );
print( "Time:", endOutsider - startOutsider );

print();
print( "Ciphertext:", ciphertext );