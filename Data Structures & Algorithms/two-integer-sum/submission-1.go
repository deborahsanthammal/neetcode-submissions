func twoSum(nums []int, target int) []int {
    var index_map map[int]int = map[int]int{}
	var result []int = []int{}
	for index, value := range nums {
		var difference int = target - value
		val, exists := index_map[difference]
		if exists {
			return append(result, val, index)
		} else {
			index_map[value] = index
		}
	}
	return result
}
