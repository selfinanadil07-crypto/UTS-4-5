import math

def limas_segitiga (la, Ist, t):
	return la + Ist, (1/3) * la * t
	
def prisma_pentagon (la, ka, t):
	return (2 * la) + (ka * t), la * t
	
def limas_segi_empat(la, Ist, t):
	return la + Ist, (1/3) * la * t
	
def prisma_segi_empat(la, ka, t):
	return (2 * la) + (ka * t), la * t
	
def kubus(s):
	return 6 * s**2, s**3
	
def tabung(r, t):
	return 2*3.14* r* (r + t), 3.14* r**2 * t
	
def kerucut(r, t, s):
	return 3.14* r* (r+s), (1/3) *3.14* r**2 * t
	
def balok(p, l, t):
    return 2 * (p*l + p*t + l*t), p*l*t

def prisma_segitiga(la, ka, t):
	return (2 * la) + (ka * t), la * t
	
def bola(r):
	return 4*3.14* r**2, (4/3) *3.14* r**3