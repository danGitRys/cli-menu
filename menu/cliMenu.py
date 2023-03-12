import math
import time
import os 
import keyboard
clear = lambda: os.system('cls')

def printSeperationLine(numberColums:int,columnWidth:int)->None:
    """_summary_

    Args:
        numberColums (int): _description_
        columnWidth (int): _description_
    """
    line = "+"
    for i in range(0,numberColums):
        for k in range(0,columnWidth):
            line = line +"-"
        line = line +  "+"
    print(line)


def printMenu(optionlist:list,numberColums:int,numberRows:int,longestOption:int,pointerPosition:list,selectedList:list, markerSign:chr = '*')->None:
    """_summary_

    Args:
        optionlist (list): _description_
        numberColums (int): _description_
        numberRows (int): _description_
        longestOption (int): _description_
        pointerPosition (list): _description_
        selectedList (list): _description_
        markerSign (chr, optional): _description_. Defaults to '*'.
    """
    columnwidth = longestOption+8
    
    printSeperationLine(numberColums,columnwidth)
    for i in range(0,numberRows):
        tempLine = "|"
        tempRowOptions = optionlist[i]

        for k in range(0,numberColums):
            tempOption = tempRowOptions[k]
            if tempOption != None:
                tempOptionLength = len(tempOption)
            else:
                tempOptionLength=0

            currentCoord = [k,i]
            pre = ''
            suf = ''
            con = ' '
            if currentCoord==pointerPosition:
                pre = '\x1b[6;30;42m'
                suf = '\x1b[0m'
            
            if currentCoord in selectedList:
                con=markerSign

            tempLine = tempLine + pre + " ["+con+"] "+suf

            if tempOption != None:
                tempLine = tempLine + str(tempOption)
            tempDiff = (longestOption-tempOptionLength) + 3
            tempLine = tempLine +  ' '*tempDiff
            tempLine = tempLine + "|"
        
       
        print(tempLine)
        printSeperationLine(numberColums,columnwidth)
       
    

    




class climenu:

    def __init__(self) -> None:
        pass

    def xyMenu(self,x:int,y:int,optionList:list,collapsColumn:bool=True,collapsRow:bool=False,multiselect:bool=False,markerSign:chr="*"):
        """_summary_

        Args:
            x (int): _description_
            y (int): _description_
            optionList (list): _description_
            collapsColumn (bool, optional): _description_. Defaults to True.
            collapsRow (bool, optional): _description_. Defaults to False.
            multiselect (bool, optional): _description_. Defaults to False.
            markerSign (chr, optional): Character to show which option/s. Defaults to *

        Returns:
            selection(list): Returns the List of the selected options
        """
        numberOptions = len(optionList)
        if numberOptions == 0:
            return None
        
        orgSizeGrid = x*y 

        #get the longest title of an option
        longestTitle = 0
        for tempOption in optionList:
            tempLength = len(tempOption)
            if tempLength>longestTitle:
                longestTitle = tempLength

        #if the Grid size is larger then need, check if the table size could be reduced

        if numberOptions < orgSizeGrid:
            diff = orgSizeGrid - numberOptions
           
            # calculate what could be reduced
            rowReducable = math.floor(diff/x)
            columnReducable = math.floor(diff/y)

            if collapsColumn==True and collapsRow==False:
                x = x - columnReducable
            
            if collapsColumn==False and collapsRow==True:
                y = y- rowReducable
            
            if collapsColumn==True and collapsRow==True:
                x= x- columnReducable
                tempGridSize = x*y
                if tempGridSize>numberOptions:
                    diff = tempGridSize-numberOptions
                    rowReducable_It2 = math.floor(diff/x)
                    y= y -rowReducable_It2
        
        if numberOptions > orgSizeGrid:
            diff = numberOptions - orgSizeGrid
            newRows = math.ceil(diff/x)
            y = y + newRows
        
        #Arrange the titles into an two dimensional array
        titleCounter = 0
        titelList = []

        for tempX in range(0,y):
          
            tempList = []
            for tempY in range(0,x):
                if titleCounter >=numberOptions:
                    tempList.append(None)
                else:
                    tempList.append(optionList[titleCounter])
                    titleCounter = titleCounter +1 
            
            titelList.append(tempList)
        
        #print(titelList)
        pointerStartPosition = [0,0]
        runCondition = True
        selectedList:list = []
        while runCondition:
            printMenu(titelList,x,y,longestTitle,pointerStartPosition,selectedList,markerSign)
            keyboard.read_key()
            if keyboard.is_pressed("right") and pointerStartPosition[0]<x-1:
                pointerStartPosition[0] = int(pointerStartPosition[0])+1
               

            if keyboard.is_pressed("left") and pointerStartPosition[0]>0:
                pointerStartPosition[0] = int(pointerStartPosition[0])-1
            
            if keyboard.is_pressed("Down") and pointerStartPosition[1]<y-1:
                pointerStartPosition[1] = int(pointerStartPosition[1])+1
                
            if keyboard.is_pressed("up") and pointerStartPosition[1]>0:
                pointerStartPosition[1] = int(pointerStartPosition[1])-1
            
            if keyboard.is_pressed("space"):
                if multiselect==False:
                    selectedList.clear()
                    currentPosition = pointerStartPosition
                    xcurrentPosition = currentPosition[0]
                    ycurrentPosition = currentPosition[1]

                    if [xcurrentPosition,ycurrentPosition] in selectedList:
                        selectedList.remove([xcurrentPosition,ycurrentPosition])
                    else:
                        selectedList.append([xcurrentPosition,ycurrentPosition])
                
                elif multiselect==True:
                    currentPosition = pointerStartPosition
                    xcurrentPosition = currentPosition[0]
                    ycurrentPosition = currentPosition[1]
                    if [xcurrentPosition,ycurrentPosition] in selectedList:
                        selectedList.remove([xcurrentPosition,ycurrentPosition])
                    else:
                        selectedList.append([xcurrentPosition,ycurrentPosition])

            if keyboard.is_pressed("enter"):
                nameList = []
                if len(selectedList) == 0:
                    return nameList
                else:
                    for selected in selectedList:
                        selectedX = selected[0]
                        selectedY = selected[1]
                        selectedOption = titelList[selectedY][selectedX]
                        if selectedOption != None:
                            nameList.append(selectedOption)
                clear()
                return nameList
            
            clear()

        


                
#printSeperationLine(4,10)
 