import numpy as np
import scipy.cluster.hierarchy
from pyxdameraulevenshtein import damerau_levenshtein_distance
from collections import defaultdict

def cluster_ngrams(ngrams, compute_distance, max_dist, method):
    """
    Cluster ngrams.

    Params:
        ngrams: [list] List of tuple of words in each ngram to cluster.
        compute_distance: [func] Function that computes distance between two
            pairs of ngrams.
        max_dist: [float] Maximum distance allowed for two clusters to merge.
        method: [string] Method to use for lustering.  'single',
            'complete', 'average', 'centroid', 'median', 'ward', or 'weighted'.
            See http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage for details.

    Returns:
        clusters: [list] List of ngrams in each cluster.
    """
    indices = np.triu_indices(len(ngrams), 1)
    pairwise_dists = np.apply_along_axis(
        lambda col: compute_distance(ngrams[col[0]], ngrams[col[1]]),
        0, indices)
    hierarchy = scipy.cluster.hierarchy.linkage(pairwise_dists, method=method)
    clusters = dict((i, [i]) for i in range(len(ngrams)))
    for (i, iteration) in enumerate(hierarchy):
        cl1, cl2, dist, num_items = iteration
        if dist >  max_dist:
            break
        items1 = clusters[cl1]
        items2 = clusters[cl2]
        del clusters[cl1]
        del clusters[cl2]
        clusters[len(ngrams) + i] = items1 + items2
    ngram_clusters = []
    for cluster in clusters.values():
        ngram_clusters.append([ngrams[i] for i in cluster])
    return ngram_clusters


def dl_ngram_dist(ngram1, ngram2):
    """
    Compute distance between ngrams by summing the Damerau-Levenshtein distance
    for consecutive words in ngrams.

    Params:
        ngram1: [tuple] Tuple of words.
        ngram2: [tuple] Tuple of words.

    Returns:
        distance [int] Measure of distance between two ngrams.
    """
    return sum(damerau_levenshtein_distance(w1, w2) for w1, w2 in zip(ngram1,
        ngram2))
