#!/usr/bin/env python
# @Author: Adeel Ahmad

import numpy as np
import matplotlib.pyplot as plt
import csv

# Rule followed: Tile N in order K → NorderK / DirD / NpixN{.ext}
S = 9 # 512 X 512 tile size assumed 
survey = 'xmmpneb2'
survey = 'gaia'
HEALPix_cell = '44785'
order = str(int(np.floor(np.log2(int(HEALPix_cell)) - S)))
angular_resolution = None
D = str(np.around(int(HEALPix_cell), decimals=-(len(HEALPix_cell)-1)))

base_url = 'http://axel.u-strasbg.fr/HiPSCatService/I/337/'+ survey +'/Norder'+ order +'/Dir'+ D +'/Npix'+ HEALPix_cell +'.tsv'

print('Choose a library for retreiving HiPS data: \n1. URLlib\n2. Requests')
choice = input('Enter your choice: ')

if (choice is '1'):
	import urllib.request
	data = urllib.request.urlopen(base_url).read()
elif (choice is '2'):
	import requests
	data = str.encode(requests.get(base_url).text)
else:
	print('Invalid choice')

parsed_data = data.decode('utf-8')

phot_g_n_obs = []
with open('../data.tsv') as tsvfile:
	reader = csv.DictReader(tsvfile, delimiter='\t')
	for row in reader:
		phot_g_n_obs.append(int(row['phot_g_n_obs']))

# plotting
plt.title('phot_g_n_obs plot')
plt.plot(phot_g_n_obs)
plt.show()