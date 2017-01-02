#!/usr/bin/env python3

import traceback
import socket
import re
import os
import sys

"""
b"\x16\x03\x01\x00\xc0\x01\x00\x00\xbc\x03\x01Xj\x8d `\xed\xf5\x13\t\xb8\x1fJ\xdd\xfcy#\xc4\xc2\n\x04m\x05:\x9e\xb5\xc8\xb6O\xb1\x8b\xed/\x00\x00*\x00\xffV\x00\xc0$\xc0#\xc0\n\xc0\t\xc0\x08\xc0(\xc0'\xc0\x14\xc0\x13\xc0\x12\x00=\x00<\x005\x00/\x00\n\xc0\x07\xc0\x11\x00\x05\x00\x04\x01\x00\x00i\x00\x00\x00\x0e\x00\x0c\x00\x00\tlocalhost\x00\n\x00\x08\x00\x06\x00\x17\x00\x18\x00\x19\x00\x0b\x00\x02\x01\x003t\x00\x00\x00\x10\x000\x00.\x02h2\x05h2-16\x05h2-15\x05h2-14\x08spdy/3.1\x06spdy/3\x08http/1.1\x00\x05\x00\x05\x01\x00\x00\x00\x00\x00\x12\x00\x00"

"""
def redirect(fake_ip_server, real_ip_server):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(fake_ip_server)
	sock.listen(5)
	sock.settimeout(40)
	print("Start listening!")
	try: 
		while True:
			client, address = sock.accept()

			server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			server.connect(('', 80))
			print("\n\nClient Info: " + str(client) + "  " + str(address))
			while True:
				try:
					client.settimeout(3)
					msg = client.recv(4096)
				except Exception as e:
					traceback.print_exc()
					sys.stderr.write("[ERROR] %s\n" % str(e))
					break
				if not msg:
					pass
				else:
					print("Client send: " + repr(msg))

			client.close()
	except Exception as e:
		sock.close()
		traceback.print_exc()
		sys.stderr.write("[SERVER ERROR] %s\n" % str(e))

if __name__=="__main__":
	redirect(('', 81), None)

