class Solution:

    def encode(self, strs: List[str]) -> str:
        joined_string = ""
        for str in strs:
            joined_string+= f"{len(str)}#{str}"
        print(joined_string)
        return joined_string
    def decode(self, s: str) -> List[str]:
        string_list = []
        i = 0
        while i < (len(s)):
            j = i
            while(s[j] != '#'):
                j+=1
            number = int(s[i:j])
            print("numeber :" ,number)
            original_string = s[j+1:j+1+number]
            print(original_string)
            string_list.append(original_string)
            i += number+1+j-i
            print("i value :",i)
        return string_list

            
            
                
