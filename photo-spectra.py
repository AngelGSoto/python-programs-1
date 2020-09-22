'''
Make photo spectra
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
#import seaborn as sns
import sys
import os

X_h4 = []
X_p35 = []
err_zp_h4 = [0.128,  0.020,  0.061,  0.029,  0.067,  0.036,  0.044,  0.042, 0.043,  0.048,  0.030, 0.092]
err_zp_pn135 =[ 0.102, 0.0,  0.115,  0.103,  0.127, 0.073,  0.073,  0.073, 0.078,  0.071,  0.070,  0.100]
filters = []
S_h41 = []
S_135 = []
filter_name = ['uJAVA', 'J0378', 'J0395', 'J0410', 'J0430', 'gSDSS', 'J0515', 'rSDSS', 'J0660', 'iSDSS', 'J0861', 'zSDSS']
for a in range(1, 13):
    filters.append(a)

wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color= ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"]

# The PNe H4 1
pattern = "JPLUS-data/H4-1-phot/*6pix.json"
file_list = glob.glob(pattern)
for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)  
    X_h4.append(data["J0348_uJAVA"]-25+20.955)
    X_h4.append(data["J0378"]-25+20.361)
    X_h4.append(data["J0395"]-25+20.094)
    X_h4.append(data["J0410"]-25+20.971)
    X_h4.append(data["J0430"]-25+21.079)
    X_h4.append(data["J0480_gSDSS"]-25+23.297)
    X_h4.append(data["J0515"]-25+21.193)
    X_h4.append(data["J0625_rSDSS"]-25+23.335)
    X_h4.append(data["J0660"]-25+20.859)
    X_h4.append(data["J0766_iSDSS"]-25+23.122)
    X_h4.append(data["J0861"]-25+21.410)
    X_h4.append(data["J0911_zSDSS"]-25+22.562)
#error propagation
err_h41 = []
for i in err_zp_h4:
    err_h4 = np.sqrt(i**2)
    err_h41.append(err_h4)
#print(err_h41)

## PNG 135
pattern1 = "JPLUS-data/PNG135coadded-phot/*6pix.json"
file_list1 = glob.glob(pattern1)
for file_name1 in file_list1:
    with open(file_name1) as f1:
        data = json.load(f1)  
    X_p35.append(data["J0348_uJAVA"]-25+20.996)
    X_p35.append(data["J0378"]-25+20.376)
    X_p35.append(data["J0395"]-25+20.130)
    X_p35.append(data["J0410"]-25+21.102)
    X_p35.append(data["J0430"]-25+21.218)
    X_p35.append(data["J0480_gSDSS"]-25+23.425)
    X_p35.append(data["J0515"]-25+21.444)
    X_p35.append(data["J0625_rSDSS"]-25+23.565)
    X_p35.append(data["J0660"]-25+21.058)
    X_p35.append(data["J0766_iSDSS"]-25+23.255)
    X_p35.append(data["J0861"]-25+21.534)
    X_p35.append(data["J0911_zSDSS"]-25+22.535)

#error propagation
err_pn135 = []
for i in err_zp_pn135:
    err_pn13 = np.sqrt(i**2)
    err_pn135.append(err_pn13)
#print(err_h41)

#########################################################
#Synthetic                                              #
#########################################################
File = "Halo-PNe-spectros/H41-HPNe--JPLUS17-magnitude.json"
with open(File) as f2:
    data2 = json.load(f2)  
    S_h41.append(data2["F348"])
    S_h41.append(data2["F378"])
    S_h41.append(data2["F395"])
    S_h41.append(data2["F410"])
    S_h41.append(data2["F430"])
    S_h41.append(data2["F480_g_sdss"])
    S_h41.append(data2["F515"])
    S_h41.append(data2["F625_r_sdss"])
    S_h41.append(data2["F660"])
    S_h41.append(data2["F766_i_sdss"])
    S_h41.append(data2["F861"])
    S_h41.append(data2["F911_z_sdss"])

File_135 = "Halo-PNe-spectros/spec-0953-52411-0160_PNG_1359559-HPNe-JPLUS17-magnitude.json"
with open(File_135) as f3:
    data3 = json.load(f3)  
    S_135.append(data3["F348"])
    S_135.append(data3["F378"])
    S_135.append(data3["F395"])
    S_135.append(data3["F410"])
    S_135.append(data3["F430"])
    S_135.append(data3["F480_g_sdss"])
    S_135.append(data3["F515"])
    S_135.append(data3["F625_r_sdss"])
    S_135.append(data3["F660"])
    S_135.append(data3["F766_i_sdss"])
    S_135.append(data3["F861"])
    S_135.append(data3["F911_z_sdss"])

#############################
#Plot Obser vs Synth        #
#############################
fig = plt.figure(figsize=(8, 6.8))
ax = fig.add_subplot(1,1,1)
plt.tick_params(axis='x', labelsize=25) 
plt.tick_params(axis='y', labelsize=25)
ax.set_xlim(13,18)
ax.set_ylim(13,18)
    #ax1.set_ylim(ymin=15,ymax=-5)
    #ax1.set_xlabel(r'$\lambda$')
ax.set_xlabel(r'Mag [AB] (Synth.)', size = 33)
ax.set_ylabel(r'Mag [AB] (Obs.)', size = 33)
for X_h44, S_h411, err_h411, colors, marker_ in zip(X_h4, S_h41, err_h41, color, marker):
    ax.scatter(X_h44, S_h411, color = colors, marker=marker_, s=70, zorder=3)
    ax.errorbar(X_h44, S_h411, yerr=err_h411, marker='.', fmt='.', color=colors, ecolor=colors, elinewidth=1.9, markeredgewidth=1.2, capsize=7)

x=np.linspace(10, 20)
ax.plot(x,x, ':k')
    
plt.text(0.05, 0.90, 'H 4-1',
         transform=ax.transAxes, fontsize=31)
#plt.margins(0.06)
plt.subplots_adjust(bottom=0.19)
save_path = '../../Dropbox/JPAS/Tesis/Fig'
plotfile = "relation-h41.pdf"
file_save = os.path.join(save_path, plotfile)
#plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(file_save)
plt.clf()
#----------------------------------------------------------------
fig = plt.figure(figsize=(8, 6.8))
ax = fig.add_subplot(1,1,1)
plt.tick_params(axis='x', labelsize=25) 
plt.tick_params(axis='y', labelsize=25)
ax.set_xlim(16.5,19.2)
ax.set_ylim(16.5,19.2)
    #ax1.set_ylim(ymin=15,ymax=-5)
    #ax1.set_xlabel(r'$\lambda$')
ax.set_xlabel(r'Mag [AB] (Synth.)', size = 33)
ax.set_ylabel(r'Mag [AB] (Obs.)', size = 33)
for X_p355, S_1355, err_zp_pn1355, colors, marker_ in zip(X_p35, S_135, err_zp_pn135, color, marker):
    ax.scatter(X_p355, S_1355, color = colors, marker=marker_, s=70, zorder=3)
    ax.errorbar(X_p355, S_1355, yerr=err_zp_pn1355, marker='.', fmt='.', color=colors, ecolor=colors, elinewidth=1.9, markeredgewidth=1.2, capsize=7)

x=np.linspace(10, 20)
ax.plot(x,x, ':k')
    
plt.text(0.05, 0.90, 'PNG 135.9+55.9',
         transform=ax.transAxes, fontsize=31)
#plt.margins(0.06)
plt.subplots_adjust(bottom=0.19)
save_path = '../../Dropbox/JPAS/Tesis/Fig'
plotfile = "relation-235.pdf"
file_save = os.path.join(save_path, plotfile)
#plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(file_save)
plt.clf()
#################################################################################################################3
plotfile = "photo-spectra-h4-1.pdf"
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(1,1,1)
plt.tick_params(axis='x', labelsize=21) 
plt.tick_params(axis='y', labelsize=21)
ax.set_xlim(xmin=0,xmax=13)
    #ax1.set_ylim(ymin=15,ymax=-5)
    #ax1.set_xlabel(r'$\lambda$')
ax.set_xlabel(r'Filters', size = 21)
ax.set_ylabel(r'Magnitude [AB]', size = 21)
ax.plot(filters, X_h4, 'ko-')
ax.errorbar(filters, X_h4, yerr=err_h41, marker='o', fmt='ko', elinewidth=1.2, markeredgewidth=1.2, markersize=8,)
plt.xticks(filters, filter_name, rotation=45)
plt.text(0.05, 0.90, 'J-PLUS PN H 4-1',
         transform=ax.transAxes, fontsize=21)
#plt.margins(0.06)
plt.subplots_adjust(bottom=0.19)
#plt.gca().invert_yaxis()
plt.savefig(plotfile)

plotfile = "photo-spectra-png135.jpg"
fig = plt.figure(figsize=(12, 7))
ax1 = fig.add_subplot(1,1,1)
plt.tick_params(axis='x', labelsize=21) 
plt.tick_params(axis='y', labelsize=21)
ax1.set_xlim(xmin=0,xmax=13)
    #ax1.set_ylim(ymin=15,ymax=-5)
    #ax1.set_xlabel(r'$\lambda$')
ax1.set_xlabel(r'Filters', size = 21)
ax1.set_ylabel(r'Magnitude [AB]', size = 21)
ax1.plot(filters, X_p35, 'ko-')
ax1.errorbar(filters, X_p35, yerr=err_pn135, marker='o', fmt='ko', elinewidth=1.2, markeredgewidth=1.2, markersize=8,)
plt.xticks(filters, filter_name, rotation=45)
#plt.xticks(filters)
    #ax1.plot(Wavesengthh, Fluxx, 'k-')
    #ax1.grid(True)
    #plt.xticks(f.filteravgwls, np.unique(f.filterset['ID_filter']), 
                              #rotation='vertical', size = 'small')
#plt.margins(0.06)
plt.subplots_adjust(bottom=0.19)
#plt.gca().invert_yaxis()
plt.savefig(plotfile)
plt.clf()

########################
#Create to ASCII file ##
########################
sys.exit()
asciifile = "photo-spectra-h4-1.dat"
file=open(asciifile,'w') #create file
file.write("#Filter mag\n")# err_mag\n")
for name, x in zip(filter_name, X_h4):#,err_h41):  
    file.write('%s %f\n'%(name, x))     #assume you separate columns by tabs
file.close()     #close file  

asciifile = "photo-spectra-png135.dat"
file=open(asciifile,'w') #create file
file.write("#Filter mag\n")# err_mag\n")
for name, x in zip(filter_name, X_p35):#, #err_pn135):  
    file.write('%s %f\n'%(name, x))     #assume you separate columns by tabs
file.close()     #close file  

