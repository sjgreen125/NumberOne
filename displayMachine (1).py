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
   initial = ""
   final = ""
   itemList = []
   typeList = []
   count = 0
   for line in inFile:
      line = line.strip()
      state1 = line[0]
      inputt = line[1]
      if count == 0:
         initial = line.strip("\n")

      if count == 1:
         final = line.strip("\n")

      if count >=2:
         line = line.split(",")
         try:
            line[-1] = line[-1].strip("\n")
            if  state1 not in itemList:
               itemList.append(state1)
            if inputt not in typeList:
               typeList.append(inputt)
            dictKey = (state1, inputt)
            dictAns = tuple(line[2:])
            turingDict[dictKey] = dictAns
         except  IndexError:
            pass
      count+=1
      
         
   randInt = 0
   while randInt < buff:
       s = "B"+s+"B"
       randInt +=1
   pos = buff
   stringlist = []
   for letter in s:
      stringlist.append(letter)
   try:
      while initial != final:
         loc= turingDict[{line,s[pos]}]
         state = loc[0]
         stringlist[pos] = loc[1]

         if loc[2] == "L":
            pos -=1
         elif loc[2] == "R":
            pos+=1
   except KeyError:
      print("!")
       
         
   if initial not in final:
      print("Rejected!")
   else:
      print("Accepted")
      finalString = ""

      for lett in stringlist:
         if lett != "B":
            finalString = finalString+lett

      print(finalString)
  
      
