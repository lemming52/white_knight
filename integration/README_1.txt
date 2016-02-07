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
Successfully managed to code a monte-carlo method and estimate a value close to the true result. Runtime is rather long however. In terms of coding style, the style was more influced by generalisation and clarity rather than a quick an blunt script style program based on personal preference. However, while the final code has vestiges of generality, it is pretty specific.




