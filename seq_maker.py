#!/usr/bin/env python

import csv
import itertools
import numpy as np
import nltk
import time
import sys
import operator
import io
import array
#from gen_utils import *
from datetime import datetime
from gru_theano import GRUTheano
import pickle

# Load data
#x_train, y_train, word_to_index, index_to_word = load_data(filename ="rawhelices.pkl",vocabulary_size= 24)

#model = load_model_parameters_theano("GRU-2016-07-25-15-07-24-48-128.dat.npz")

#generate_sentences(model, 1000, index_to_word, word_to_index)

test = pickle.load(open("gen_helices.pkl","rb"))
print (test)
