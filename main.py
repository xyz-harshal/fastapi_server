from fastapi import FastAPI,WebSocket
from routes import userRoute
from auth import jwt_encode,jwt_decode
from fastapi.middleware.cors import CORSMiddleware
import socketio
from typing import Dict,List
app=FastAPI()

allowed_origin=["http://localhost:3000"]

sio=socketio.AsyncServer(async_mode='asgi',cors_allowed_origins=allowed_origin,logger=True,engineio_logger=True)
socket_app=socketio.ASGIApp(sio,app)
app.mount('/socket.io',socket_app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origin,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(userRoute.router)


class ConnectionManager:
    def __init__(self):
        self.active_connections:Dict[str,List[str]]={}

    async def connect(self,sid:str,user_id:str):
        if user_id not in self.active_connections:
            self.active_connections[user_id]=[]
        self.active_connections[user_id].append(sid)
        print(f"New Connection added to {user_id}: of {sid}")
        print(self.active_connections)
    
    async def disconnect(self,sid:str):
        for user_id,sids in self.active_connections.items():
            if sid in sids:
                sids.remove(sid)
                print(f"Disconnected user: {user_id}, SID: {sid}")
                if not sid:
                    del self.active_connections[user_id]

@sio.event
async def connect(sid,environ):
    print(f"client connected: {sid}")

@sio.event
async def disconnect(sid):
    print(f"client disconnected: {sid}")

@sio.event
async def message(sid,data):
    print(f"message recieved from: {sid} is: {data}")
    await sio.emit('message',{'data':f"Server recieved: {data}"},room=sid)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
