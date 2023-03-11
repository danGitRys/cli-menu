import math
class climenu:

    def __init__(self) -> None:
        pass

    def xyMenu(self,x:int,y:int,optionList:list,collapsColumn:bool=True,collapsRow:bool=False):
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
            print(tempX)
            tempList = []
            for tempY in range(0,x):
                if titleCounter >=numberOptions:
                    tempList.append(None)
                else:
                    tempList.append(optionList[titleCounter])
                    titleCounter = titleCounter +1 
            
            titelList.append(tempList)
        
        print(titelList)


        


                

 