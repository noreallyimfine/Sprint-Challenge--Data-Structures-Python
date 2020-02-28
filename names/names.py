import time
from binary_search_tree import BinarySearchTree
start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


root = BinarySearchTree(names_1[0])
for name in names_1[1:]:
    root.insert(name)

duplicates = []
for name in names_2:
    if root.contains(name):
        duplicates.append(name)


print(len(duplicates))
end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")



## ORIGINAL SOLUTION - Runitime: O(n^2) or O(n*m) where n is length of list and m is the length of the other

print("Original code and runtime...")
start_time = time.time()
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
