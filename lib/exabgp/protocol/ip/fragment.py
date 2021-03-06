# encoding: utf-8
"""
fragment.py

Created by Thomas Mangin on 2010-02-04.
Copyright (c) 2009-2015 Exa Networks. All rights reserved.
"""

from exabgp.protocol.resource import Resource


# =================================================================== Fragment

# Uses bitmask operand format defined above.
#   0   1   2   3   4   5   6   7
# +---+---+---+---+---+---+---+---+
# |   Reserved    |LF |FF |IsF|DF |
# +---+---+---+---+---+---+---+---+
#
# Bitmask values:
# +  Bit 7 - Don't fragment (DF)
# +  Bit 6 - Is a fragment (IsF)
# +  Bit 5 - First fragment (FF)
# +  Bit 4 - Last fragment (LF)

class Fragment (Resource):
	_NAME = 'fragment'

	NOT      = 0x00
	DONT     = 0x01
	IS       = 0x02
	FIRST    = 0x04
	LAST     = 0x08
	# reserved = 0xF0

	_VALUE = dict ((k.lower().replace('_','-'),v) for (k,v) in {
		'NOT-A-FRAGMENT': NOT,
		'DONT-FRAGMENT':  DONT,
		'IS-FRAGMENT':    IS,
		'FIRST-FRAGMENT': FIRST,
		'LAST-FRAGMENT':  LAST,
	}.items())

	_STRING = dict([(r,l) for (l,r) in _VALUE.items()])
