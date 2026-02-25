import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch1=""
        ch2=""
        ch=""
        if s==" ":
            return True
        else:
            s1=re.sub(r'[^a-zA-Z0-9]','',s).lower()
            ch1=s1
            ch2=s1[::-1]
            if(ch1==ch2):
                return True
            else:
                return False

        