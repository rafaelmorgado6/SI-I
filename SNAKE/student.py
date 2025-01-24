# Rafael Morgado 104277

"""Example client."""
import asyncio
import getpass
import json
import os
from agent import Agent
# Next 4 lines are not needed for AI agents, please remove them from your code!
import websockets

#keys = ['a','a','a','a', 'w', 'a','a','a','a','a','a','d', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'] # Test
async def agent_loop(server_address="localhost:8000", agent_name="student"):
    agent = None
    #keys = []
    async with websockets.connect(f"ws://{server_address}/player") as websocket:
        # Receive information about static game properties
        await websocket.send(json.dumps({"cmd": "join", "name": agent_name}))

        while True:
            try:
                state = json.loads(
                    await websocket.recv()
                )  # receive game update, this must be called timely or your game will get out of sync with the server
                
                if agent is None:
                    agent = Agent(state.get('map'), state.get('size'), state.get('body'))
                    #print(agent.map)

                
                keys = agent.solve(state)
                #print('score: ' + str(state.get('score')))
                print(state)
                print('\n')
                # print the state, you can use this to further process the game state
                # Next lines are only for the Human Agent, the key values are nonetheless the correct ones!
                
                await websocket.send(
                    json.dumps({"cmd": "key", "key": keys.pop(0)})
                )  # send key command to server - you must implement this send in the AI agent
            except websockets.exceptions.ConnectionClosedOK:
                print("Server has cleanly disconnected us")
                return


# DO NOT CHANGE THE LINES BELLOW
# You can change the default values using the command line, example:
# $ NAME='arrumador' python3 client.py
loop = asyncio.get_event_loop()
SERVER = os.environ.get("SERVER", "localhost")
PORT = os.environ.get("PORT", "8000")
NAME = os.environ.get("NAME", "104277")
loop.run_until_complete(agent_loop(f"{SERVER}:{PORT}", NAME))