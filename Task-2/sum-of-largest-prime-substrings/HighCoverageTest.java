package sumoflargestprimesubstrings;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class HighCoverageTest {

    private final Solution solution = new Solution();

    @Test
    public void testSingleDigit() {
        assertEquals(2L, solution.sumOfLargestPrimes("2"));
    }

    @Test
    public void testTwoDigits() {
        assertEquals(28L, solution.sumOfLargestPrimes("23"));
    }

    @Test
    public void testMixedDigits() {
        assertEquals(1883L, solution.sumOfLargestPrimes("11373"));
    }

    @Test
    public void testZerosAndPrimes() {
        assertEquals(1127L, solution.sumOfLargestPrimes("1013"));
    }

    @Test
    public void testRepeatedEvenWithSinglePrime() {
        assertEquals(2L, solution.sumOfLargestPrimes("222222"));
    }
}

