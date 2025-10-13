package robotcollisions;
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class RegressionTest0 {

    public static boolean debug = false;

    @Test
    public void test1() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test1");
        robotcollisions.Solution solution0 = new robotcollisions.Solution();
        java.lang.Class<?> wildcardClass1 = solution0.getClass();
        org.junit.Assert.assertNotNull(wildcardClass1);
    }

    @Test
    public void test2() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test2");
        robotcollisions.Solution solution0 = new robotcollisions.Solution();
        int[] intArray2 = new int[] { (short) 0 };
        int[] intArray3 = new int[] {};
        // The following exception was thrown during execution in test generation
        try {
            java.util.List<java.lang.Integer> intList5 = solution0.survivedRobotsHealths(intArray2, intArray3, "");
            org.junit.Assert.fail("Expected exception of type java.lang.StringIndexOutOfBoundsException; message: Index 0 out of bounds for length 0");
        } catch (java.lang.StringIndexOutOfBoundsException e) {
            // Expected exception.
        }
        org.junit.Assert.assertNotNull(intArray2);
        org.junit.Assert.assertArrayEquals(intArray2, new int[] { 0 });
        org.junit.Assert.assertNotNull(intArray3);
        org.junit.Assert.assertArrayEquals(intArray3, new int[] {});
    }

    @Test
    public void test3() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test3");
        robotcollisions.Solution solution0 = new robotcollisions.Solution();
        int[] intArray4 = new int[] { '#', (-1), '4' };
        int[] intArray11 = new int[] { (-1), (short) 100, (byte) 100, '4', 100, (byte) 0 };
        java.util.List<java.lang.Integer> intList13 = solution0.survivedRobotsHealths(intArray4, intArray11, "hi!");
        robotcollisions.Solution solution14 = new robotcollisions.Solution();
        int[] intArray18 = new int[] { '#', (-1), '4' };
        int[] intArray25 = new int[] { (-1), (short) 100, (byte) 100, '4', 100, (byte) 0 };
        java.util.List<java.lang.Integer> intList27 = solution14.survivedRobotsHealths(intArray18, intArray25, "hi!");
        robotcollisions.Solution solution28 = new robotcollisions.Solution();
        int[] intArray32 = new int[] { '#', (-1), '4' };
        int[] intArray39 = new int[] { (-1), (short) 100, (byte) 100, '4', 100, (byte) 0 };
        java.util.List<java.lang.Integer> intList41 = solution28.survivedRobotsHealths(intArray32, intArray39, "hi!");
        // The following exception was thrown during execution in test generation
        try {
            java.util.List<java.lang.Integer> intList43 = solution0.survivedRobotsHealths(intArray25, intArray39, "RRL");
            org.junit.Assert.fail("Expected exception of type java.lang.StringIndexOutOfBoundsException; message: Index 5 out of bounds for length 3");
        } catch (java.lang.StringIndexOutOfBoundsException e) {
            // Expected exception.
        }
        org.junit.Assert.assertNotNull(intArray4);
        org.junit.Assert.assertArrayEquals(intArray4, new int[] { 35, (-1), 52 });
        org.junit.Assert.assertNotNull(intArray11);
        org.junit.Assert.assertArrayEquals(intArray11, new int[] { (-1), 100, 100, 52, 100, 0 });
        org.junit.Assert.assertNotNull(intList13);
        org.junit.Assert.assertNotNull(intArray18);
        org.junit.Assert.assertArrayEquals(intArray18, new int[] { 35, (-1), 52 });
        org.junit.Assert.assertNotNull(intArray25);
        org.junit.Assert.assertArrayEquals(intArray25, new int[] { (-1), 100, 100, 52, 100, 0 });
        org.junit.Assert.assertNotNull(intList27);
        org.junit.Assert.assertNotNull(intArray32);
        org.junit.Assert.assertArrayEquals(intArray32, new int[] { 35, (-1), 52 });
        org.junit.Assert.assertNotNull(intArray39);
        org.junit.Assert.assertArrayEquals(intArray39, new int[] { (-1), 100, 100, 52, 100, 0 });
        org.junit.Assert.assertNotNull(intList41);
    }

    @Test
    public void test4() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test4");
        robotcollisions.Solution solution0 = new robotcollisions.Solution();
        int[] intArray4 = new int[] { '#', (-1), '4' };
        int[] intArray11 = new int[] { (-1), (short) 100, (byte) 100, '4', 100, (byte) 0 };
        java.util.List<java.lang.Integer> intList13 = solution0.survivedRobotsHealths(intArray4, intArray11, "hi!");
        java.lang.Class<?> wildcardClass14 = solution0.getClass();
        org.junit.Assert.assertNotNull(intArray4);
        org.junit.Assert.assertArrayEquals(intArray4, new int[] { 35, (-1), 52 });
        org.junit.Assert.assertNotNull(intArray11);
        org.junit.Assert.assertArrayEquals(intArray11, new int[] { (-1), 100, 100, 52, 100, 0 });
        org.junit.Assert.assertNotNull(intList13);
        org.junit.Assert.assertNotNull(wildcardClass14);
    }

    @Test
    public void test5() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test5");
        robotcollisions.Solution solution0 = new robotcollisions.Solution();
        int[] intArray4 = new int[] { '#', (-1), '4' };
        int[] intArray11 = new int[] { (-1), (short) 100, (byte) 100, '4', 100, (byte) 0 };
        java.util.List<java.lang.Integer> intList13 = solution0.survivedRobotsHealths(intArray4, intArray11, "hi!");
        java.lang.Class<?> wildcardClass14 = intList13.getClass();
        org.junit.Assert.assertNotNull(intArray4);
        org.junit.Assert.assertArrayEquals(intArray4, new int[] { 35, (-1), 52 });
        org.junit.Assert.assertNotNull(intArray11);
        org.junit.Assert.assertArrayEquals(intArray11, new int[] { (-1), 100, 100, 52, 100, 0 });
        org.junit.Assert.assertNotNull(intList13);
        org.junit.Assert.assertNotNull(wildcardClass14);
    }

    @Test
    public void test6() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test6");
        robotcollisions.Solution solution0 = new robotcollisions.Solution();
        robotcollisions.Solution solution1 = new robotcollisions.Solution();
        int[] intArray5 = new int[] { '#', (-1), '4' };
        int[] intArray12 = new int[] { (-1), (short) 100, (byte) 100, '4', 100, (byte) 0 };
        java.util.List<java.lang.Integer> intList14 = solution1.survivedRobotsHealths(intArray5, intArray12, "hi!");
        robotcollisions.Solution solution15 = new robotcollisions.Solution();
        int[] intArray19 = new int[] { '#', (-1), '4' };
        int[] intArray26 = new int[] { (-1), (short) 100, (byte) 100, '4', 100, (byte) 0 };
        java.util.List<java.lang.Integer> intList28 = solution15.survivedRobotsHealths(intArray19, intArray26, "hi!");
        // The following exception was thrown during execution in test generation
        try {
            java.util.List<java.lang.Integer> intList30 = solution0.survivedRobotsHealths(intArray12, intArray19, "");
            org.junit.Assert.fail("Expected exception of type java.lang.StringIndexOutOfBoundsException; message: Index 0 out of bounds for length 0");
        } catch (java.lang.StringIndexOutOfBoundsException e) {
            // Expected exception.
        }
        org.junit.Assert.assertNotNull(intArray5);
        org.junit.Assert.assertArrayEquals(intArray5, new int[] { 35, (-1), 52 });
        org.junit.Assert.assertNotNull(intArray12);
        org.junit.Assert.assertArrayEquals(intArray12, new int[] { (-1), 100, 100, 52, 100, 0 });
        org.junit.Assert.assertNotNull(intList14);
        org.junit.Assert.assertNotNull(intArray19);
        org.junit.Assert.assertArrayEquals(intArray19, new int[] { 35, (-1), 52 });
        org.junit.Assert.assertNotNull(intArray26);
        org.junit.Assert.assertArrayEquals(intArray26, new int[] { (-1), 100, 100, 52, 100, 0 });
        org.junit.Assert.assertNotNull(intList28);
    }

    @Test
    public void test7() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test7");
        robotcollisions.Solution solution0 = new robotcollisions.Solution();
        int[] intArray4 = new int[] { '#', (-1), '4' };
        int[] intArray11 = new int[] { (-1), (short) 100, (byte) 100, '4', 100, (byte) 0 };
        java.util.List<java.lang.Integer> intList13 = solution0.survivedRobotsHealths(intArray4, intArray11, "hi!");
        java.lang.Class<?> wildcardClass14 = intArray11.getClass();
        org.junit.Assert.assertNotNull(intArray4);
        org.junit.Assert.assertArrayEquals(intArray4, new int[] { 35, (-1), 52 });
        org.junit.Assert.assertNotNull(intArray11);
        org.junit.Assert.assertArrayEquals(intArray11, new int[] { (-1), 100, 100, 52, 100, 0 });
        org.junit.Assert.assertNotNull(intList13);
        org.junit.Assert.assertNotNull(wildcardClass14);
    }

    @Test
    public void test8() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test8");
        robotcollisions.Solution solution0 = new robotcollisions.Solution();
        int[] intArray4 = new int[] { '#', (-1), '4' };
        int[] intArray11 = new int[] { (-1), (short) 100, (byte) 100, '4', 100, (byte) 0 };
        java.util.List<java.lang.Integer> intList13 = solution0.survivedRobotsHealths(intArray4, intArray11, "hi!");
        robotcollisions.Solution solution14 = new robotcollisions.Solution();
        int[] intArray18 = new int[] { '#', (-1), '4' };
        int[] intArray25 = new int[] { (-1), (short) 100, (byte) 100, '4', 100, (byte) 0 };
        java.util.List<java.lang.Integer> intList27 = solution14.survivedRobotsHealths(intArray18, intArray25, "hi!");
        robotcollisions.Solution solution28 = new robotcollisions.Solution();
        int[] intArray32 = new int[] { '#', (-1), '4' };
        int[] intArray39 = new int[] { (-1), (short) 100, (byte) 100, '4', 100, (byte) 0 };
        java.util.List<java.lang.Integer> intList41 = solution28.survivedRobotsHealths(intArray32, intArray39, "hi!");
        // The following exception was thrown during execution in test generation
        try {
            java.util.List<java.lang.Integer> intList43 = solution0.survivedRobotsHealths(intArray25, intArray39, "RRRRR");
            org.junit.Assert.fail("Expected exception of type java.lang.StringIndexOutOfBoundsException; message: Index 5 out of bounds for length 5");
        } catch (java.lang.StringIndexOutOfBoundsException e) {
            // Expected exception.
        }
        org.junit.Assert.assertNotNull(intArray4);
        org.junit.Assert.assertArrayEquals(intArray4, new int[] { 35, (-1), 52 });
        org.junit.Assert.assertNotNull(intArray11);
        org.junit.Assert.assertArrayEquals(intArray11, new int[] { (-1), 100, 100, 52, 100, 0 });
        org.junit.Assert.assertNotNull(intList13);
        org.junit.Assert.assertNotNull(intArray18);
        org.junit.Assert.assertArrayEquals(intArray18, new int[] { 35, (-1), 52 });
        org.junit.Assert.assertNotNull(intArray25);
        org.junit.Assert.assertArrayEquals(intArray25, new int[] { (-1), 100, 100, 52, 100, 0 });
        org.junit.Assert.assertNotNull(intList27);
        org.junit.Assert.assertNotNull(intArray32);
        org.junit.Assert.assertArrayEquals(intArray32, new int[] { 35, (-1), 52 });
        org.junit.Assert.assertNotNull(intArray39);
        org.junit.Assert.assertArrayEquals(intArray39, new int[] { (-1), 100, 100, 52, 100, 0 });
        org.junit.Assert.assertNotNull(intList41);
    }
}

