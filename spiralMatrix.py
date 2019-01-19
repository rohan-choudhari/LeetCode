class Solution:
    def spiralMatrix(self, mat):
        border = mat.pop(0)
        if mat:
            for i in mat:
                border.append(i.pop(-1))
        if mat:
            border+=(mat.pop(-1))[::-1]
        if mat:
            for i in mat:
                border.append(i.pop(0))
        return(border, mat)

    def main(self, mat):
        spiral = []
        while(mat):
            [border, mat] = self.spiralMatrix(mat)
            spiral+=border
        return(spiral)



leetCode = Solution()
if 0:
    mat = [[ 1, 2, 3 ], [ 4, 5, 6 ],[ 7, 8, 9 ]]
if 1:
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]]
print(leetCode.main(mat))
