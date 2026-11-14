class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "NoneString"
        new_str = "|^|".join(strs)
        print(new_str)
        return new_str

    def decode(self, s: str) -> List[str]:
        if s == "NoneString":
            return []
        l = s.split("|^|")
        return l

