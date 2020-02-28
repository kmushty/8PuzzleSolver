#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np

class EightPuzzle: 
    
    #creating the initialization of objects that define the indeces

    def __init__(self, node_state_i, node_index_i, parent_node_index_i, move, param):
        self.node_state_i = node_state_i
        self.node_index_i = node_index_i
        self.parent_node_index_i = parent_node_index_i
        self.move = move
        self.param = param
        
def TakeInput():
    
    #Taking the inputs from the user for the values
    
    print("input values between 0 and 8 without repetition")
    numbers = []
    while i<9 and i>=0:
        temp = int(input("input value " + str(i)))
        numbers.append(temp)
        i += 1
    return np.reshape(numbers,(3,3)) # converting the input values to form an array

def BlankTileLocation(numbers):

    #Checking the location of the blank tile. In this case the tile with value 0

    node_check = np.reshape(numbers, 9)
    new_node = np.copy(node_check)
    index_blank = np.where(node_check == 0)
    return int(index_blank)

def SolvabilityCondition(numbers):
    
    #checking if the input conditions will give a value that is solvable
    
    check = np.reshape(numbers, 9)
    temp = 0
    for i in range(9):
        if not check[i] == 0:
            verify = check[i]
            for j in range(1 + i, 9):
                if check[j] == 0 or verify < check[j]:
                    continue
                else:
                    temp = temp + 1
    if temp % 2 != 0: 
        
        #checking for an even value to erify if the puzzle is solvable
        
        print("The puzzle cannot be solved")
    else:
        print("The puzzle is solvable, generating solution. Please wait!")

def ActionMoveRight(node_index_i):
    #Moving the empty tile to the right
    
    i, j = BlankTileLocation(node_index_i)
    if j == 2:
        return 0
    else:
        #Performing the swap to the right of the empty tile
        final = np.copy(node_index_i)
        temp = final[i, j + 1]
        final[i, j] = temp
        final[i, j + 1] = 0
        return final  
    
def ActionMoveLeft(node_index_i):
    #Moving the empty tile to the left
    
    i, j = BlankTileLocation(node_index_i)
    if j == 0:
        return 0
    else:
        #Performing the swap to the left of the empty tile
        
        final = np.copy(node_index_i)
        temp = final[i, j - 1]
        final[i, j] = temp
        final[i, j - 1] = 0
        return final  
    
def ActionMoveUp(node_index_i):
    
    #Moving the empty tile to the top
    
    i, j = BlankTileLocation(node_index_i)
    if i == 0:
        return 0
    else:
        #Performing the swap to the top of the empty tile
        
        final = np.copy(node_index_i)
        temp = final[i - 1, j]
        final[i, j] = temp
        final[i - 1, j] = 0
        return final  
    
def ActionMoveDown(node_index_i):
    
    #Moving the empty tile to the bottom
    
    i, j = BlankTileLocation(node_index_i)
    if i == 2:
        return 0
    else:
        #Performing the swap to the bottom of the empty tile
        
        final = np.copy(node_index_i)
        temp = final[i + 1, j]
        final[i, j] = temp
        final[i + 1, j] = 0
        return final
    
def MoveTile(move, node_index_i):
    #Defining the movement parameter for each motion
    if move == 'up': 
        return ActionMoveUp(node_index_i)
    if move == 'down':
        return ActionMoveDown(node_index_i)
    if move == 'left':
        return ActionMoveLeft(node_index_i)
    if move == 'right':
        return ActionMoveRight(node_index_i)
    else:
        return None
    

def PathDef(path):  
    
    # Writing the final path in the text file
    
    
    if os.path.exists("Path_file.txt"):
        os.remove("Path_file.txt")

    f = open("Path_file.txt", "a")
    for node in path:
        if node.parent is not None:
            f.write(str(node.node_no) + "\t" + str(node.parent.node_no) + "\t" + str(node.param) + "\n")
    f.close()
    
def PrintNodes(val):  
    
    # Printing the final values
    
    for i in val:
        print("Move : " + "\n" + str(i.move)
        print("Result : " + "\n" + str(i.data)) 
        print("Node : "  + "\n" + str(i.node_no))


def NodeWrite(k):  # all the states created to a text file

    temp = open("Nodes.txt", "w")
    for obj in k:
        for i in range(len(obj)):
            for j in range(len(obj)):
                temp.write(str(obj[j][i]) + " ")
        temp.write("\n")
    temp.close()
    
    
def NodeCompleted(finish):  # writing all the nodes explored 
    if os.path.exists("Nodes_info.txt"):
        os.remove("Nodes_info.txt")

    f = open("Nodes.txt", "a")
    for test in finish:
        f.write('[')
        for i in range(len(test)):
            for j in range(len(test)):
                f.write(str(test[j][i]) + " ")
        f.write(']')
        f.write("\n")
    f.close()

def SearchAlgo():
    
    #writing the logic for the search algorithm
    
    parent_nodes = []
    parent_nodes.append(node)

    goal_node = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]) #defining the goal node
    move = ['up', 'down', 'left', 'right'] 
    relative_nodes = [] 
    node_count = 0
    checked_nodes = []
    
    checked_nodes.append(parent_nodes[0].node_index_i.tolist()) #adding the previously obtained node to the list

    while parent_nodes:   
        
        #creating the loop to move the tiles in order to check for goal node
        
        temp_nodes = parent_nodes.pop(0)

        if temp_nodes.node_index_i.tolist() == goal_node.tolist():
            return temp_nodes, relative_nodes, checked_nodes 

        for move in MoveTile:
            explorer_temp_node, param = ActionMove(move, temp_nodes.node_index_i) #performing the swapping of tiles using defined move parameters

            if (explorer_temp_node != None) and (explorer_temp_node.tolist() != temp_nodes.child_node.tolist()):
                node_count += 1
                child_node = EightPuzzle(param, node_count, np.array(explorer_temp_node), temp_nodes)
                relative_nodes.append(child_node)

                if not (child_node.node_index_i.tolist() in checked_nodes): #check if node has been achieved priously
                    parent_nodes.append(child_node)
                    checked_nodes.append(child_node.node_index_i.tolist())
                    
                    if child_node.node_index_i.tolist() == goal_node.tolist(): #check if current outout node is goal node
                        return child_node, relative_nodes, checked_nodes 
                    
def main():
    
    m = numbers()
    SolvabilityCondition(m)

    x = EightPuzzle(0, m, None, None, 0)
    
    p, q, r = exploring_nodes(x)

    if p is None and q is None and r is None:
        print("Goal not reached")
    else:
        # Print and write the final output
        PathDef(path(p))
        PrintNodes(path(p))
        NodeWrite(r)
        NodeCompleted(q)



