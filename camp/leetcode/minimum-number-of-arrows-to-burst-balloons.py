class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        previous=points[0]
        arrows=1
        for i in range(1,len(points)):
            if previous[1]>=points[i][0]:
                previous[1]=min(previous[1],points[i][1])
            else:
                arrows+=1 
                previous=points[i]
        return arrows 





        # we need to sort the array first because it makes it easier for us to find the overlapping ones 
        # whenever we find an overlapping ballons we are not going to increase our arrow count 
        # in the case of 3 or more overlapping ballons if the last ballon overlaps with the first one(previous one) it means 
        # that it is overlapping with the ones in the middele so how can we know when we have 3 or more overapping ballons 
        # we donot update the previous ones to the next if we have found an overlapping we will going to chake for the next then 
        # now we can update it to the current
        # -----------------     a
        # -------               b
        #     ---------         c
        # for the above we will chake first a and b we found that a and b are overlapping so we do not update our a we will 
        # only have one arrow then since we find an overlapping ones we chake a with c they are also overlapping so we only
        # need one arro to brust all the 3 ballos
        # there is a catch to this what if the bigger is overlapping with the smaller and the two smaller ones are not overlapping 
        # with the bigger like:
        # --------------------- a
        # --------              b
        #               ----    c
        # if you check if the a is overlapping with b then u will find that true and you will continue to chaking a with c and you 
        # will find that they are overlpping but b and c are not overlapping do you need some kind of way to avoid this situation 
        #so when takinf the Xend value we have to take the minimum one of the two 

                 

        