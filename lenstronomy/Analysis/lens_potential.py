import numpy as np
import scipy
from lenstronomy.Util import util
from lenstronomy.Util import mask_util as mask_util
import lenstronomy.Util.multi_gauss_expansion as mge
from lenstronomy.Util import analysis_util
from lenstronomy.LensModel.lens_model_extensions import LensModelExtensions
import lenstronomy.Util.constants as const

__all__ = ["LensPotentialAnalysis"]


class LensPotentialAnalysis(object):
    """Class with analysis routines to compute derived properties of the lens model."""

    def __init__(self, lens_model):
        """

        :param lens_model: LensModel instance
        """
        self._lens_model = lens_model

    def lens_potential_on_radius(
        self, kwargs_lens, center_x, center_y, theta_E, numPix=72
    ):
        """
        在半径 theta_E 的圆周上，对 ψ(θ) 做“方位角平均”（沿圆周平均）。
        返回：每个透镜分量的 <ψ>_{|θ|=theta_E}
        """
        phi = np.linspace(0.0, 2.0 * np.pi, numPix, endpoint=False)
        x = center_x + theta_E * np.cos(phi)
        y = center_y + theta_E * np.sin(phi)

        psi_list = []
        for i in range(len(kwargs_lens)):
            psi = self._lens_model.potential(x, y, kwargs_lens, k=i)
            psi_list.append(np.mean(psi))
        return psi_list

