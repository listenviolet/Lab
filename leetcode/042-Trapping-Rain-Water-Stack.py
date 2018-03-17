def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        stack = []
        current = 0
        n = len(height)
        while(current < n):
            print("current:", current)
            while(len(stack) and height[current] > height[stack[len(stack) - 1]]):
                top = stack.pop()
                print("top: ", top)
                if not stack: break
                distance = current - stack[len(stack) - 1]  - 1
                bounded_height = min(height[current], height[stack[len(stack) - 1]]) - height[top]
                ans += distance * bounded_height
            stack.append(current)
            current = current + 1
            print(stack)
        return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))