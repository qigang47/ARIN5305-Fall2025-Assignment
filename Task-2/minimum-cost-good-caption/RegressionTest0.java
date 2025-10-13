package minimumcostgoodcaption;
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
        minimumcostgoodcaption.Solution solution0 = new minimumcostgoodcaption.Solution();
        java.lang.Class<?> wildcardClass1 = solution0.getClass();
        org.junit.Assert.assertNotNull(wildcardClass1);
    }

    @Test
    public void test2() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test2");
        minimumcostgoodcaption.Solution solution0 = new minimumcostgoodcaption.Solution();
        java.lang.String str2 = solution0.minCostGoodCaption("aaaaaa");
        org.junit.Assert.assertEquals("'" + str2 + "' != '" + "aaaaaa" + "'", str2, "aaaaaa");
    }

    @Test
    public void test3() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test3");
        minimumcostgoodcaption.Solution solution0 = new minimumcostgoodcaption.Solution();
        java.lang.String str2 = solution0.minCostGoodCaption("hi!");
        java.lang.String str4 = solution0.minCostGoodCaption("hi!");
        java.lang.Class<?> wildcardClass5 = solution0.getClass();
        org.junit.Assert.assertEquals("'" + str2 + "' != '" + "hhh" + "'", str2, "hhh");
        org.junit.Assert.assertEquals("'" + str4 + "' != '" + "hhh" + "'", str4, "hhh");
        org.junit.Assert.assertNotNull(wildcardClass5);
    }

    @Test
    public void test4() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test4");
        java.lang.Object obj0 = new java.lang.Object();
        java.lang.Class<?> wildcardClass1 = obj0.getClass();
        org.junit.Assert.assertNotNull(wildcardClass1);
    }

    @Test
    public void test5() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test5");
        minimumcostgoodcaption.Solution solution0 = new minimumcostgoodcaption.Solution();
        java.lang.String str2 = solution0.minCostGoodCaption("hi!");
        java.lang.Class<?> wildcardClass3 = solution0.getClass();
        org.junit.Assert.assertEquals("'" + str2 + "' != '" + "hhh" + "'", str2, "hhh");
        org.junit.Assert.assertNotNull(wildcardClass3);
    }

    @Test
    public void test6() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "RegressionTest0.test6");
        minimumcostgoodcaption.Solution solution0 = new minimumcostgoodcaption.Solution();
        java.lang.String str2 = solution0.minCostGoodCaption("abc");
        java.lang.Class<?> wildcardClass3 = solution0.getClass();
        org.junit.Assert.assertEquals("'" + str2 + "' != '" + "bbb" + "'", str2, "bbb");
        org.junit.Assert.assertNotNull(wildcardClass3);
    }
}

