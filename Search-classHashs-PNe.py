from astropy import units as u
from astropy.coordinates import SkyCoord 
import numpy as np
from astropy.io import ascii
from astropy.table import Table

obj = ascii.read("match_TileSplus-HASHPNe.txt")
#obj = ascii.read("match-JPLUSTiles-HASHPne.txt")
# mask = obj['PNstat'] == "L"

# new_table = obj[mask]

# #save new table

a=obj['PNG']
len(a)
# #ascii.write(new_table, 'match_TileSplus-HASHPNe-possible.txt')
# ascii.write(new_table, 'match-JPLUSTiles-HASHPne-likely.txt')
 

table = Table([obj['PNG'], obj['Name_2'], obj['PNstat'], obj['RAJ2000'], obj['DECJ2000']], names=('PNG','Name_2', 'PNstat', 'RAJ2000', 'DECJ2000' ), meta={'name': 'first table'})   
    
    
#Saving resultated table

asciifile = "PNe-HASH-coordinate.tab"
table.write(asciifile, format="ascii.tab")
