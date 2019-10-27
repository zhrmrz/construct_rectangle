from math import log2
class Sol:
    def construct_rectangle(self, area):
        min=[area,1]
        n=int(log2(area))+1
        for j in range(1,n+1):
            if area%j==0:
                i=area//j
                s=i+j
                if s<sum(min):
                    min=[i,j]
                    s=0
        return min
