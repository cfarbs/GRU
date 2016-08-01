#!/usr/bin/env python

import pickle

string = "ALA CYS ASP GLU PHE GY HIS ILE LYS LEU MET ASN PRO GLN ARG SER THR VAL TRP TYR"

pickle.dump(string,open("Init_seq.pkl","wb"))
