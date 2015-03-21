
import scipy.stats

def distinguish(x, y):
	# x, y = lists of data points
	ks, pks = scipy.stats.ks_2samp(x, y)
	u, pu = scipy.stats.mannwhitneyu(x, y)
	return {'ks': ks, 'pks': pks, 'u': u, 'pu': u}