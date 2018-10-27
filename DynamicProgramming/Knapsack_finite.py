def knapsack(capacity, items, memo, n):
    if capacity == 0 or n < 0:
        return 0
    else:
        if capacity in memo:
            return memo[capacity]
        else:
            options = [item[0] + knapsack(capacity-item[1], items, memo, n-1) for item in items if item[1] <= capacity]
            if len(options) == 0:
                return 0
            else:
                memo[capacity] = max(options)
                return memo[capacity]

def main():
    # A single item is a value, weight tuple
    # This version assumes a finite number of items
    items = [(20, 10), (300, 15)]
    capacity = 401
    memo = {}
    ks = knapsack(capacity, items, memo, len(items)-1)
    print(ks)

if __name__ == "__main__":
    main()
