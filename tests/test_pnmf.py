import unittest
import numpy as np

from nmflib.projective import ProjectiveNMF
from nmflib.clusternmf import ClusterNMF

from sklearn.datasets import load_iris


class TestPNMF(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        iris = load_iris()
        X, y = iris["data"], iris["target"]

        cls.X = X

    def setUp(self):

        self.pnmf = ProjectiveNMF(self.X, 5, stopconv=1e-4)
        self.cvx = ClusterNMF(self.X, 5, stopconv=1e-4)
        self.res = self.pnmf.predict()
        self.cvxres = self.cvx.predict()

    def test_pnmf_converge(self):
        # Test that the objective function is non-increasing
        cg = self.res.convgraph

        assert not np.any((np.roll(cg, 1) - cg)[1:] < 0)

    def test_pnmf_objective(self):
        # Test that the objective function is calculated correctly

        W = self.res.matrices[0]

        assert np.linalg.norm(self.X -  W.dot(W.T).dot(self.X), 'fro') - self.res.objvalue < 1e-10

    def test_cvxnmf_converge(self):
        cg = self.cvxres.convgraph

        print cg
        assert not np.any((np.roll(cg, 1) - cg)[1:] < 0)
