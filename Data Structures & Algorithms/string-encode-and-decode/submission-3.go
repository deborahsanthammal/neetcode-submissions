type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	var result string = ""
	for _, s := range strs{
		result += strconv.Itoa(len(s)) + ":" + s
	}
	return result
}

func (s *Solution) Decode(encoded string) []string {
	var length string
	var result []string
	i := 0
	for i<len(encoded){
		if encoded[i] != ':'{
			length += string(encoded[i])
			i += 1
		} else {
			length_num, _ := strconv.Atoi(length)
			str := encoded[i+1:i+length_num+1]
			result = append(result, str)
			length = ""
			i += length_num+1
		}
	}
	return result
}
