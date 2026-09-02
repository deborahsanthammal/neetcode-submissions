func isAnagram(s string, t string) bool {
	var s_count, t_count map[rune]int = make(map[rune]int), map[rune]int{}

	if len(s) != len(t) {
		return false
	}

	for _, val := range s {
		s_count[val]++ 
	}

	for _, val := range t {
		t_count[val]++ 
	}

	for key, val := range s_count {
		_, exists := t_count[key]
		if !exists {return false}
		if val != t_count[key] {return false}
	}
	return true
}
