import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

class Solution {
    public long sumOfLargestPrimes(String s) {
        Set<Long> primes = new HashSet<>();
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                String substring = s.substring(i, j);
                if (substring.length() > 0) {
                    try {
                        long num = Long.parseLong(substring);
                        if (isPrime(num)) {
                            primes.add(num);
                        }
                    } catch (NumberFormatException e) {
                        // Handle numbers that are too large for long (though problem says digit string)
                        // In practice, according to constraints, perhaps this won't be triggered
                        continue;
                    }
                }
            }
        }
        
        if (primes.size() < 3) {
            long sum = 0;
            for (long prime : primes) {
                sum += prime;
            }
            return sum;
        } else {
            TreeSet<Long> sortedPrimes = new TreeSet<>(primes);
            long sum = 0;
            for (int i = 0; i < 3; i++) {
                sum += sortedPrimes.pollLast();
            }
            return sum;
        }
    }
    
    private boolean isPrime(long num) {
        if (num <= 1) {
            return false;
        }
        if (num == 2 || num == 3) {
            return true;
        }
        if (num % 2 == 0) {
            return false;
        }
        long sqrtNum = (long) Math.sqrt(num) + 1;
        for (long i = 3; i <= sqrtNum; i += 2) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}