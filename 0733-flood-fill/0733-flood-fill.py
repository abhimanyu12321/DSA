class Solution(object):
    def dfs(self,image,sr,sc,color,curr):
        if sr<0 or sr >=len(image) or sc<0 or sc>=len(image[0]): return
        if image[sr][sc] != curr: return;
        image[sr][sc] = color
        # make recursive calls
        self.dfs(image,sr-1,sc,color,curr)
        self.dfs(image,sr+1,sc,color,curr)
        self.dfs(image,sr,sc-1,color,curr)
        self.dfs(image,sr,sc+1,color,curr)

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color: return image
        self.dfs(image,sr,sc,color,image[sr][sc])
        return image

        