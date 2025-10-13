// Command to generate tests: java -classpath randoop-all-4.3.3.jar:bin randoop.main.Main gentests --testclass=basiccalculator.Solution --time-limit=20 --output-limit=10 --literals-file=src/basiccalculator/literals.txt --junit-output-dir=src/basiccalculator
package basiccalculator;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({ RegressionTest0.class })
public class RegressionTest {
}
