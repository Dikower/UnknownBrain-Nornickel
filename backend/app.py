import json
from pathlib import Path
from fastapi import FastAPI
from fastapi import Request, Response, WebSocket
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi import Header
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import asyncio
import uvicorn
import os


app = FastAPI()
templates = Jinja2Templates(directory="templates")
CHUNK_SIZE = 1024*1024
video_path = Path("video.mp4")
origins = [
    "http://localhost:5000",
    "http://localhost:8000",
]
opened_files = {}


# @app.on_event('startup')
# def startup():
#     global opened_files
#     for name in os.listdir('static/raw'):
#         opened_files[name] = open(f'static/raw/{name}', 'rb')
#
#
# @app.on_event('shutdown')
# def shutdown():
#     for file in opened_files:
#         file.close()


app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/ws/{path}")
async def websocket_endpoint(path: str, websocket: WebSocket):
    with open(f'static/info/{path}.json', 'r', encoding='utf8') as file:
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

    with open(f'static/raw/{path}.mp4', "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        filesize = str(video_path.stat().st_size)
        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
            'Accept-Ranges': 'bytes'
        }
        return Response(data, status_code=206, headers=headers, media_type="video/mp4")
    # path += '.mp4'
    # video = opened_files[path]
    # video.seek(start)
    # data = video.read(end - start)
    # filesize = str(video_path.stat().st_size)
    # headers = {
    #     'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
    #     'Accept-Ranges': 'bytes'
    # }
    # return Response(data, status_code=206, headers=headers, media_type="video/mp4")


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)