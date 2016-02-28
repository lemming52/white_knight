CORE EXERCISE ##################################################################################

FILES

Python
integration.py - evaluate the montecarlo method across a suitable range and for the particular value.
plot_monte.py - Used to plot the data.
tools.py - load method

Pictures
Values.png - Plot of the calculated values for each sample number with associated error - Generated
Errors.png - Plot of the error variation with sample number - Generated

Data
Samples.dat - Storage of values from multi_value.py - Generated

RESULTS
10^7
Value: 537.188
Error: 0.011

RUNNING ORDER:
To regenerate results run:
integration.py
plot_monte.py

EXTERNAL PACKAGES
numpy
matplotlib


COMMENTARY
Successfully managed to code a monte-carlo method and estimate a value close to the true result, with the value and error getting closer as samples increase. Restructure code from initial method to use memory intensive but rapid numpy functions. In terms of coding style, the style was more influced by generalisation and clarity rather than a quick an blunt script style program based on personal preference. However, while the final code has vestiges of generality, it is pretty specific.


SUPPLEMENTARY 1 ###############################################################################

FILES

Python
cornu.py - calculate points in cornu spiral
plot.py - contains load method
fresnel.py - evaluating fresnel integrals
plot_cornu.py - plot data

Pictures
cornu.png

Data
cornu.dat

RUN
cornu.py
plot_cornu.py

EXTERNAL PACKAGES
numpy
matplotlib
scipy

SUPPLEMENTARY 2 ###############################################################################

FILES

Python
diffraction.py - calculate complex amplitudes
plot_diffraction.py - plot results
plot.py - load method
fresnel.py - fresnel methods

Pictures
diffraction_30cm.png
diffraction_50cm.png
diffraction_100cm.png

Data
diffraction_30cm.dat
diffraction_50cm.dat
diffraction_100cm.dat

RUN
diffraction.py
plot_diffraction.py

EXTERNAL PACKAGES
numpy
matplotlib
scipy


