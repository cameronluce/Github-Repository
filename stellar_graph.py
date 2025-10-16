#Ensure stellar data is in the same folder as the .py or .ipynb to ensure they correctly load, regardless of location

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reads files and locally stores data
hb006 = pd.read_csv('hb0060z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')
hb010 = pd.read_csv('hb0100z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')
hb020 = pd.read_csv('hb0200z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')
ms006 = pd.read_csv('ms0060z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')
ms010 = pd.read_csv('ms0100z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')
ms020 = pd.read_csv('ms0200z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')
ms030 = pd.read_csv('ms0300z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')
ms060 = pd.read_csv('ms0600z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')
ms080 = pd.read_csv('ms0800z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')
ms100 = pd.read_csv('ms1000z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')
ms150 = pd.read_csv('ms1500z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')
ms200 = pd.read_csv('ms2000z019s.dat', sep='\s+', header = 0, on_bad_lines = 'warn')

#plots all graphs
plt.plot(hb006['logTef'], hb006['logL'])
plt.plot(hb010['logTef'], hb010['logL'])
plt.plot(hb020['logTef'], hb020['logL'])
plt.plot(ms006['logTef'], ms006['logL'])
plt.plot(ms010['logTef'], ms010['logL'])
plt.plot(ms020['logTef'], ms020['logL'])
plt.plot(ms030['logTef'], ms030['logL'])
plt.plot(ms060['logTef'], ms060['logL'])
plt.plot(ms080['logTef'], ms080['logL'])
plt.plot(ms100['logTef'], ms100['logL'])
plt.plot(ms150['logTef'], ms150['logL'])
plt.plot(ms200['logTef'], ms200['logL'])
plt.legend(['hb006', 'hb010', 'hb020', 'ms006', 'ms010', 'ms020', 'ms030', 'ms060', 'ms080', 'ms100', 'ms150', 'ms200'])
plt.title('HR Diagram (All)')
plt.xlabel('log(T$_{ef}$)')
plt.ylabel('log(L)')
plt.gca().invert_xaxis()
plt.style.use('ggplot')

#plots helium burning graphs
plt.plot(hb006['logTef'], hb006['logL'])
plt.plot(hb010['logTef'], hb010['logL'])
plt.plot(hb020['logTef'], hb020['logL'])
plt.legend(['hb006', 'hb010', 'hb020'])
plt.title('HR Diagram (hb stars only)')
plt.xlabel('log(T$_{ef}$)')
plt.ylabel('log(L)')
plt.gca().invert_xaxis()
plt.style.use('ggplot')

#plots main sequence
plt.plot(ms006['logTef'], ms006['logL'])
plt.plot(ms010['logTef'], ms010['logL'])
plt.plot(ms020['logTef'], ms020['logL'])
plt.plot(ms030['logTef'], ms030['logL'])
plt.plot(ms060['logTef'], ms060['logL'])
plt.plot(ms080['logTef'], ms080['logL'])
plt.plot(ms100['logTef'], ms100['logL'])
plt.plot(ms150['logTef'], ms150['logL'])
plt.plot(ms200['logTef'], ms200['logL'])
plt.legend(['ms006', 'ms010', 'ms020', 'ms030', 'ms060', 'ms080', 'ms100', 'ms150', 'ms200'])
plt.title('HR Diagram (Main Sequence Stars)')
plt.xlabel('log(T$_{ef}$)')
plt.ylabel('log(L)')
plt.gca().invert_xaxis()
plt.style.use('ggplot')
