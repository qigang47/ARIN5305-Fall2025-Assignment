import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numberOfSpecialChars(String word) {
        Map<Character, Integer> lastLower = new HashMap<>();
        Map<Character, Integer> firstUpper = new HashMap<>();
        
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (Character.isLowerCase(c)) {
                lastLower.put(c, i);
            } else if (Character.isUpperCase(c)) {
                char lowerC = Character.toLowerCase(c);
                if (!firstUpper.containsKey(lowerC)) {
                    firstUpper.put(lowerC, i);
                }
            }
        }
        
        int count = 0;
        for (char c : lastLower.keySet()) {
            if (firstUpper.containsKey(c) && lastLower.get(c) < firstUpper.get(c)) {
                count++;
            }
        }
        
        return count;
    }
}