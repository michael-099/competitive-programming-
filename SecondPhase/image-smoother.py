class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # for i in range (len(img)):
        #     img[i]=[0]+img[i]+[0]
        # zero=[0]*len(img[i])
        # img.append(zero)
        # img.insert(0,zero)
        # print(img)
        smoothd_img=[[0]*len(img[0]) for i in range (len(img))]
        for i in range(len(img)):     
             for j in range(len(img[0])):
                count=0
                Sum=0
                # Sum=(img[i][j]+img[i-1][j]+img[i][j-1]+img[i-1][j-1]+img[i+1][j]+img[i][j+1]+img[i+1][j+1]+img[i+1][j-1]+img[i-1][j+1])
                for ii in range(-1,2):
                    for jj in range(-1,2):
                        if i+ii>=0 and i+ii<= len(img)-1 and j+jj>=0 and j+jj<=len(img[0])-1:
                            count+=1
                            Sum=Sum+img[i+ii][j+jj]
                smoothd_img[i][j]=Sum//count
        return smoothd_img
        