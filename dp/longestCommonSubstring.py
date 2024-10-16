def findLength(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # table = [[0, 0, 0, 0, 0],
        #          [0, 0, 0, 0, 0],
        #          [0, 0, 0, 0, 0],
        #          [0, 0, 0, 0, 0],
        #          [0, 0, 0, 0, 0]]
        rows = len(nums1) # Number of rows
        cols = len(nums2)  # Number of columns

        # Create a 2D array filled with zeros
        table = []
        for i in range(rows):
            table.append([0] * cols)

        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j]:
                    if j == 0:
                        table[i][j] = 1
                    else:    
                        table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = 0
        print(max(table[len(nums2)-1]), table)
        
findLength([0,0,0,0,1], [1,0,0,0,0])
