# Worksheet2part2

## Table of content 
* *Introduction*
* *Installation*
* *Tasks*
    + Task 1
    + Task 2
    + Task 3
    
## Introduction :
This is worksheet 2 part 2 of IOT, it will mostly focus on the implementation of binary heaps to encode and decode morse code.
The programming language used is python 
This projects has 2 python files as well as 3 Tasks.
The first thing to do would be making sure everything is correctly set up on the device that is going to be used .
## Installation :
Before engaging in this worksheet, the first thing to do is to understand how to get the python files of this project to run correctly on the device used.
A remote server **csctcloud.uwe.ac.uk** was used for this as well as the next IOT worksheets . Accessing the remote server requires installing   Azure CLI and SSH Keys  .Visual studio code needs to be installed on the device and configured for remote development to enable the user to connect to the server as it represents the environment the code will be ran in, for this particular part a UWE email was used to connect.
It’s useful to know that the steps and commands to run might differ depending on the OS of the device, just like any other editor could be used instead of VS .
## Tasks : 
### Task 1 :

The goal of this task was to implement the **decode_bt** function , this function does exactly what the W2P1 decode function does , takes a string of morse code and returns the text value of it , only this time the function will be using a binary heap .
In the python file **Bheap.py**  a binary heap is first implemented , it methods  allow insertion , printing all elements as well as getting the index of the nodes (parent  and  children) .
The **decode_bt** function consists of a nested for loop that would go through each item of each morse sequence and starting from and checks If the item is a dot or a dash , starting from the root , it will go either right or left and would then update the current index.
```
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
```
__The second part of this task__ was to implement some tests for the **decode_bt** function , which can be found in the **Bheap.py** file , 8 unit tests were ran using the assertEqual method , the unittest python library had to be imported to run the tests , commented tests are meant to fail hence why being commented out.
```
#testing the decode_bt function 8 tests provided 
        self.assertEqual(BH.decode_bt('..- ...'), 'US')       # testing simple word US
        self.assertEqual(BH.decode_bt('..-'), 'U')         # testing a single letter 
        #self.assertEqual(BH.decode_bt('..-'), 'u')      # testing a letter lower case           ERROR 
        self.assertEqual(BH.decode_bt('.... . .-.. .-.. ---  .-- --- .-. .-.. -..'), 'HELLO#WORLD')          
        #self.assertEqual(BH.decode_bt('..--'), 'ù')           # a character that's not in the heap        ERROR
        self.assertEqual(BH.decode_bt('...-..-'), '$')   
        # a character that does not exist will result in a blank 
        self.assertEqual(BH.decode_bt('..--'), '*') 
        self.assertEqual(BH.decode_bt('..........'), '')
```


__The third and last part of task one consists of comparing the different ways of decoded a morse message using binary heaps, trees and dictionaries__.
As seen with the **decode** function in part one, where the binary tree was used   and the **decode_bt** using the heap in this task, the concept is practically the same as the binary heap is a  linear representation of a tree , both would need a nested for loop to access each item (dot or dash) of each sequence of morse code as seen in both **decode** and **decode_bt**, the functions check if the item is a dot or dash to know which node to move to next or to stop. 

Decoding using a binary tree would lead to a tree traversal , which is  possible due to __current node__  being updated to either the right or left child of the current node every time a dot or dash is met, starting with the root as the current node .On the other hand for binary heaps since  it’s linear and the values are represented in the form of an array  ,it will keep track of the current index of the array and update it each time , by calling a function that would do the calculations , in this case (**getPositionLeftchild or getPositionRightChild** ) to know where to move next.
Python dictionaries are another story,a dictionary is meant to have pairs of keys a values.Morse code could be decoded using a dictionary by putting letters as keys and to each key a value (morse code) , implementing the **decode** function this way would lead to utilizing one for loop instead of two as accessing each item wouldn’t be necessary anymore, it would only need to get the value of that specific key .

While decoding morse code seems simpler using a python dictionary , dictionaries are known for not being the most efficient data structure when it comes to memory space usage  and consumption .As a conclusion which method to use would depend on the needs and the resources .

### Task 2: 
For the second task, two functions were implemented **encode_ham** and **decode_ham** but, first to have a better understanding of what those functions are supposed to return ,  a second web page was visited by connecting to the remote server and forwarding the __port 10101__ , from a browser using the URL __://localhost:10101__ it was possible to test some  of the functionalities the two functions should have .

**Encode_ham** takes a sender , receiver and message as parameters and returns a morse message , when being encoded it will be under this specific syntax **RECEIVERDESENDER=MSG=(** in morse code , this was implemented by calling a simple **encode** function that would encode each parameter separately by using a dictionary as encoding using a binary heap is more complicated than decoding with one .
```
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
```

**Decode_ham** works the other way around as it would take a morse string and returns a tuple that contains (the sender, receiver and message) , but then again the decode_ham wouldn’t decode a string with an incorrect syntax that's  why some validation checks had to be put in place to make a difference between a simple **decode** function and the **decode_ham** one.
**decode_ham** uses a decode function but has additional restrictions
```
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


```
**Decode_ham** allows the receiver or sender to be ‘DE’ but not both at the same time , just like any wrong syntax typed it will return a wrong syntax message
**testing*
In the **Bheap.py** file can be found some unittests made to test both encode_ham and decode_ham **19** tests in total using the assertEqual method which will need the unittest standard library to be imported for, and of course just like the tests before some are commented out as they are made to fail .

```
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

```

### Task 3:
For this last task , two additional functions were  implemented the **send_message** function as well as  the **send_time** function . As a websocket connection to the remote server  was established using the URL __“ws: //localhost:10102”__ , websocket had to be imported  in the **Task3.py** file .
After connecting to the server , the user has to enter a message , which will be encoded by **encode_ham** , the **send_message** function will then send the encoded message to echo and wait for a response  , the last step would be to call **decode_ham** and wait for it to decode the message sent by echo 
**for some reason the encoded part has an additional =( at the end making the decode_ham classify it as a wrong syntax , trying the exact same morse code outside of the server gets the right input proving that the function is working perfectly**
```
message=input("enter message :")
          message=str(message)
          print('here is the message',message)
          #calling encode_ham 
          message=BH.encode_ham(client_id,'echo',message)
          # calling the send_message function 
          await send_message(websocket, message, client_id)
          response = await recv_message(client_id,websocket)   
          print("The Server Sent Back:")
          print(response) 
          print(BH.decode_ham(response))

```

**Send_time** function goes through the same steps  as **send_message** but instead of returning a message it returns the current time 
__Note__ that importing json , asyncio and the Bheap.py file are a must to run **Task3.py**
