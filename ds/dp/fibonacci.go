package dp

// FibonacciRecursive solve using recursion only - No dynamic programming used
// Time Complexity: O(2^n) - there's a lot of repetition of already solved subproblems
// Space Complexity: O(2^n) - because of the stack calls
func FibonacciRecursive(n int) int {
	if n <= 2 {
		return 1
	}
	return FibonacciRecursive(n-1) + FibonacciRecursive(n-2)
}

// FibRecursionWithMemoization uses both recursion and memoization
// Time Complexity: O(n)
// Space Complexity: O(n)
func FibRecursionWithMemoization(n int) int {
	cache := map[int]int{}
	if n <= 2 {
		cache[n] = 1
	} else {
		cache[n] = FibRecursionWithMemoization(n-1) + FibRecursionWithMemoization(n-2)
	}
	return cache[n]
}

// FibonacciBottomUp bottom-up approach
// Time Complexity: O(n)
// Space Complexity: O(n) - we're using extra space for memoizing
func FibonacciBottomUp(n int) int {
	cache := map[int]int{}
	for i := 1; i <= n; i++ {
		if i <= 2 {
			cache[i] = 1
			continue
		}
		cache[i] = cache[i-1] + cache[i-2]
	}
	return cache[n]
}

// FibonacciBottomUp2 bottom up approach
// Time Complexity: O(n)
// Space Complexity: O(1) - we are only keeping trach of the last 2 answers
func FibonacciBottomUp2(n int) int {
	var first, second int
	for i := 1; i <= n; i++ {
		if i <= 2 {
			first = 1
			second = 1
			continue
		}
		temp := second
		second = first + second
		first = temp
	}
	return second
}
