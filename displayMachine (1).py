#Stephen Green
#Foundations of CS
#1/30/17


def readMachine(fname):
   inFile = open(fname, "r")
   initial = next(inFile).strip()
   final = next(inFile).strip().split(",")
   trans = {}
       
   for line in inFile:
      
       line = line.strip()
       line = line.split(",")
       state = line[0]
       inputt = line[1]
       finalstate = line[2:]

       trans[(state,inputt)]= finalstate

   return initial, final, trans
   
def FSM(mName,s):
   result = readMachine(mName)
   initial = result[0]
   final = result[1]
   trans = result[2]
   state = initial
   for letter in s:
      try:
         key = (state, letter)
         state = trans[key][0]
         if state not in final:
            print("Rejected!")
         else:
            print("Accepted")

      except KeyError:
         print("!")


def Turing(mName,s,buff):
   turingDict ={}
   inFile = open(mName, "r")
   initial = next(inFile).strip()
   final = next(inFile).strip()

   for line in inFile:
      line = line.strip()
      line = line.split(",")
      state1 = line[0]
      inputt = line[1]
      state2 = line[3]
      finalinput = line[4]
      direction = line[5]
   for letter in s:
      try:
         key = (state1, letter)
         
         
         
