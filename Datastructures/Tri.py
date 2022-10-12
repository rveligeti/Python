
class Trie:

    def __init__(self):
        self.pointer=dict()
        self.endofWord=False
        

    def insert(self, word: str) -> None:
        currentPointer=self
        for item in word:
            if item in currentPointer.pointer:
                currentPointer=currentPointer.pointer[item]
            else:
                value=Trie()
                currentPointer.pointer[item]=value
                currentPointer=value
        currentPointer.endofWord=True
        
        

    def search(self, word: str) -> bool:
        currentPointer=self
        for item in word:
            if item in currentPointer.pointer:
                currentPointer=currentPointer.pointer[item]
            else:
                return False
        return currentPointer.endofWord

    def startsWith(self, prefix: str) -> bool:
        currentPointer=self
        for item in prefix:
            if item in currentPointer.pointer:
                currentPointer=currentPointer.pointer[item]
            else:
                return False
        return True
