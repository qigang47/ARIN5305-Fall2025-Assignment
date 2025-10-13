package basiccalculator;


import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class HighCoverageTest {

    private final Solution solution = new Solution();

    @Test
    public void testSimple() {
        assertEquals(2, solution.calculate("1+1"));
    }

    @Test
    public void testNestedPositiveAndNegative() {
        assertEquals(9, solution.calculate("(10-(2+3))+4"));
    }

    @Test
    public void testMultiLevelParentheses() {
        assertEquals(-6, solution.calculate("(1-(3-(5-(7-(9-(11))))))"));
    }

    @Test
    public void testZeroAndParentheses() {
        assertEquals(11, solution.calculate("(7)-(0)+(4)"));
    }

    @Test
    public void testLargeValue() {
        assertEquals(2147483647, solution.calculate("2147483647"));
    }
}

