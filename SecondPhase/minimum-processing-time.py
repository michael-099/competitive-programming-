class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
            processorTime.sort(reverse=True)
            tasks.sort()

            sum_=0
            cycle_sum=[]
            pt_index=0
            for i in range (len(tasks)):
                sum_=max(sum_,tasks[i]+processorTime[pt_index])
                
                if (i+1)%4==0 :
                    cycle_sum.append(sum_)
                    sum_=0 
                    pt_index+=1
            return max(cycle_sum)


                    
                