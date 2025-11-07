class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>(); 
        int[] prefixSum = new int[nums.length];         
        prefixSum[0] = nums[0];
        
        for(int i = 1; i < nums.length; i++){
            prefixSum[i] = nums[i] + prefixSum[i - 1];  
        }

        map.put(0, 1);
        int count = 0;

        for(int i = 0; i < prefixSum.length; i++){      
            int target = prefixSum[i] - k;
            if(map.containsKey(target)){                 
                count += map.get(target);
            }
            map.put(prefixSum[i], map.getOrDefault(prefixSum[i], 0) + 1);
        }

        return count;
    }
}