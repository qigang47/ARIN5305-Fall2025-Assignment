package countthenumberofspecialcharactersii;

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
        java.lang.Object obj0 = new java.lang.Object();
        java.lang.Class<?> wildcardClass1 = obj0.getClass();
        org.junit.Assert.assertNotNull(wildcardClass1);
    }

    @Test
    public void test2() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test2");
        countthenumberofspecialcharactersii.Solution solution0 = new countthenumberofspecialcharactersii.Solution();
        java.lang.Class<?> wildcardClass1 = solution0.getClass();
        org.junit.Assert.assertNotNull(wildcardClass1);
    }

    @Test
    public void test3() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test3");
        countthenumberofspecialcharactersii.Solution solution0 = new countthenumberofspecialcharactersii.Solution();
        int int2 = solution0.numberOfSpecialChars("ABC");
        int int4 = solution0.numberOfSpecialChars("aabbAABB");
        int int6 = solution0.numberOfSpecialChars("ABC");
        org.junit.Assert.assertTrue("'" + int2 + "' != '" + 0 + "'", int2 == 0);
        org.junit.Assert.assertTrue("'" + int4 + "' != '" + 2 + "'", int4 == 2);
        org.junit.Assert.assertTrue("'" + int6 + "' != '" + 0 + "'", int6 == 0);
    }

    @Test
    public void test4() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test4");
        countthenumberofspecialcharactersii.Solution solution0 = new countthenumberofspecialcharactersii.Solution();
        int int2 = solution0.numberOfSpecialChars("ABC");
        int int4 = solution0.numberOfSpecialChars("aabbAABB");
        java.lang.Class<?> wildcardClass5 = solution0.getClass();
        org.junit.Assert.assertTrue("'" + int2 + "' != '" + 0 + "'", int2 == 0);
        org.junit.Assert.assertTrue("'" + int4 + "' != '" + 2 + "'", int4 == 2);
        org.junit.Assert.assertNotNull(wildcardClass5);
    }

    @Test
    public void test5() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test5");
        countthenumberofspecialcharactersii.Solution solution0 = new countthenumberofspecialcharactersii.Solution();
        int int2 = solution0.numberOfSpecialChars("ABC");
        int int4 = solution0.numberOfSpecialChars("aabbAABB");
        int int6 = solution0.numberOfSpecialChars("Aa");
        int int8 = solution0.numberOfSpecialChars("");
        java.lang.Class<?> wildcardClass9 = solution0.getClass();
        org.junit.Assert.assertTrue("'" + int2 + "' != '" + 0 + "'", int2 == 0);
        org.junit.Assert.assertTrue("'" + int4 + "' != '" + 2 + "'", int4 == 2);
        org.junit.Assert.assertTrue("'" + int6 + "' != '" + 0 + "'", int6 == 0);
        org.junit.Assert.assertTrue("'" + int8 + "' != '" + 0 + "'", int8 == 0);
        org.junit.Assert.assertNotNull(wildcardClass9);
    }
}
