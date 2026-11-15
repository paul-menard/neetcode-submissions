class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [(position[i], speed[i]) for i in range(len(position))]
        fleets.sort(reverse = True, key=lambda x : x[0])
        stack = [fleets[0]]
        for fleet in fleets[1:]:
            ## does the latest on the stack catch the car in front ?
            if stack and (target - stack[-1][0])/stack[-1][1] < (target - fleet[0])/fleet[1]:
                stack.append(fleet)
        return len(stack)

