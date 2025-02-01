class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int minValue = prices[0];
        
        for (int price : prices) {
            ans = max(ans, price - minValue);
            minValue = min(minValue, price);
        }
        
        return ans;
    }
};
