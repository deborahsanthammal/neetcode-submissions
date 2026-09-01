func hasDuplicate(nums []int) bool {
    var count map[int]int = map[int]int{}

	for i:=0; i<len(nums); i++ {
		_, exists := count[nums[i]]
		if exists {
			return true
		}
		count[nums[i]] += 1
	}
	return false
}
