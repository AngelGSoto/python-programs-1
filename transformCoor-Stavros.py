from astropy import units as u
from astropy.coordinates import SkyCoord 
import numpy as np
from astropy.io import ascii

#two files for the coordinates of fields observed in the survey (ra and dec). 
splusra=ascii.read("ra.txt")  
splusdec=ascii.read("dec.txt")  
#two files for the sources. in this case symbiotic
# stara=ascii.read("SyStCatra.txt")  
# stadec=ascii.read("SyStCatdec.txt")
##two files for the sources. in this case halo PNE
stara=ascii.read("ra-pne-HASH.txt")  
stadec=ascii.read("dec-pne-HASH.txt")

for i in range(0,len(splusra)):
    print i,"No"
    for j in range(0,len(stara)):
        a1=stara[i]
        b1=stadec[i]
        a2=splusra[j]
        b2=splusdec[j]
        c1 = SkyCoord(a1,b1, unit=(u.hourangle, u.deg))
        c2 = SkyCoord(a2,b2, unit=(u.hourangle, u.deg))
        if np.sqrt((c1.ra.degree-c2.ra.degree)*(c1.ra.degree-c2.ra.degree)+(c1.dec.degree-c2.dec.degree)*(c1.dec.degree-c2.dec.degree))<1.0:
            print c1.ra.degree, c1.dec.degree ,i, "No", "S-PLUS"
            print a1
            print b1
            print "##########################"
            print c2.ra.degree, c2.dec.degree,j, "No", "Obj"
            print a2
            print b2
            print np.sqrt((c1.ra.degree-c2.ra.degree)*(c1.ra.degree-c2.ra.degree)+(c1.dec.degree-c2.dec.degree)*(c1.dec.degree-c2.dec.degree))
            print "--------------------------"
