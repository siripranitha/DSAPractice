class Solution:
    def reverseWords(self, s: str) -> str:
       output = ""
       i=len(s)-1
       while i>=0:
        # remove the available white spaces from the end
        while i>=0 and s[i]==" ":
            i = i-1
        if i<0:
            break
        # mark the end of this word
        end = i
        while i>=0 and s[i]!=" ":
            i = i-1

        if output:
            output = output + " " # appending white space only if we already have a output
        output = output + s[i+1:end+1]

       return output     
