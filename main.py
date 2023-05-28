import httpx
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/pgc/player/web/playurl")
async def api_playurl(request: Request):
    # print(request.)
    url = f"https://api.bilibili.com/pgc/player/web/playurl?{request.query_params}"
    headers = dict(request.headers.items())
    headers.pop("host",None)
    headers.pop("connection",None)
    headers.pop("accept-encoding",None)
    # print(headers)
    async with httpx.AsyncClient(
            headers=headers,
            timeout=10,
    ) as client:
        res = await client.get(url)
    # print(res.text)
    return res.json()


@app.get("/pgc/player/api/playurl")
async def api_playurl(request: Request):
    # print(request.)
    url = f"https://api.bilibili.com/pgc/player/api/playurl?{request.query_params}"
    headers = dict(request.headers.items())
    headers.pop("host",None)
    headers.pop("connection",None)
    headers.pop("accept-encoding",None)
    # print(headers)
    async with httpx.AsyncClient(
            headers=headers,
            timeout=10,
    ) as client:
        res = await client.get(url)
    # print(res.text)
    return res.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("chuchai:app", host="0.0.0.0", port=9999, reload=True)
