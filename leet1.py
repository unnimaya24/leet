lengthOfLastWord=input("enter the name")
def lengthOfLastWord(self, s: str):
        stripped = s.strip()
        strList = stripped.split(" ")
        lastWord = strList[-1]
        return len(lastWord)