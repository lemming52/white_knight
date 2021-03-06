CORE EXERCISE ##################################################################################

FILES

Python
diffraction.py - Master Script, only script that needs executing. Evaluates the aperture
                 and plots the patterns.
tools.py - config loading package
config_coren.json - Configuration files for the core exercises (n=1, 2)

Pictures:
config_coren.png - produced diffraction patern


RUNNING ORDER:
To regenerate results run:
diffraction.py
    specify: core1 then re-run for core2

EXTERNAL PACKAGES
numpy
matplotlib


COMMENTARY
The plot produced for core 1 shows the expected sinc relationship, so much so the predicted plot is completely overlapped by the calculated. For the second core exercise, the plot produced the sensible results, showing the regular spacing between maxima expected due to the sinusoidal variation in the aperture.


SUPPLEMENTARY
###############################################################################


FILES

Python
diffraction.py
tools.py
config_suppn.json

Pictures:
config_suppn.png


RUNNING ORDER:
To regenerate results run:
diffraction.py
    specify: supp1 then re-run for supp2

EXTERNAL PACKAGES
numpy
matplotlib


COMMENTARY
The fresnel correction was easy to slot into my existing code. The single slit pattern is reminiscent of a fresnel single slit convolved onto the finite fraunhofer slit pattern. The pattern for the sinusoidal grating shows fresnel noise convolved onto the fraunhofer diffraction pattern for the grating.

CONFIG JSON FILE
###############################################################################

{
    "width" : d,
    "distance" : D,
    "extent" : L,
    "centre" : middle of L, would be used to position the slit away from the middle
    "wavelength",
    "args" : dictionary of any variables required for the aperture function,
    "correction" : boolean for application of fresnel correction,
    "ap_func" : specify the apeture function here with string,
    "predicted" : bool - whether or not to overlay a predicted sinc function
    "lim" : plot limits
}

