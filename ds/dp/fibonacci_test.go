package dp

import (
	"testing"
)

func TestFibonacci(t *testing.T) {
	assertion := func(t *testing.T, expect, got int) {
		if expect != got {
			t.Fatalf("expected %d got %d", expect, got)
		}
	}
	t.Run("test fibonacci with recursive approach only", func(t *testing.T) {
		expect := 5
		got := FibonacciRecursive(5)
		assertion(t, expect, got)
	})
	t.Run("test fibonacci with recursion and memoization", func(t *testing.T) {
		expect := 13
		got := FibRecursionWithMemoization(7)
		assertion(t, expect, got)
	})
	t.Run("fibonacci with bottom up approach", func(t *testing.T) {
		expect := 21
		got := FibonacciBottomUp(8)
		assertion(t, expect, got)
	})
	t.Run("fibonacci with bottom up approach with optimized space", func(t *testing.T) {
		expect := 21
		got := FibonacciBottomUp2(8)
		assertion(t, expect, got)
	})
}
