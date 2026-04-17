class Solution:
    def floodFill(self, image, sr, sc, color):
        starting_color = image[sr][sc]
        if starting_color == color: 
            return image
        
        def dfs(r, c):
            # Check boundaries and if current pixel matches starting color
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            if image[r][c] != starting_color:
                return
            
            # Fill color and recurse
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        dfs(sr, sc)
        return image