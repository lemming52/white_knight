CORE EXERCISE ##################################################################################

FILES

Python
integration.py - Package of all functions used.
single_value.py - Used to calulate a value for a single number of Samples.
multi_value.py - Used to calculate values for a range of samples.
plot.py - Used to plot the data.

Pictures
Values.png - Plot of the calculated values for each sample number with associated error - Generated
Errors.png - Plot of the error variation with sample number - Generated

Data
Samples.dat - Storage of values from multi_value.py - Generated

RESULTS
10^7
Value: 537.185
Error: 0.010

RUNNING ORDER:
To regenerate results run:
multi_value.py
plot.py

REQUIREMENTS
python==3.5.1
numpy==1.10.1
matplotlib==1.5.0

COMMENTARY
Successfully managed to code a monte-carlo method and estimate a value close to the true result, with the value and error getting closer as samples increase. Runtime is rather long however. In terms of coding style, the style was more influced by generalisation and clarity rather than a quick an blunt script style program based on personal preference. However, while the final code has vestiges of generality, it is pretty specific.


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

REQUIREMENTS
python==3.5.1
numpy==1.10.1
matplotlib==1.5.0
scipy==0.16.0

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

REQUIREMENTS
python==3.5.1
numpy==1.10.1
matplotlib==1.5.0
scipy==0.16.0

