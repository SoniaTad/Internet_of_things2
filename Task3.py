import Bheap
from Bheap import *
import asyncio
import websockets
import json

BH=bh()
async def main():
    #connecting 
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        message=json.loads(await websocket.recv())
        
        if message['type'] == 'join_evt':
          client_id = message['client_id']
        
          client_id=str(client_id)
          #user input for the message to send 
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
          #As discussed during the labs session the morse code generated seems to have an additional =( which the decode_ham function will recognize as a wrong syntax
          #when running the function outside the server no additional =( is added 
          print(BH.decode_ham(response))
          #calling encode_ham to send time
          msg=BH.encode_ham(client_id,'time','hello world')
          #calling the send_time function 
          await send_time(websocket,msg,client_id)
        
          #getting back the current time
          rsp=await rec_message(client_id,websocket)
        
          print(rsp)
           #decode the morse code to get the time 
          print(BH.decode_ham(rsp))
        else:
            # If first message is not the join message exit
            print("Did not receive a correct join message")
            return 0

async def send_message(websocket, message, client_id):
    outward_message = {
        'client_id': client_id,
        'type':'morse_evt',
        'payload': message}
    await websocket.send(json.dumps(outward_message))

async def recv_message(client_id,websocket):
    message = json.loads(await websocket.recv())
    
    
    return message['payload']

#same implementation but this time with time
async def send_time(websocket,message,client_id):
    
    outward_message = {
        'client_id': client_id,
        'type':'morse_evt',
        'payload':message}
    
    await websocket.send(json.dumps(outward_message))

async def rec_message(client_id,websocket):
    message = json.loads(await websocket.recv())
    
    
    return message['payload']

#----------------------------------------------getting the binary heap used for Bheap.py --------------------------------------------------------
string=['#', 'E', 'T', 'I', 'A', 'N', 'M', 'S', 'U', 'R', 'W', 'D', 'K', 'G', 'O', 'H', 'V', 'F', '*', 'L', '*', 'P', 'J', 'B', 'X', 'C', 'Y', 'Z', 'Q', '*', '*', '5', '4', '*', '3', '*', '¿', '?', '2', '&', '*', '+', '*', '*', '*','*', '1', '6', '=', '/', '*','*', '*', '(', '*', '7', '*', '*', '*', '8', '*', '9', '0','*','*','*','*','*','*','*','*','*','*','*','*','*','_','*','*','*','*','”','*','*','.','*','*','*','*','*','*','*','*',"'",'*','*','-','*','*','*','*','*','*','*','*',';','!','*',')','*','*','*','¡','*',',','*','*','*','*',':','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','$']
BH.insert(string)
for i in range(0,118):
   string.append('*')

#-----------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    
    asyncio.run(main())
    