GET_MIN_LOC(A,i,j,direct)
	min_x,min_y = FIND_MIN_LINE(A,i,j,direct)
	if direct == 0
		if A[min_x][min_y] < (min_x-1 < 0) ? MAX_VALUE : A[min_x-1][min_y] and A[min_x][min_y] < (min_x+1 >= A.length-1) ? MAX_VALUE : A[min_x+1][min_y]
			return A[min_x][min_y]
		else if min_x+1 >= A.length or A[min_x-1][min_y] < A[min_x+1][min_y]
			return GET_MIN_LOC(A[0:min_x,0:-1],min_x,min_y,(direct+1)%2)
		else if min_x-1 < 0 or A[min_x+1][min_y] < A[min_x-1][min_y]
			return GET_MIN_LOC(A[min_x:-1,0:-1],min_x,min_y,(direct+1)%2)
	else if direct == 1
		if A[min_x][min_y] < (min_y-1 < 0) ? MAX_VALUE : A[min_x][min_y-1] and A[min_x][min_y] < (min_y+1 > A[0].length-1) ? MAX_VALUE : A[min_x][min_y+1]
			return A[min_x][min_y]
		else if min_y+1 >= A[0].length or A[min_x][min_y-1] < A[min_x][min_y+1]
			return GET_MIN_LOC(A[0:-1,0:min_y],min_x,min_y,(direct+1)%2)
		else if min_y-1 < 0 or A[min_x][min_y+1] < A[min_x][min_y-1]
			return GET_MIN_LOC(A[0:-1,min_y:-1],min_x,min_y,(direct+1)%2)

FIND_MIN_LINE(A,i,j,direct)
	if direct == 0 //横线
		int min_j = 0
		for k = 1 to A[0].length-1
			if A[i][k] < A[i][min_j]
				min_j = k
		return i,min_j
	else if direct == 1 //竖线
		int min_i = 0
		for k = 1 to A.length-1
			if A[k][j] < A[min_i][j]
				min_i = k
		return min_i,j

先在正中间画一条横线,找到横线上最小的位置a。如果这个位置上下两个位置都比它大，那么它是局部最小。
否则上下至少有一个比这个位置小。把较大的半个矩阵舍弃，因为从a开始按贪心找局部最小值不会离开没被舍弃的半个矩阵。
接着画一条n/2长度的竖线，又把矩阵分成了两半。找到横线加竖线合起来最小的位置。用同样的方式把最小不在的半个矩阵舍弃。
这样操作下去每两次画的线长度会减半，画的线总长度是O(n)

因为每次矩阵切分的时候都会平均减去n/2的矩阵大小，所有搜索的元素大概是n+n/2+n/4+n/8+...=2n=O(n)






