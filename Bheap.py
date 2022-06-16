import unittest
#binary heap class
class bh:
  def __init__(self):
    self.string=[]
  #checks if the binary heap is empty 
  def isEmpty(self):
    if len(self.string)<1:
      return True
    else:
      return False
  #gets the parent node if exists
  def getParent(self,index):
    if index < len(self.string) and index > 0:
      return int(self.string[(index-1)//2])

    else:
      return False
   # returns the right child of a node    
  def getRightChild(self,index):
    if ((index*2) + 2) < len(self.string):
      return self.string[(index*2)+ 2]
    else :
      return False
    #returns the left child of a node if exists 
  def getLeftChild(self,index):
    if ((index*2) + 1) < len(self.string):
      return self.string[(index *2) + 1]
    else:
      return False
      # method to get the index (position) of the right child of a node
  def getPositionRightChild(self,index):
    return ((index*2) + 2)
    #mothod to get the index (position) of the left child of a node 
  def getPositionLeftChild(self,index):
    
    
    return ((index*2) + 1)
  # mothod to print  all elements in the binary heap 
  def printlist(self):
    print(self.string)
  #method to insert into the binary heap 
  def insert(self,*args):
    #this insert method would let the user insert one or more elements to the b heap by taking a list as parameter 
    if len(args)==1  and isinstance(args[0],list):
      for item in args[0]:
        self.string.append(item)
    else:
      return False
  # Task 1 implementation , creating the decode_bt function    
  def decode_bt(self,morse):
    
    #check if the heap is empty 
    if self.isEmpty()== True :
      return True
    else:
      
      TheString=''
      
      str=morse.split(' ')
      
      #for each word in our string that we just split 
      for char in str :
        
        if len(char)>7:
        
          current_index=0
          
        else:
          Result=[]
            
          current_index=0
          for item in char:
            
            
            if item=='.':
              #need to go left 
              #updating current_index
              current_index=self.getPositionLeftChild(current_index)
              
            elif item== '-':
              #need to go right 
              
              current_index=self.getPositionRightChild(current_index)
          Result.append(self.string[current_index])
          result = "".join(Result)
          TheString=TheString + result
      
      return TheString
   # method added to be called in the encode_ham function  
  def encode_1(self,msg):
    #create empty string 
    MorseString=''
    #convert the msg to uppercase 
    MSG=msg.upper()
    
    for letter in MSG:
      #checking if the letter is in the dictionary created first
      if letter in MORSE_CODE_DICT:
        MorseString += MORSE_CODE_DICT[letter] + ' '
      elif letter==' ':
            
        MorseString += ' '
      else:
        MorseString+= ''
        
    return MorseString
    
  def encode_ham(self,sender,receiver,msg):
    #checking if a receiver , sender and mesage were provided by the user 
    if len(sender)==0:
      s='a sender needs to be provided'
      return s
      
    elif  len(receiver)==0 :
      r='a receiver needs to be provided'
      return r
    elif len(msg)==0:
      m='no message to encode'
      return m
    else:
      
      RESULT=''
      #calling the encode_1 method to encode each part separately to get that specific syntax 
      FIRST=self.encode_1(receiver)
      SECOND=self.encode_1(sender)
      THIRD=self.encode_1(msg)
      FOURTH=self.encode_1('DE')
      FIFTH=self.encode_1('=')
      SIXTH=self.encode_1('(')
      RESULT=FIRST + FOURTH + SECOND + FIFTH + THIRD + FIFTH + SIXTH
      return RESULT

  def decode_ham(self,str):
      #checking if a message was provided 
      if len(str)==0:
        print('no message to decode')
      else:
        #calling the decode_bt function to decode the morse message
        m=self.decode_bt(str)
        
        
        
        #counting the number of DE , = and ( in the decoded message 
        counter=m.count('DE')
        #print('number of DE',counter)
        COUNTER=m.count('=')
        #print('number of =',COUNTER)
        cont=m.count('(')
        #using the split function to split the decoded message when DE is found 
        x = m.split("DE")
        #print('AFTER',x)
        
        
        # putting some restrictions as decode_ham only decodes the specific syntax of RECEIVERDESENDER=MSG=(
        #if the syntax isn't matched a wrong syntax message will be printed out 
        if  COUNTER==2 and counter<3 and cont==1:
          
        #if the receiver is DE 
          if x[0] == "" and len(x)>2:
            
            
            x[0] = "DE"
            y = x[2].split("=")
          #if the sender is DE 
          elif x[1]=="" and x[0]!="":
            
            
            y=x[2].split("=")
            y[0]="DE"
            
          else:
              y = x[1].split("=")
          if y[1] == "":
            y[1] = "no message was input"
          if y[0]=="":
            y[0]= "no sender"
          if x[0]=="":
            x[0]="no receiver"
          
          z = y[0], x[0], y[1]
          
          return z
        else:
          z= 'wrong syntax'
          return z
                

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', '=':'-...-','+':'.-.-.','¿':'..-.-','¡':'--...-','&':'.-...','_':'..--.-',
                    "'":'.----.',':':'---...','”':'.-..-.','!':'-.-.--',
                    ';':'-.-.-.','$':'...-..-'}    
 
#creating an object of the bh() class to call the methods   
BH=bh()

#all characters in the  binary heap 
string=['#', 'E', 'T', 'I', 'A', 'N', 'M', 'S', 'U', 'R', 'W', 'D', 'K', 'G', 'O', 'H', 'V', 'F', '*', 'L', '*', 'P', 'J', 'B', 'X', 'C', 'Y', 'Z', 'Q', '*', '*', '5', '4', '*', '3', '*', '¿', '?', '2', '&', '*', '+', '*', '*', '*','*', '1', '6', '=', '/', '*','*', '*', '(', '*', '7', '*', '*', '*', '8', '*', '9', '0','*','*','*','*','*','*','*','*','*','*','*','*','*','_','*','*','*','*','”','*','*','.','*','*','*','*','*','*','*','*',"'",'*','*','-','*','*','*','*','*','*','*','*',';','!','*',')','*','*','*','¡','*',',','*','*','*','*',':','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','$']
BH.insert(string)
#adding blank '* characters added to the binary tree  after Task 4(part 1) to balance the tree
for i in range(0,118):
  BH.string.append('*')





BH.printlist()



print(BH.decode_bt(".-. .---- -.. . ... .---- -...- .... .. -...- -.--."))




class TestMorse(unittest.TestCase,bh):
    def test(self):
        #testing the decode_bt function 8 tests provided 
        self.assertEqual(BH.decode_bt('..- ...'), 'US')       # testing simple word US
        self.assertEqual(BH.decode_bt('..-'), 'U')         # testing a single letter 
        #self.assertEqual(BH.decode_bt('..-'), 'u')      # testing a letter lower case           ERROR 
        self.assertEqual(BH.decode_bt('.... . .-.. .-.. ---  .-- --- .-. .-.. -..'), 'HELLO#WORLD')         #testing a sentence with a  & as a space 
        #self.assertEqual(BH.decode_bt('..--'), 'ù')           # a character that's not in the heap        ERROR
        self.assertEqual(BH.decode_bt('...-..-'), '$')   
        # a character that does not exist will result in a blank 
        self.assertEqual(BH.decode_bt('..--'), '*') 
        self.assertEqual(BH.decode_bt('..........'), '')    # if inputing more dashes or dots than needed nothing  will happen 

        #testing the encode_ham function 9 tests provided :
        self.assertEqual(BH.encode_ham('','receiver','message'),'a sender needs to be provided')   # testing with no sender 
        #self.assertEqual(BH.encode_ham('','receiver','message'),'') # ERROR  cause the system is supposed to tell the user it needs to add a user 
        self.assertEqual(BH.encode_ham('sonia','','message'),'a receiver needs to be provided')    # in case no receiver is added the system will let the user know 
        self.assertEqual(BH.encode_ham('sonia','receiver',''),'no message to encode')    # in case no message is entered the system will let the user know 
        self.assertEqual(BH.encode_ham('s','t','e'),'- -.. . ... -...- . -...- -.--. ')  # when receiver , sender and message are provided correct morse code output 
        self.assertEqual(BH.encode_ham('s','t','e e'),'- -.. . ... -...- .  . -...- -.--. ')   # if the message contains a space the encode_ham will take it into consideration
        self.assertEqual(BH.encode_ham('s 54','t 1','e e'),'-  .---- -.. . ...  ..... ....- -...- .  . -...- -.--. ')  # if spaces are put in the sender or receiver names the encode_ham also takes that into consideration 
        self.assertEqual(BH.encode_ham('s 54','t 1','HELLO'),'-  .---- -.. . ...  ..... ....- -...- .... . .-.. .-.. --- -...- -.--. ') # testing upper case messages 
        self.assertEqual(BH.encode_ham('s 54','t 1','£'),'-  .---- -.. . ...  ..... ....- -...- -...- -.--. ')  #putting something that's not in the dictionary will just print the message as empty

        #testing the decode_ham function  10 unit tests provided 
        #decoding a single character
        self.assertEqual(BH.decode_ham('.'),'wrong syntax')
        #this test will fail as . isn't the  right syntax 
        #self.assertEqual(BH.decode_ham('.'),'E')
        #this test shows that what's decoded needs to strictly follow the syntax  
        self.assertEqual(BH.decode_ham('- .... .. ...  .. ...  .-  - . ... -'),'wrong syntax')
        # test shows when a simple sender, receiver , message is decoded 
        self.assertEqual(BH.decode_ham('. -.-. .... --- -.. . .---- ..--- ...-- ....- ..... -.... -...- .... .. -...- -.--.'),('123456', 'ECHO', 'HI'))
        # test to show what is returned when no sender is provided 
        self.assertEqual(BH.decode_ham('. -- -- .- -.. . -...- ..--- .----. ...-..- -...- -.--.'),('no sender','EMMA',"2'$"))
        #test to show what is returned when no receiver is provided 
        self.assertEqual(BH.decode_ham('-.. . ... --- -. .. .- -...- ..--- .----. ...-..- -...- -.--.'),('SONIA','no receiver',"2'$"))
        #test to show what is returned when no receiver is provided 
        self.assertEqual(BH.decode_ham('. -- -- .- -.. . ... --- -. .. .- -...- -...- -.--.'),('SONIA','EMMA','no message was input'))
        #test shows the result for DE as a sender 
        self.assertEqual(BH.decode_ham('. -- -- .- -.. . -.. . -...- .... . .-.. .-.. ---  .-- --- .-. .-.. -.. -...- -.--.'),('DE','EMMA','HELLO#WORLD'))
        #test shows the result for DEas a receiver 
        self.assertEqual(BH.decode_ham('-.. . -.. . ... --- -. .. .- -...- .-... .-... -...- -.--.'),('SONIA','DE','&&'))
        #test shows that decode_ham won't accept DE as both a sender and receiver 
        self.assertEqual(BH.decode_ham('-.. . -.. . -.. . -...- .-... .-... -...- -.--.'),'wrong syntax')
        


if __name__ == '__main__':
  unittest.main()

