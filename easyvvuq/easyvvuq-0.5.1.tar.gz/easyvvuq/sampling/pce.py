import logging
import chaospy as cp
from .base import BaseSamplingElement, Vary

__author__ = "Jalal Lakhlili"
__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "LGPL"


class PCESampler(BaseSamplingElement, sampler_name="PCE_sampler"):
    def __init__(self,
                 vary=None,
                 count=0,
                 polynomial_order=4,
                 regression=False,
                 rule="G",
                 sparse=False,
                 growth=False):
        """
        Create the sampler for the Polynomial Chaos Expansion method using
        pseudo-spectral projection.

        Parameters
        ----------
        vary: dict or None
            keys = parameters to be sampled, values = distributions.

        count : int, optional
            Specified counter for Fast forward, default is 0.

        polynomial_order : int, optional
            The polynomial order, default is 4.

        regression : bool, optional
            If True, regression variante (point collecation) will be used,
            otherwise projection variante (pseud-spectral) will be used.
            Default value is False.

        rule : char, optional
            The quadrature method, in case of projection (default is Gaussian "G").
            The sequence sampler in case of regression (default is Hammersley "M")


        sparse : bool, optional
            If True, use Smolyak sparse grid instead of normal tensor product
            grid. Default value is False.

        growth (bool, None), optional
            If True, quadrature point became nested.
        """

        if vary is None:
            msg = ("'vary' cannot be None. RandomSampler must be passed a "
                   "dict of the names of the parameters you want to vary, "
                   "and their corresponding distributions.")
            logging.error(msg)
            raise Exception(msg)
        if not isinstance(vary, dict):
            msg = ("'vary' must be a dictionary of the names of the "
                   "parameters you want to vary, and their corresponding "
                   "distributions.")
            logging.error(msg)
            raise Exception(msg)
        if len(vary) == 0:
            msg = "'vary' cannot be empty."
            logging.error(msg)
            raise Exception(msg)

        self.vary = Vary(vary)
        self.polynomial_order = polynomial_order

        # List of the probability distributions of uncertain parameters
        params_distribution = list(vary.values())

        # Multivariate distribution
        self.distribution = cp.J(*params_distribution)

        # The orthogonal polynomials corresponding to the joint distribution
        self.P = cp.orth_ttr(polynomial_order, self.distribution)

        # The quadrature information
        self.quad_order = polynomial_order + 1
        self.quad_sparse = sparse
        self.rule = rule

        # Clenshaw-Curtis should be nested if sparse (#139 chaospy issue)
        self.quad_growth = growth
        cc = ['c', 'C', 'clenshaw_curtis', 'Clenshaw_Curtis']
        if sparse and quadrature_rule in cc:
            self.quad_growth = True

        # To determinate the PCE vrainte to use
        self.regression = regression

        # Regression variante (Point collocation method)
        if regression:
            # Change the default rule
            if rule == "G":
                self.rule = "M"

            # Generates samples
            self._number_of_samples = 2 * len(self.P)
            self._nodes = cp.generate_samples(order=self._number_of_samples,
                                              domain=self.distribution,
                                              rule=self.rule)

        # Projection variante (Pseudo-spectral method)
        else:
            # Nodes and weights for the integration
            self._nodes, _ = cp.generate_quadrature(order=self.quad_order,
                                                    dist=self.distribution,
                                                    rule=self.rule,
                                                    sparse=sparse,
                                                    growth=self.quad_growth)
            # Number of samples
            self._number_of_samples = len(self._nodes[0])

        # Fast forward to specified count, if possible
        self.count = 0
        if self.count >= self._number_of_samples:
            msg = (f"Attempt to start sampler fastforwarded to count {self.count}, "
                   f"but sampler only has {self._number_of_samples} samples, therefore"
                   f"this sampler will not provide any more samples.")
            logging.warning(msg)
        else:
            for i in range(count):
                self.__next__()

    def element_version(self):
        return "0.4"

    def is_finite(self):
        return True

    def is_restartable(self):
        return True

    def __next__(self):
        if self.count < self._number_of_samples:
            run_dict = {}
            i_par = 0
            for param_name in self.vary.get_keys():
                run_dict[param_name] = self._nodes.T[self.count][i_par]
                i_par += 1
            self.count += 1
            return run_dict
        else:
            raise StopIteration

    def get_restart_dict(self):
        return {"vary": self.vary.serialize(),
                "count": self.count,
                "polynomial_order": self.polynomial_order,
                "regression": self.regression,
                "rule": self.rule,
                "sparse": self.quad_sparse,
                "growth": self.quad_growth}
