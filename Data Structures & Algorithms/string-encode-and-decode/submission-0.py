class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res


    def decode(self, s: str) -> list[str]:
        # create an empty list to store the decoded strings

        res = []
        #i is out position in the encoded string(start at the beginning)
        i = 0
        # keep going until we've read the entire string
        while i < len(s):

            #Step 1: find where the # is (it marks the end of the length)
               #J starts at the same position as i
            j = i
            #Keep moving j forward
            while s[j] != '#':
                j += 1
                 #Until we find #


            # step 2, extract the length number
            #s[i:j] gets everything from i to j(the number before "#")
            #int()(converst the string "5" to the number 5)
            length = int(s[i:j])

            #Step 3: Move past the "#" to start the actual string

            i = j + 1
            # Step 4: Ca;culate where the string ends
            j = i + length
            
            #Step 5: Extract the String
            res.append(s[i:j])
            # Step 6: Move i to start of next encoded string
            i = j

        return res
        

        
