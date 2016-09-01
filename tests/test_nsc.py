"""
Tests for nonnegative spectral clustering
"""
import unittest
import numpy as np
from sklearn.datasets import load_iris

from nmflib.nsc import NSpecClus


class TestNSC(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        iris = load_iris()
        X, y = iris["data"], iris["target"]

        cls.X = X

    def failing_test_nsc_converge_nn(self):
        # Test that the objective function is non-increasing

        self.nsc = NSpecClus(self.X, 5, stopconv=1e-4)
        self.res = self.nsc.predict()

        cg = self.res.convgraph

        assert not np.any((np.roll(cg, 1) - cg)[3:] > 0)

    def test_nsc_converge_gauss(self):
        # Test that the objective function is non-increasing

        self.nsc = NSpecClus(self.X, 5, stopconv=1e-4, affinity="gaussian")
        self.res = self.nsc.predict()

        cg = self.res.convgraph

        assert not np.any((np.roll(cg, 1) - cg)[3:] > 0)
