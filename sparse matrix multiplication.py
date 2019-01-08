class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        if not A or not A[0]:
            return None
        
        if not B or not B[0]:
            return None

        index_a = {}
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    if i in index_a:
                        index_a[i].append(j)
                    else:
                        index_a[i] = [j]

        index_b = {}
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j] != 0:
                    if j in index_b:
                        index_b[j].append(i)
                    else:
                        index_b[j] = [i]        

        C = [[0 for i in range(len(A[0]))] for j in range(len(A))]

        for a_key in range(len(C)):
            for b_key in range(len(C[0])):
                if a_key in index_a and b_key in index_b:                                  
                    list_a = index_a[a_key]
                    list_b = index_b[b_key]
                    intersec = set(list_b).intersection(list_a)
                
                    sum = 0
                    for num in intersec:
                        sum += A[a_key][num] * B[num][b_key]
                    C[a_key][b_key] = sum
                    
        for j in range(len(C[0]) - 1, -1, -1):
            delete = True
            for i in range(len(C)):
                if C[i][j] != 0:
                    delete = False
            if delete:
                for arr in C:
                    arr.pop()
            else:
                return C
        return C