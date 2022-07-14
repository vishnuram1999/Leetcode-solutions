class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = []
        arr.append(first)
        for i in range(len(encoded)):
            new = arr[i] ^ encoded[i]
            arr.append(new)
        return arr