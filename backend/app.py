import json
from pathlib import Path
from fastapi import FastAPI
from fastapi import Request, Response, WebSocket
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi import Header
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="templates")
CHUNK_SIZE = 1024*1024
video_path = Path("video.mp4")
origins = [
    "http://localhost:5000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/")
# async def read_root(request: Request):
#     return templates.TemplateResponse("index.html", context={"request": request})
#
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws/F1_1_3_1");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{path}")
async def websocket_endpoint(path: str, websocket: WebSocket):
    with open(f'info/{path}.json', 'r', encoding='utf8') as file:
        data = json.load(file)
    await websocket.accept()
    i = 0
    while True:
        # data = await websocket.receive_text()
        # await websocket.send_text(f"Message text was: {data}")
        await asyncio.sleep(1)
        await websocket.send_json(data[i])
        i += 1
        if i >= len(data):
            i = 0


@app.get("/video/{path}/")
async def video_endpoint(path: str, Range: str = Header(None)):
    start, end = Range.replace("bytes=", "").split("-")
    start = int(start)
    end = int(end) if end else start + CHUNK_SIZE

    # with open(f'data/{path}.mp4', "rb") as video:
    with open(f'raw/{path}.mp4', "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        filesize = str(video_path.stat().st_size)
        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
            'Accept-Ranges': 'bytes'
        }
        return Response(data, status_code=206, headers=headers, media_type="video/mp4")


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)