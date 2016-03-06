# External Packages
import numpy as np


def dy1(vector):
    y1, y2, y3, y4 = vector
    return y3


def dy2(vector):
    y1, y2, y3, y4 = vector
    return y4


def dy3(vector, g, m1, m2, L1, L2):
    """
    Abbreviations
    M = m0 + m1
    S = sin(y1 - y2)
    C = cos(y1 - y2)
    s1 = sin(y1)
    s2 = sin(y2)

    Equation
    y3' = g*[m2 * C * s2  -  M * s1]  -  S*m2*[L1 * y3^2 * C + L2*y4^2]
          -------------------------------------------------------------
                                L1*[M - m2*C^2]
    """
    y1, y2, y3, y4 = vector
    M, S, C, s1, s2 = abbreviate(m1, m2, y1, y2)

    num_a = g*(m2*C*s2-M*s1)
    num_b = S*m2(L1*C*y3**2 + L2*y4**2)
    den = L1*(M - m2*C**2)

    return (num_a + num_b)/den


def dy4(vector, g, m1, m2, L1, L2):
    """
    Abbreviations
    M = m0 + m1
    S = sin(y1 - y2)
    C = cos(y1 - y2)
    s1 = sin(y1)
    s2 = sin(y2)

    Equation
    y4' = g*M*[s2 - s1*C]  -  S*[M * L1 * y3^2 + C * m2 * L2 * y4^2]
          -------------------------------------------------------------
                                L2*[m2*C^2 - M]
    """
    y1, y2, y3, y4 = vector
    M, S, C, s1, s2 = abbreviate(m1, m2, y1, y2)

    num_a = g*M*(s2-s1*C)
    num_b = S*(M*L1*y3**2 + C*m2*L2*y4**2)
    den = L2*(m2*C**2 - M)

    return (num_a + num_b)/den


def abbreviate(m1, m2, y1, y2):
    M = m1 + m2
    S = np.sin(y1-y2)
    C = np.cos(y1-y2)
    s1 = np.sin(y1)
    s2 = np.cos(y2)
    return M, S, C, s1, s2

