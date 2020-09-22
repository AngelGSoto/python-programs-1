from astropy.io import fits
import os
import glob
import json
import argparse
import matplotlib.pyplot as plt
import pandas as pd
#import StringIO
from astropy.table import Table
from astropy.io import ascii
import sys
import numpy as np

#create list with the magnitudes
fitsfile = "WD_splus_obs.fits"
hdulist= fits.open(fitsfile)

hdu = hdulist[0]
tab = hdulist[1].data

#Crearting the table
table = Table([tab['id'], tab['ra'], tab['dec'], tab["PhotoFlag"], tab['r_auto'], tab['g_auto'], tab['i_auto'], tab['z_auto'], tab['ujava_auto'], tab['f378_auto'], tab['f395_auto'], tab['f410_auto'], tab['f430_auto'], tab['f515_auto'], tab['f660_auto'], tab['f861_auto'], tab['r_aper'],  tab['g_aper'], tab['i_aper'], tab['z_aper'], tab['ujava_aper'], tab['f378_aper'], tab['f395_aper'],  tab['f410_aper'], tab['f430_aper'], tab['f515_aper'], tab['f660_aper'], tab['f861_aper'], tab['er_auto'], tab['eg_auto'], tab['ei_auto'], tab['ez_auto'], tab['eujava_auto'], tab['ef378_auto'], tab['ef395_auto'],  tab['ef410_auto'] , tab['ef430_auto'], tab['ef515_auto'], tab['ef660_auto'], tab['ef861_auto'],  tab['er_aper'], tab['eg_aper'], tab['ei_aper'], tab['ez_aper'], tab['eujava_aper'], tab['ef378_aper'], tab['ef395_aper'],  tab['ef410_aper'] , tab['ef430_aper'], tab['ef515_aper'], tab['ef660_aper'], tab['ef861_aper']], names=('id', 'RA', 'Dec', "PhotoFlag", 'rSDSS_auto', 'gSDSS_auto', 'iSDSS_auto', 'zSDSS_auto', 'uJAVA_auto', 'J0378_auto', 'J0395_auto', 'J0410_auto', 'J0430_auto', 'J0515_auto', 'J0660_auto', 'J0861_auto', 'rSDSS_ISO_GAUSS', 'gSDSS_ISO_GAUSS', 'iSDSS_ISO_GAUSS', 'zSDSS_ISO_GAUSS', 'uJAVA_ISO_GAUSS', 'J0378_ISO_GAUSS', 'J0395_ISO_GAUSS', 'J0410_ISO_GAUSS', 'J0430_ISO_GAUSS', 'J0515_ISO_GAUSS', 'J0660_ISO_GAUSS', 'J0861_ISO_GAUSS', 'rSDSS_auto_err', 'gSDSS_auto_err', 'iSDSS_auto_err', 'zSDSS_auto_err', 'uJAVA_auto_err', 'J0378_auto_err', 'J0395_auto_err', 'J0410_auto_err', 'J0430_auto_err', 'J0515_auto_err', 'J0660_auto_err', 'J0861_auto_err',  'rSDSS_ISO_GAUSS_err', 'gSDSS_ISO_GAUSS_err', 'iSDSS_ISO_GAUSS_err', 'zSDSS_ISO_GAUSS_err', 'uJAVA_ISO_GAUSS_err', 'J0378_ISO_GAUSS_err', 'J0395_ISO_GAUSS_err', 'J0410_ISO_GAUSS_err', 'J0430_ISO_GAUSS_err', 'J0515_ISO_GAUSS_err', 'J0660_ISO_GAUSS_err', 'J0861_ISO_GAUSS_err'), meta={'name': 'first table'})  

asciifile = "WD_splus_obs.tab"
table.write(asciifile, format="ascii.tab")
