try:
	import cPickle as pickle
except:
	import pickle
import pprint

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print 'DAT:',
pprint.pprint(data)
data_string = pickle.dumps(data)
print 'PICKLE: %r' % data_string
