class Solution:
    def isracecarbounded(self, instructions):
            #type instructions: string
            #return type: boolean
            initial_pos=[0,0]
            cur_pos=[0,0]
            #direction= ['S':0,'W':1,'N':2,'E':3] Reference for cur_dir (current direction)
            cur_dir=2
            
            #TODO: Write code below to returnn a boolean value with the solution to the prompt.
            previousChar = ""
            for i in range(len(instructions)):
                 if i == 0: 
                      previousChar = instructions[i]
                 else:
                      if (previousChar == instructions[i] and instructions[i] == "L") or (previousChar == instructions[i] and instructions[i] == "R"):
                           return True 
            return False 
                      
            pass
        
def main():
    input1=input()
    tc1 = Solution()
    ans = tc1.isracecarbounded(input1)
    print(ans)

if __name__ == "__main__":
    main()