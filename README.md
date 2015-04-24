# clust
Cluster ngrams in Python.  Clustering is done using [Scipy's hierarchy clustering](http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage).

# Usage

### `cluster_ngram(ngrams, compute_distance, max_dist, method)`
Returns a list of ngrams in each cluster.
- **ngrams**: [list] List of ngrams to cluster.  Ex: [['my', 'cat', 'ran'], ['i', 'like', 'trigrams']]
- **compute_distance**: [func] Distance function that takes two ngrams as input and returns the distance between them.  This package includes a function that sums the [Damerau–Levenshtein distance](https://github.com/gfairchild/pyxDamerauLevenshtein) between the words in both ngrams as `dl_ngram_dist`
- **max_dist**: [float] If the distance between two clusters is more than max_dist, then the clusters will not be merged together.
- **method**: [string] Method for clustering.  'single', 'complete', 'average', 'centroid', 'median', 'ward', or 'weighted'.  See the [Scipy docs](http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html) for details.
  
# Exmaple
    >>> from clust import cluster_ngrams, dl_ngram_dist
    >>> ngrams = [['from', 'my', 'house'],                                                  
    ...['from', 'my', 'hose'],                                                   
    ...['he', 'was', 'eating'],
    ...['she', 'was', 'eating'],
    ...['fell', 'asleep', 'on'],                                                 
    ...['moved', 'to', 'a'],
    ...['rom', 'my', 'house'],
    ...['from', 'my', 'house']]
    >>> cluster_ngrams(ngrams, dl_ngram_dist, max_dist=3, method='single')
    [[['fell', 'asleep', 'on']], 
    [['moved', 'to', 'a']], 
    [['he', 'was', 'eating'], ['she', 'was', 'eating']], 
    [['rom', 'my', 'house'], ['from', 'my', 'hose'], ['from', 'my', 'house'], ['from', 'my', 'house']]]
