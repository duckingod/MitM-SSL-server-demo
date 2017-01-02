#!/usr/bin/env python
import struct
def gn(b):
	pad = b"\x00"*(4-len(b))
	return struct.unpack(">L", pad + b)[0]

class TLSProtocolFormat:
	def __init__(self, b):
		self.read_tls_header(b)
	def read_tls_header(self, b):
		self.tls_header = {}
		self.tls_header['record_type'] = gn(b[0:1])
		self.tls_header['tls_version'] = (b[1], b[2])
		self.tls_header['header_length'] = gn(b[3:5])
		if self.tls_header['record_type']==22:
			self.read_handshake_header(b[5:])
	def read_handshake_header(self, b):
		def read_cipher_suites(b):
			self.handshake['cipher_suites_length'] = gn(b[0:2])
			self.handshake['cipher_suites'] = []
			n = self.handshake['cipher_suites_length']
                        b = b[2:]
			for i in range(n/2):
				self.handshake['cipher_suites'].append(hex(gn(b[i*2:(i+1)*2])))
			return n+1
		self.handshake = {}
		self.handshake['type'] = gn(b[0:1])
		self.handshake['message_length'] = gn(b[1:4])
		self.handshake['tls_version'] = (b[4], b[5])

		# b[5:37] random
                b = b[38:]

                self.handshake['sessionid_length'] = gn(b[:1])
                session_id_len = int((self.handshake['sessionid_length']+7)/8)
		self.handshake['sessionid'] = gn(b[1:1+session_id_len]) 
                b = b[1+session_id_len:]

		offset = read_cipher_suites(b)
                b = b[offset:]
		
		
		
		
	
msg = b"\x16\x03\x01\x00\xc0\x01\x00\x00\xbc\x03\x01Xj\x8d `\xed\xf5\x13\t\xb8\x1fJ\xdd\xfcy#\xc4\xc2\n\x04m\x05:\x9e\xb5\xc8\xb6O\xb1\x8b\xed/\x00\x00*\x00\xffV\x00\xc0$\xc0#\xc0\n\xc0\t\xc0\x08\xc0(\xc0'\xc0\x14\xc0\x13\xc0\x12\x00=\x00<\x005\x00/\x00\n\xc0\x07\xc0\x11\x00\x05\x00\x04\x01\x00\x00i\x00\x00\x00\x0e\x00\x0c\x00\x00\tlocalhost\x00\n\x00\x08\x00\x06\x00\x17\x00\x18\x00\x19\x00\x0b\x00\x02\x01\x003t\x00\x00\x00\x10\x000\x00.\x02h2\x05h2-16\x05h2-15\x05h2-14\x08spdy/3.1\x06spdy/3\x08http/1.1\x00\x05\x00\x05\x01\x00\x00\x00\x00\x00\x12\x00\x00"

f = TLSProtocolFormat(msg)
print(f.tls_header)
print(f.handshake)

