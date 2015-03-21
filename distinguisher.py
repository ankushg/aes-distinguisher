
import scipy.stats
import aes

def distinguish(x, y):
	# x, y = lists of data points
	ks, pks = scipy.stats.ks_2samp(x, y)
	u, pu = scipy.stats.mannwhitneyu(x, y)
	return {'ks': ks, 'pks': pks, 'u': u, 'pu': u}

def F(r, p, q):
	# r = rounds
	# p = byte to vary (in random 128 bit string)
	# q = byte to check (in result)
	# returns number of different values of q
	M = aes.generateRandomKey(16)
	S = [M[:p] + byte + M[p+1:] for byte in [chr(i) for i in xrange(2**8)]]
	K = aes.generateRandomKey(16)
	T = [aes.encryptData(K, s, r) for s in S]
	return len(set([t[q] for t in T]))