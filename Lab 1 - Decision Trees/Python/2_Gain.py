import monkdata as m
import dtree as d
import drawtree_qt5 as dt
import random

for i in range(0, 6):
    print("MONK-1 expected information gain of attribute ", i + 1, ":", d.averageGain(m.monk1, m.attributes[i]))
    
for i in range(0, 6):
    print("MONK-2 expected information gain of attribute ", i + 1, ":", d.averageGain(m.monk2, m.attributes[i]))
    
for i in range(0, 6):
    print("MONK-3 expected information gain of attribute ", i + 1, ":", d.averageGain(m.monk3, m.attributes[i]))