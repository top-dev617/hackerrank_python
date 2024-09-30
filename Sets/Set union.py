n = int(input())  # Number of elements in the first set
l = list(input().split())  # Elements for the first set
m = int(input())  # Number of elements in the second set
k = list(input().split())  # Elements for the second set

s1 = set(l)  # Creating set from the first list
s2 = set(k)  # Creating set from the second list

print(len(s1.union(s2)))  # Printing the length of the union of the two sets
