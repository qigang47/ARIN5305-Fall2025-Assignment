package countthenumberofspecialcharactersii;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class HighCoverageTest {

    private final Solution solution = new Solution();

    @Test
    public void testLowerBeforeUpper() {
        assertEquals(1, solution.numberOfSpecialChars("bB"));
    }

    @Test
    public void testUpperBeforeLower() {
        assertEquals(0, solution.numberOfSpecialChars("Bb"));
    }

    @Test
    public void testMultipleSpecial() {
        assertEquals(3, solution.numberOfSpecialChars("bbBcCdD"));
    }

    @Test
    public void testAlternating() {
        assertEquals(2, solution.numberOfSpecialChars("cdDC"));
    }

    @Test
    public void testRepeatedBlocks() {
        assertEquals(2, solution.numberOfSpecialChars("ccddCCDD"));
    }
}

