class Solution {
    public boolean hasDuplicate(int[] nums){
       HashMap<Integer, Integer> dup = new HashMap<>();

       for(int i=0; i < nums.length; i++){
            Integer duple = dup.get(nums[i]);

            if(duple != null){
                return true;
            }

            dup.put(nums[i], i);

       }

       return false;
    }
}
