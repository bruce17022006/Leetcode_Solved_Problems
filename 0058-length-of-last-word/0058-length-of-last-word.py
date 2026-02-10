class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st=len(s)
        cnt=0
        for i in range(st-1,-1,-1):
            if(s[i]==' ' and cnt>0):
                break
            elif(s[i]==' ' and cnt<0):
                continue
            elif(s[i]!=' '):
                cnt+=1
        return cnt
                