import numpy as np
from scipy.misc import imread,imresize,imsave
data_set_size=50000;
#unpickle input
def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

def loss(w):
	scores = w.dot(data)
	reg=np.sum(np.square(w))	
	a=np.arange(data_set_size)
	cc = scores[labels,a]
	scores=np.maximum(0,scores-cc+delta)
	scores[labels,a]=0
	return (np.sum(scores)/data_set_size)+reg
	
#main
W = np.random.random((10,3072))
delta = 10
d=unpickle("data_batch_1")
data = d['data']
data = np.transpose(data)
labels = d['labels']
for i in range(2,6):
	d=unpickle("data_batch_"+str(i))
	img = d['data']
	img = np.transpose(img)
	l = d['labels']
	data = np.append(data,img,axis=1)
	labels = np.append(labels,l)
print data
print W 
print loss(W) 
