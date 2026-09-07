func topKFrequent(nums []int, k int) []int {
    var count map[int]int = make(map[int]int)
    var freq [][]int = make([][]int, len(nums)+1)

    for _, n := range nums{
        _, exists := count[n] 
        if exists {
            count[n]++
        } else {
            count[n] = 1
        }
    }

    for key, value := range count{
        freq[value] = append(freq[value], key)
    }
    var result []int
    for i := len(freq)-1; len(result) != k; i--{
        for _, n := range freq[i] {
            result = append(result, n)
        }
    }
    return result
}
