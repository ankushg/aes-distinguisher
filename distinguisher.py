
import scipy.stats
import aes
import random

def distinguish(x, y):
	# x, y = lists of data points
	ks, pks = scipy.stats.ks_2samp(x, y)
	u, pu = scipy.stats.mannwhitneyu(x, y)
	return {'ks': ks, 'pks': pks, 'u': u, 'pu': pu}

def F(r, p, q):
	# r = rounds
	# p = byte to vary (in random 128 bit string)
	# q = byte to check (in result)
	# returns number of different values of q
	M = aes.generateRandomKey(16)
	S = [M[:p] + byte + M[p+1:] for byte in [chr(i) for i in xrange(2**8)]]
	K = aes.generateRandomK	ey(16)
	T = [aes.encryptData(K, s, nbrRounds=r) for s in S]
	return len(set([t[q] for t in T]))

def test(r, numTrials):
	# r = rounds
	# numTrials = number of times to run F
	X = [F(r, random.randint(0, 16), random.randint(0, 16)) for i in xrange(numTrials)]
	Y = [F(10, random.randint(0, 16), random.randint(0, 16)) for i in xrange(numTrials)]
	return X, Y, distinguish(X, Y)

def alt_test(r, numTrials):
	# r = rounds
	# numTrials = number of times to run F
	X = []
	Y = []
	for i in xrange(numTrials):
		M = aes.generateRandomKey(16)
		S = [M[:p] + byte + M[p+1:] for byte in [chr(i) for i in xrange(2**8)]]
		K = aes.generateRandomKey(16)

		T_r = [aes.encryptData(K, s, nbrRounds=r) for s in S]
		T_10 = [aes.encryptData(K, s, nbrRounds=10) for s in S]
		F_r = len(set([t[q] for t in T_r]))
		F_10 = len(set([t[q] for t in T_10]))
		X.append(F_r)
		Y.append(F_10)
	return X, Y, distinguish(X, Y)

def Frandom(q):
	M = [aes.generateRandomKey(16) for i in xrange(2**8)]
	return len(set([m[q] for m in M]))

def testRandom(r, numTrials):
	X = [F(r, random.randint(0, 15), random.randint(0, 15)) for i in xrange(numTrials)]
	Y = [Frandom(random.randint(0, 15)) for i in xrange(numTrials)]
	return X, Y, distinguish(X, Y)
