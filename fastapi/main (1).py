from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.middleware("http")
async def connection_notice(request, call_next):
    print(f"A Player Connecting This Server: {request.client.host}")
    response = await call_next(request)
    return response


@app.get("/", response_class=HTMLResponse)
@app.get("/8000", response_class=HTMLResponse)
def home():
    return """<!doctype html>
<html lang="tr">
<head><meta charset="utf-8"><title>Google'ı aç</title></head>
<body>
  <button onclick="window.open('https://www.google.com', '_blank', 'width=1200,height=800')">
    Google'ı aç
  </button>
</body>
</html>"""


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
