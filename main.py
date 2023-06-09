import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get("/")
def hello_world():
    return {'message': 'Pagina Inicial'}

if __name__ == '__main__':
    uvicorn.run(app)