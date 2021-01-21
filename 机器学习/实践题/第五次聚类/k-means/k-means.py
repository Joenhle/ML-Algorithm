import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def get_sse(data,center,y_pred):
    sse = 0
    for i in range(data.shape[0]):
        c = y_pred[i]
        sse += (data[i][0]-center[c][0])**2 + (data[i][1]-center[c][1])**2
    return sse

import numpy as np
data = [[2,5],[4,6],[3,1],[6,4],[7,2],[8,4],[2,3],[3,1],[5,7],[6,9],[12,16],[10,11],[15,19],[16,12],[11,15],
        [10,14],[19,11],[17,14],[16,11],[13,19]]
data = np.array(data)
for index, k in enumerate((2,3,4,5)):
    model = KMeans(n_clusters=k,random_state=k).fit(data)
    y_pred = model.predict(data)
    see = get_sse(data,model.cluster_centers_,y_pred)
    print("k="+str(k),"see="+str(see))
    print("center:\n",model.cluster_centers_)
    plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],marker='x',c='r')
    plt.scatter(data[:,0], data[:,1],c=y_pred)
    plt.text(.99, .01, ('k=%d, see: %.2f' % (k, see)), transform=plt.gca().transAxes, size=10,
             horizontalalignment='right')
    plt.show()

