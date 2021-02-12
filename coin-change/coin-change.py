class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        arr = [[None for c in coins] for a in range(amount + 1)]

        n = len(coins)
        # base:
        # 1) amount = 0
        # 2) len(coins) = 1
        for c in range(n):
            arr[0][c] = 0
        for a in range(1, amount + 1):
            if a % coins[0] == 0:
                arr[a][0] = a // coins[0]
            else:
                arr[a][0] = float('inf')
        # recursive property:
        # coin_change(coins[0...i], amount)
        # = minimum of:
        # 1) coins[i] not used: coin_change(coins[0...i-1], amount) i.e. 
        # 2) coins[i] used: coin_change(coins[0...i], amount-coins[i]) + 1
        for c in range(1, n):
            for a in range(1, amount + 1):
                if a - coins[c] > -1:
                    arr[a][c] = min(arr[a][c - 1], arr[a - coins[c]][c] + 1)
                else:
                    arr[a][c] = arr[a][c - 1]

        if arr[amount][n - 1] == float('inf'):
            return -1
        return arr[amount][n - 1]