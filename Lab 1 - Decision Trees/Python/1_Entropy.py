import monkdata as m
import dtree as d
import drawtree_qt5 as dt
import random


# Assignment 1 #
monk1_entropy = d.entropy(m.monk1)
monk2_entropy = d.entropy(m.monk2)
monk3_entropy = d.entropy(m.monk3)

print("Entropy of MONK-1: ", monk1_entropy)
print("Entropy of MONK-2: ", monk2_entropy)
print("Entropy of MONK-3: ", monk3_entropy)