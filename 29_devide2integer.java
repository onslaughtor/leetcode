public class Solution {
    public int divide(int dividend, int divisor) {
        int ans = 0;
        if (divisor == 0||(dividend==Integer.MIN_VALUE&&divisor==-1))
            return Integer.MAX_VALUE;
        if(divisor==1)
            return dividend;
        long x = Math.abs(Long.valueOf(dividend)), y = Math.abs(Long.valueOf(divisor));
        for (int i = 31; i >= 0; i--) {
            if (x >= (y<<i)) {
                x -= y<<i;
                ans += 1 << i;
            }
        }
         
        if ((dividend < 0 && divisor > 0) || (dividend > 0 && divisor < 0))
            return ~ans + 1;
        return ans;
    }
}