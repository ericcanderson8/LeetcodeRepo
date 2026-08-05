class Solution:
    def isNumber(self, s: str) -> bool:
        # state 0 -> state 8
        # options include
        # "Num"
        # "Sign"
        # "Dot"
        # "E"
        rulebook = [
            {"Num": 2, "Sign": 1, "Dot": 3},           
            {"Dot": 3, "Num": 2}, 
            {"Num": 2, "E": 6, "Dot": 4},
            {"Num": 5}, 
            {"Num": 5, "E": 6},
            {"Num": 5, "E": 6},
            {"Num": 7, "Sign": 8},
            {"Num": 7},
            {"Num": 7}
        ]

        state = 0
        identifier = ""
        for c in s:
            if c.isdigit():
                identifier = "Num"
            elif c == '+' or c == '-':
                identifier = "Sign"
            elif c == 'e' or c == 'E':
                identifier = "E"
            elif c == '.':
                identifier = "Dot"
            else:
                return False

            if identifier in rulebook[state]:
                state = rulebook[state][identifier]
            else:
                return False

        endings = {2, 4, 5, 7}

        if state in endings:
            return True
        return False
        # check that your last room is a valid ending state
        