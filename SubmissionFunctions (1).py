import numpy as np


def Lagrangian(c: np.ndarray, A: np.ndarray, labda: np.ndarray) -> \
        tuple[float, np.ndarray]:

    return obj_lagrange , x_lagrange


def InfeasToFeas(c: np.ndarray, A: np.ndarray, x_infeas: np.ndarray) -> \
        tuple[float, np.ndarray]:

    return obj_feas, x_feas

def UpdateLabda(A: np.ndarray, labda: float, LB: float, UB: float,
                x_lagrange: np.ndarray, rho: float):

    return labda_next

def SubgradientOpt(c: np.ndarray, A: np.ndarray,
                   labda_init: np.ndarray, rho_init: float,
                   k: int) -> tuple[float, float, np.ndarray, list, list]:


    return LB_best, UB_best, x_best, LB_list, UB_list