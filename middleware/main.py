import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time * 1000) + " ms"
    response.headers["X-User-Agent"] = request.headers.get("User-Agent", "unknown")
    response.headers["X-Request-Method"] = request.method
    response.headers["X-Request-Path"] = request.url.path
    response.headers["X-Request-Query"] = str(request.query_params)
    response.headers["X-Request-Body"] = str(await request.body())
    response.headers["X-Request-Timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    response.headers["X-Response-Timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    response.headers["X-Response-Status"] = str(response.status_code)
    response.headers["X-Response-Content-Type"] = response.headers.get("Content-Type", "application/json")
    response.headers["X-Response-Length"] = str(len(response.body)) if hasattr(response, 'body') else "0"
    return response


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
