# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
actual_list = []

value = 0
while len(original_list) < length_of_circular_linked_list and index < len(circular_linked_list):
    element = circular_linked_list[index]
    if element not in original_list:
        original_list.append(element)
    value += 1

print(len(origianl_list))
print(" ".join(str(num) for num in original_list))
