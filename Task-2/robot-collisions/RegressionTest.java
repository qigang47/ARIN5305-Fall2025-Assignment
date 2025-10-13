// Command to generate tests: java -classpath randoop-all-4.3.3.jar:bin randoop.main.Main gentests --testclass=robotcollisions.Solution --time-limit=20 --output-limit=10 --literals-file=src/robotcollisions/literals.txt --junit-output-dir=src/robotcollisions
package robotcollisions;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({ RegressionTest0.class })
public class RegressionTest {
}
