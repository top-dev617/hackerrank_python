if __name__ == "__main__":
    # Read input for the first set
    M = int(input())  # Size of set M
    a = set(map(int, input().split()))  # Elements of set M

    # Read input for the second set
    N = int(input())  # Size of set N
    b = set(map(int, input().split()))  # Elements of set N

    # Compute the symmetric difference
    symmetric_diff = a.symmetric_difference(b)

    # Print the sorted symmetric difference
    for num in sorted(symmetric_diff):
        print(num)
