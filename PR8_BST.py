import sys

def optimal_bst(keys, freq, n):
    cost = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        cost[i][i] = freq[i]
    
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = sys.maxsize
            
            for r in range(i, j + 1):
                c = (cost[i][r - 1] if r > i else 0) + \
                    (cost[r + 1][j] if r < j else 0) + \
                    sum(freq[i:j + 1])
                
                if c < cost[i][j]:
                    cost[i][j] = c
    
    return cost[0][n - 1]

def main():
    n = int(input("Enter number of elements: "))
    keys = list(map(int, input("Enter keys (sorted): ").split()))
    freq = list(map(float, input("Enter search probabilities: ").split()))
    
    if len(keys) != n or len(freq) != n:
        print("Error: Number of keys and probabilities must match the specified count.")
        return
    
    min_cost = optimal_bst(keys, freq, n)
    print(f"Optimal BST cost: {min_cost}")

if __name__ == "__main__":
    main()
