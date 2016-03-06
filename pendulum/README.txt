CORE EXERCISE ##################################################################################

FILES

Python
pendulum.py - master method, solves the differential equations using odeint and stores
              the solutions, positional and energy informations in text files. Requires
              user input to select configuration and store info appropriately.
config_core.json - configuration file for the core exercise, stored in JSON format.
tools.py - useful methods, e.g. loading the json.
plot_double.py - plotting function, generates trajectories of the masses, energy variation
                 plots both zoomed and wide angle. Requires user input to select the system.
animate.py - show an animation of the trajectories. Requires user input to select system


Notes
label - The word label is used throughout, and describes the particular string for
        identifying a system, i.e. core for the core exercise.
energy - the potential energy is defined negatively

Pictures
positions_core.png - trajectories of masses
energies_core.png - fractional deviation of energy from initial against time zoomed
energies_core_wide.png - plot of energy against time zoomed out, so that the constant nature
                         is visible.

Data
double_solutions_core.txt - solutions yi of the differential equation
double_positions_core.txt - cartesian coordinates of the masses
double_energies_core.txt - kinetic and potential energies of each mass

RUNNING ORDER:
To regenerate results run:
pendulum.py
    specify: core
plot_double.py
    specify: core

EXTERNAL PACKAGES
numpy
scipy
matplotlib


COMMENTARY
Managed to solve the system of equations and generate a plot for the core exercise. While the double pendulum is typically associated with chaotic motion the initial values result in a sedate plot. The system appears correct with some minor energy variation(tends to decay) which is likely due to numerical error. However, the overall variation is negligible. The implementation is designed to be quite general, and should hopefully function easily, but requires some user input and is not sanitised.


SUPPLEMENTARY 1 ###############################################################################



SUPPLEMENTARY 2 ###############################################################################



