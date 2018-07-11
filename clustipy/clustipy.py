import numpy as np
from sklearn.cluster import KMeans
import netaddr


def clustering(addresses: [netaddr.IPNetwork], n_clusters: int):
    ips = np.array([[int(x.ip)] for x in addresses], dtype=np.uint32)
    kmeans = KMeans(n_clusters=n_clusters)
    labels = kmeans.fit_predict(ips)
    centroids = np.array(kmeans.cluster_centers_, dtype=np.uint32)[:, 0]
    centroips = []
    for c in centroids.tolist():
        ip = netaddr.IPNetwork('0.0.0.0/32')
        ip.value = c
        centroips.append(ip)
    result = []
    for l in range(n_clusters):
        result.append([])
        members = [netaddr.IPAddress(int(x)) for x in ips[labels == l][:, 0]]
        for sp in centroips[l].supernet(0):
            if len([x for x in members if x in sp]) == len(members):
                result[l].append(sp)
        result[l].reverse()
    result = [x[0] for x in result]
    return sorted(result)
