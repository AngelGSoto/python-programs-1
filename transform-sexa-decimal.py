from __future__ import print_function, division
from PyAstronomy import pyasl
import numpy as np

list_=np.loadtxt("teste.txt",  delimiter = None, converters = None, skiprows = 0, usecols = None, unpack = False, ndmin = 0,)











# Coordinates of HD 1 from SIMBAD
hd1 = "00 05 08.83239 +67 50 24.0135"

print("Coordinates of HD 1 (SIMBAD): ", hd1)

# Obtain decimal representation
ra, dec = pyasl.coordsSexaToDeg(hd1)
print("Coordinates of HD 1 [deg]: %010.6f  %+09.6f" % (ra, dec))

# Convert back into sexagesimal representation
sexa = pyasl.coordsDegToSexa(ra, dec)
print("Coordinates of HD 1 [sexa]: ", sexa)
