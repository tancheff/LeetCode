# Given a fixed-length integer array arr, duplicate each occurrence of zero,
# shifting the remaining elements to the right.
# Do not return anything, modify arr in-place instead. - this constraint makes this Q hard

arr = [1,0,2,3,0,4,5,0]
# arr = [1,2,3]
new_arr = []

for i in range(0, len(arr)):
    new_arr.append(arr[i])
    if arr[i] == 0:
        new_arr.append(0)

for i in range(0, len(new_arr) - len(arr)):
    new_arr.pop()

print(new_arr)