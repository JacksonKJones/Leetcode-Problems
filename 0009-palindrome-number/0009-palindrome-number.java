class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0  || x != 0 && x%10 == 0) {
            return false;
        }

        int test = 0;
        while (x > test) {
            test = test*10 + x%10;
            x/=10;
        }

        return (x == test || x == test/10);
    }
}