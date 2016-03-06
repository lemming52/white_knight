# External Packages
import numpy as np
from scipy.integrate import odeint

# Custom Packages
import tools


def double_pend(vector, t, g, m1, m2, L1, L2):
    # Collates each differential equation in a form suitable for ODEINT
    derivatives = []
    derivatives.append(dy1(vector))
    derivatives.append(dy2(vector))
    derivatives.append(dy3(vector, g, m1, m2, L1, L2))
    derivatives.append(dy4(vector, g, m1, m2, L1, L2))
    return derivatives


# Linked first order equations for the system
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

    # Split up the equations, for almost clarity
    num_a = g*(m2*C*s2-M*s1)
    num_b = S*m2*(L1*C*y3**2 + L2*y4**2)
    den = L1*(M - m2*C**2)

    return (num_a - num_b)/den


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

    # Split up these awful equations for readability
    num_a = g*M*(s2-s1*C)
    num_b = S*(M*L1*y3**2 + C*m2*L2*y4**2)  # WHY
    den = L2*(m2*C**2 - M)

    return (num_a - num_b)/den


def abbreviate(m1, m2, y1, y2):
    """
    Generate the abbreviated values used in differentials 3 and 4
    from the base variables
    """
    M = m1 + m2
    S = np.sin(y1-y2)
    C = np.cos(y1-y2)
    s1 = np.sin(y1)
    s2 = np.sin(y2)
    return M, S, C, s1, s2


def evaluate(label):
    # Run the evaluation

    # Load the configuration data
    config = tools.load_config(label)
    t = np.linspace(0, config['sim_time'], config['time_samples'])

    solution = odeint(double_pend, config['initial'], t,
                      args=(config['g'],
                            config['m1'],
                            config['m2'],
                            config['L1'],
                            config['L2'])
                      )
    positions = position(solution, config['L1'], config['L2'], t)
    energies = energy(solution, config['g'],
                      config['m1'],
                      config['m2'],
                      config['L1'],
                      config['L2'], t)

    # Insert the time column into the solution array
    sol = np.insert(solution, 0, t, axis=1)

    # Store the data using the label as an indicator
    np.savetxt('double_solutions_%s.txt' % label, sol, delimiter='\t')
    np.savetxt('double_positions_%s.txt' % label, positions, delimiter='\t')
    np.savetxt('double_energies_%s.txt' % label, energies, delimiter='\t')


def position(solution, L1, L2, t):
    # Convert the theta values into cartesian positions
    theta1 = solution[:, 0]
    theta2 = solution[:, 1]
    x1 = L1*np.sin(theta1)
    x2 = x1 + L2*np.sin(theta2)
    y1 = -L1*np.cos(theta1)
    y2 = y1 - L2*np.cos(theta2)
    # Condense the arrays into one
    return np.column_stack((t, x1, y1, x2, y2))


def energy(solution, g, m1, m2, L1, L2, t):
    # Calculate energy values at each time step
    theta1 = solution[:, 0]
    theta2 = solution[:, 1]
    v1 = solution[:, 2]
    v2 = solution[:, 3]
    Ek_1 = m1*(L1*v1)**2/2
    # UGH
    Ek_2 = m2*((L1*v1)**2 + (L2*v2)**2 + 2*L1*L2*v1*v2*np.cos(theta1-theta2))/2
    Ep_1 = -m1*g*L1*np.cos(theta1)
    Ep_2 = -m2*g*L1*np.cos(theta1) - m2*g*L2*np.cos(theta2)
    # Concatenate the arrays
    return np.column_stack((t, Ek_1, Ek_2, Ep_1, Ep_2))


def main():
    label = input('Enter config file label (e.g. core): ')
    evaluate(label)

main()
