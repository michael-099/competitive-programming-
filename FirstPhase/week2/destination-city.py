class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        '''
        we are going to have a dictonary to count the number of occurrence 
        and from the dictionary i thought of returning the minimum value but it will also 
        return the starting i will going to have 2 dictionaries one to store the starting city and 
        destination city after i will going to check if a the distnation city will going to be in the start city if not we will return the city but we can use set insted of dictionary 
        initializ two sets destination and start 
        use destination with out start 
        return that string
        '''
        destinations=set()
        starts=set()
        for start,destination in paths:
             destinations.add(destination)
             starts.add(start)
        result=list(destinations-starts)
        return result[0]