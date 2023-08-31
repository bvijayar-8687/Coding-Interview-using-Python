import numpy as np
import sys

def initialize_Node_Visits(rowindex,columnindex):
    for i in range(columnindex):
        for j in range(rowindex):
             point_seen[j][i] = False;

def visit_All_Edges(temp):
    for row in range(rows):
        for col in range(columns):
             if ((row * col == 0 or row == rows - 1 or col == columns - 1) and temp[row][col] == 1 and point_seen[row][col] == False):
                     search_Inside_Matrix(temp,point_seen,row,col)                      
                                   
def extract_Sub_Matrix(index,rows,columns):
    final_list = []
    temp_list = []
    for i in range (index, index+rows):
        for j in range (0, columns):
            temp_list.append(matrix[i][j])
        final_list.append(temp_list)
        temp_list = []
    return final_list


def find_Size_Of_Matrix(submatrix):
     count = 0
     matrixcount = 0
     columncount = np.full(shape=4,fill_value=0,dtype=np.int)
     for i in range(len(submatrix)):
         if(len(submatrix[i]) == 0):
              columncount[matrixcount] = count;
              matrixcount = matrixcount+1;
              count = 0;         
         else:
              count = count + 1; 
     columncount[matrixcount] = count;         
     return columncount;
        

def check_If_Node_Visited(rowIndex, columnIndex):
    if point_seen[rowIndex][columnIndex] == False:
        return False 
    return True;

def check_For_Background_Conditions(temp, rowIndex, columnIndex):
    if(rowIndex < 0 or columnIndex <0 or rowIndex >= len(temp) or columnIndex >= len(temp[0]) or temp[rowIndex][columnIndex] == 0):
        return False;
    else:
        return True;  

def search_Inside_Matrix(temp, point_seen, rowIndex, columnIndex):
    if check_For_Background_Conditions(temp, rowIndex, columnIndex) == False:
        return;
    else:
        if check_If_Node_Visited(rowIndex, columnIndex) == False:
            point_seen[rowIndex][columnIndex] = True; 
            search_Inside_Matrix(temp,point_seen,rowIndex,columnIndex+1)
            search_Inside_Matrix(temp,point_seen,rowIndex+1,columnIndex)
            search_Inside_Matrix(temp,point_seen,rowIndex+1,columnIndex+1)
            search_Inside_Matrix(temp,point_seen,rowIndex-1,columnIndex-1)
            search_Inside_Matrix(temp,point_seen,rowIndex,columnIndex-1)
            search_Inside_Matrix(temp,point_seen,rowIndex-1,columnIndex)
            search_Inside_Matrix(temp,point_seen,rowIndex-1,columnIndex+1)
            search_Inside_Matrix(temp,point_seen,rowIndex+1,columnIndex-1)


def count_Closed_Islands(temp):
    totalClosed = 0
    visit_All_Edges(temp);
    for row in range(rows):
        for col in range(columns):
            if(temp[row][col] == 1):
                 totalClosed = totalClosed + 1;
    return totalClosed;
                 

def count_Total_Islands(temp,rows,columns):
     totalIslands = 0
     for row in range(rows):
        for col in range(columns):
             if(point_seen[row][col] == False and temp[row][col] == 1):
                 totalIslands = totalIslands + 1;
                 search_Inside_Matrix(temp,point_seen,row,col)
     return totalIslands;

def count_Distinct_Islands(temp):
    visit_All_Edges(temp);
    return '';

with open("input.txt") as file:
    matrix = [list(line.strip()) for line in file]

rows = 0
columns = 0
matrixCount = 0
columncount = find_Size_Of_Matrix(matrix)
columns = len(matrix[0])
rows = int(columncount[matrixCount])
point_seen  =  [ [0]*columns for i in range(rows)]
initialize_Node_Visits(rows,columns)            
totalClosed =0
totalIslands = 0
distinctIslands = 0
iterCount = 0
sys.setrecursionlimit(2900)
for i in range(len(columncount)):
     temp = extract_Sub_Matrix(iterCount,rows,columns)
     for j in range(len(temp)):
           for k in range(len(temp[i])):
                        search_Inside_Matrix(temp,point_seen,j,k) 
     totalIslands = count_Total_Islands(temp,rows,columns)
     totalClosed = count_Closed_Islands(temp)
     distinctIslands = count_Distinct_Islands(temp)
     print('**********Printing Results for **********')
     print(matrixCount+1,'Matrix')
     print('Matrix has ',rows,'Rows and ',columns,'Columns')
     print('Matrix has values')
     print(temp)
     print('Printing the values for Total Islands', totalIslands)
     print('Printing the values for Closed Islands',totalClosed)
     print('Printing the values for Distinct Islands',distinctIslands)
     tot = len(temp)
     iterCount = iterCount+rows+1
     columns = len(matrix[tot+1])
     rows = int(columncount[matrixCount+1])
     point_seen  =  [ [0]*columns for i in range(rows)]
     initialize_Node_Visits(rows,columns)            
     matrixCount= matrixCount + 1
                    
                    