class Solution:
    def isValid(self, s: str) -> bool:
        d={'}':'{',']':'[',')':'('}
        l=[]
        for i in s:
            if i in d:
                x=l.pop() if l else '*'
                if d[i]!=x:
                    return False
            else:
                l.append(i)
        return not l