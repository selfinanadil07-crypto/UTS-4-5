import math

def layang_layang (d1, d2, s1, s2):
	return 2* (s1 + s2), 0.5 * d1 * d2
	
def segitiga(a, t, s1, s2, s3):
	return s1 + s2 + s3, 0.5 * a*t
	
def persegi(s):
	return 4* s, s * s

def jajar_genjang(a, t, sm):
	return 2* (a + sm), a * t

def belah_ketupat(s, d1, d2):
	return 4* s, 0.5 * d1 * d2
	
def trapesium(a, b, c, d, t):
	return a + b + c + d, 0.5 * (a + b) * t
	
def heksagon(s):
	return 6 * s, (3 * math.sqrt(3) / 2) * s**2
	
def lingkaran(r):
	return 2*3.14* г, 3.14* r**2
	
def persegi_panjang(p, I):
	return 2* (p + 1), p * 1
	
def pentagon(s):
    return 5 * s, 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * s**2