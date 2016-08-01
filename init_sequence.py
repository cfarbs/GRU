#!/usr/bin/env python
import random
import pickle

aa = ['ALA', 'CYS', 'ASP', 'GLU', 'PHE', 'GLY', 'HIS', 'ILE', 'LYS', 'LEU', 'MET', 'ASN', 'PRO', 'GLN', 'ARG', 'SER', 'THR', 'VAL', 'TRP', 'TYR']
samples = []
for i in range(10000):
    tempsamp = random.sample(aa,12)
    samples.append(tempsamp)

pickle.dump(samples,open("Init_seq.pkl","wb"))
