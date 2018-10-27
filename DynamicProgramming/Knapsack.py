def knapsack(capacity, items, memo):
    if capacity == 0:
        return 0
    else:
        if capacity in memo:
            return memo[capacity]
        else:
            options = [item[0] + knapsack(capacity-item[1], items, memo) for item in items if item[1] <= capacity]
            if len(options) == 0:
                return 0
            else:
                memo[capacity] = max(options)
                return memo[capacity]

def main():
    # A single item is a value, weight tuple
    # This version assumes there is an infinite amount of these items
    items = [(20, 1), (300, 2)]
    capacity = 401
    memo = {}
    ks = knapsack(capacity, items, memo)
    print(ks)

if __name__ == "__main__":
    main()
