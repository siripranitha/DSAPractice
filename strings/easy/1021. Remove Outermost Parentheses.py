class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        if not s:
            return ""

        start = 0
       
        n = len(s)
        openingBracket = 0
        output = ""

        for i in range(n):

            if s[i]=="(":
                openingBracket+=1
            else:
                openingBracket -=1
            if openingBracket==0:
                end = i
                output = output + s[start+1:end]
                start = end+1

        return output
                

        


        
