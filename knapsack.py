def knapsack(items, n, W):
  
 
    if n == 0 or W == 0:
        return 0

    weight, value = items[n - 1]

    if weight > W:
        return knapsack(items, n - 1, W)

   
    return max(
        knapsack(items, n - 1, W), 
        value + knapsack(items, n - 1, W - weight)  
    )


if __name__ == "__main__":
   
    items = [(2, 3), (3, 4), (4, 5), (5, 8)] 
    W = 5 
    n = len(items)

    max_value = knapsack(items, n, W)
    print(f"Maximum value that can be obtained: {max_value}")
