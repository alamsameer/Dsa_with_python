def subsetSums(self, arr, N):
		# code here
    def backtrack(start,path):
        res.append(sum(path))
        for i in range(start,N):
            path.append(arr[i])
            backtrack(i+1,path)
            path.pop()
    res=[]
    backtrack(0,[])
    return res