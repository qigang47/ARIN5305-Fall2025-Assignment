package minimumcostgoodcaption;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class HighCoverageTest {

    private final Solution solution = new Solution();

    @Test
    public void testBaseCase() {
        assertEquals("bbb", solution.minCostGoodCaption("abc"));
    }

    @Test
    public void testUniformString() {
        assertEquals("aaaaaa", solution.minCostGoodCaption("aaaaaa"));
    }

    @Test
    public void testMixedPattern() {
        assertEquals("bbbbfff", solution.minCostGoodCaption("abcdeff"));
    }

    @Test
    public void testRepeatingPattern() {
        assertEquals("yyyyyy", solution.minCostGoodCaption("xyzxyz"));
    }

    @Test
    public void testShortLengthEarlyReturn() {
        // length < 3 should trigger early return path
        assertEquals("", solution.minCostGoodCaption("ab"));
    }
}

