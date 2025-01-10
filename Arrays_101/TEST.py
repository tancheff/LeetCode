from root_equals_sum_of_children import solution


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_arr = []

        for i in range(0, len(arr)):
            new_arr.append(arr[i])
            if arr[i] == 0:
                new_arr.append(0)

        for i in range(0, len(new_arr) - len(arr)):
            new_arr.pop()

        return new_arr

