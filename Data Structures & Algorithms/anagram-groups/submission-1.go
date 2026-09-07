func groupAnagrams(strs []string) [][]string {
    var result map[[26]int][]string = make(map[[26]int][]string)

    for _, s := range strs {
        var key [26]int
        for _, c := range s {
            key[c-'a']++

        }
        result[key] = append(result[key], s)
    }
    var output [][]string
    for _, group := range result {
        output = append(output, group)
    }
    return output
}
