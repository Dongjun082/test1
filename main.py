from fastapi import FastAPI

app = FastAPI()


@app.get("/first")  # 기본주소로 요청
async def root():
    return "안녕하세요."  # {"message": "Hello World"}
