import monkdata as m
import dtree as d
import drawtree_qt5 as dt
import random

monk1_nodes_lvl1 = [] # Nodes at level 1 of tree

for i in range(1, 5):
    # Splitting monk1 data using attribute 'A5' into 4 nodes each containing one possible value of 'A5'
    monk1_nodes_lvl1.append(d.select(m.monk1, m.attributes[4], i))


# Prints the information gain for the remaining 5 attribute for all 4 newly created nodes.
for i in range(0, 4):
    for j in [0, 1, 2, 3, 5]:
        print("Node ", i + 1, " expected information gain of attribute ", j + 1, ":", 
              d.averageGain(monk1_nodes_lvl1[i], m.attributes[j]))
        
monk1_nodes_lvl2 = [] # Nodes at level 2 of tree        

# Node 1 is known, no need to expand

# Expanding node 2 of level 1, using attribute 'A4' 
for i in range(1, 4):    # 'A4', (1, 2, 3)
    monk1_nodes_lvl2.append(d.select(monk1_nodes_lvl1[1], m.attributes[3], i))
    
# Expanding node 3 of level 1, using attribute 'A6' 
for i in range(1, 3):    # 'A6', (1, 2)
    monk1_nodes_lvl2.append(d.select(monk1_nodes_lvl1[2], m.attributes[5], i))
    
# Expanding node 4 of level 1, using attribute 'A1' 
for i in range(1, 4):    # 'A1', (1, 2, 3)
    monk1_nodes_lvl2.append(d.select(monk1_nodes_lvl1[3], m.attributes[0], i))
    
# Printing most common class of all leaves on level 2
for i in range(0, len(monk1_nodes_lvl2)):
    print(d.mostCommon(monk1_nodes_lvl2[i]))


# Building tree
monk1_tree = d.buildTree(m.monk1, m.attributes, 2)
monk2_tree = d.buildTree(m.monk2, m.attributes)
monk3_tree = d.buildTree(m.monk3, m.attributes)


# Drawing tree
dt.drawTree(monk1_tree)
#dt.drawTree(monk2_tree)
#dt.drawTree(monk3_tree)

# Check performance of tree on training dataset
print("MONK-1 training data performance:", d.check(monk1_tree, m.monk1))
print("MONK-2 training data performance:", d.check(monk2_tree, m.monk2))
print("MONK-3 training data performance:", d.check(monk3_tree, m.monk3))

# Check performance of tree on test dataset
print("MONK-1 test data performance:", d.check(monk1_tree, m.monk1test))
print("MONK-2 test data performance:", d.check(monk2_tree, m.monk2test))
print("MONK-3 test data performance:", d.check(monk3_tree, m.monk3test))
