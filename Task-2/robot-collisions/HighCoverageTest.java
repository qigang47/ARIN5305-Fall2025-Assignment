package robotcollisions;
import java.util.Arrays;
import java.util.List;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class HighCoverageTest {

    private final Solution solution = new Solution();

    @Test
    public void testSingleCollision() {
        int[] positions = {1, 3};
        int[] healths = {5, 3};
        String directions = "RL";
        List<Integer> result = solution.survivedRobotsHealths(positions, healths, directions);
        assertEquals(Arrays.asList(4), result);
    }

    @Test
    public void testMutualDestruction() {
        int[] positions = {1, 2};
        int[] healths = {3, 3};
        String directions = "RL";
        List<Integer> result = solution.survivedRobotsHealths(positions, healths, directions);
        assertEquals(Arrays.asList(), result);
    }

    @Test
    public void testNoCollisionAllRight() {
        int[] positions = {5, 4, 3, 2, 1};
        int[] healths = {2, 17, 9, 15, 10};
        String directions = "RRRRR";
        List<Integer> result = solution.survivedRobotsHealths(positions, healths, directions);
        assertEquals(Arrays.asList(2, 17, 9, 15, 10), result);
    }

    @Test
    public void testChainCollision() {
        int[] positions = {2, 4, 7, 9};
        int[] healths = {6, 5, 4, 3};
        String directions = "RLRL";
        List<Integer> result = solution.survivedRobotsHealths(positions, healths, directions);
        assertEquals(Arrays.asList(5), result);
    }

    @Test
    public void testMultipleInteractions() {
        int[] positions = {1, 4, 10, 11, 12};
        int[] healths = {5, 3, 8, 2, 6};
        String directions = "RLRRR";
        List<Integer> result = solution.survivedRobotsHealths(positions, healths, directions);
        assertEquals(Arrays.asList(4, 8, 2, 6), result);
    }
}

