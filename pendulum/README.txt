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

FILES

Python
pendulum.py
config_moden.json
tools.py
plot_double.py
animate.py
normal_modes.py - plot variation of angular displacement with time and anaylse the displacement with fft to remove the frequency. Also generates the predicted values for the frequency.

Pictures
positions_moden.png
energies_moden.png
energies_moden_wide.png
angular_displacements_moden.png - Plot of variation of angular displacement with time
angular_displacements_freq_moden.png - power specrum of angular displacement ideally showing the predicted frequencies

Data
double_solutions_moden.txt
double_positions_moden.txt
double_energies_moden.txt

RUNNING ORDER:
To regenerate results run:
pendulum.py
    specify: mode1, mode2
plot_double.py
    specify: mode1, mode2
normal_modes
    specify: mode1, mode2

EXTERNAL PACKAGES
numpy
scipy
matplotlib


COMMENTARY
Methods preserved from core exercise seem to generate same results, and show the predicted in phase/ out of phase relationships for the symmetric/antisymmetric mmodes of the double pendulum. However, the frequencies do not match the predicted values, with a small discrepancy for the low frequency symmetric mode and a large discrepancy on the high frequency mode.


SUPPLEMENTARY 2 ###############################################################################



