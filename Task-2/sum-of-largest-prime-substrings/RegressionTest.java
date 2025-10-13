// Command to generate tests: java -classpath randoop-all-4.3.3.jar:bin randoop.main.Main gentests --testclass=sumoflargestprimesubstrings.Solution --time-limit=20 --output-limit=10 --literals-file=src/sumoflargestprimesubstrings/literals.txt --junit-output-dir=src/sumoflargestprimesubstrings
package sumoflargestprimesubstrings;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({ RegressionTest0.class })
public class RegressionTest {
}
