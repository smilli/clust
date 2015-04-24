import unittest
from clust import cluster_ngrams, dl_ngram_dist
from pyxdameraulevenshtein import damerau_levenshtein_distance

class TestCluster(unittest.TestCase):

    def test_cluster_ngrams(self):
        ngrams = [
            ['from', 'my', 'house'],
            ['from', 'my', 'hose'],
            ['he', 'was', 'eating'],
            ['she', 'was', 'eating'],
            ['fell', 'asleep', 'on'],
            ['moved', 'to', 'a'],
            ['rom', 'my', 'house'],
            ['from', 'my', 'house'],
        ]
        clusters = [[['fell', 'asleep', 'on']], [['moved', 'to', 'a']], [['he',
            'was', 'eating'], ['she', 'was', 'eating']], [['rom', 'my',
                'house'], ['from', 'my', 'hose'], ['from', 'my', 'house'],
                ['from', 'my', 'house']]]
        self.assertEqual(cluster_ngrams(ngrams, dl_ngram_dist, 3, 'single'),
            clusters)


if __name__ == '__main__':
    unittest.main()
