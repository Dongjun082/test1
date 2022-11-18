from fastapi import FastAPI
from pydantic import BaseModel
# pydantic 데이터의 이동을 할때 사용하는것


class Cat(BaseModel):
    name: str
    id: int = 0


app = FastAPI()


@app.get("/first/{id}")  # 기본주소로 요청
async def root(id: int):
    # 딕셔너리 데이터 안에는 불변데이터가 들어가고 값은 아무거나 상관없이 들어가도 된다.
    return {"message": "Hello World", "id": id}


@app.get("/second")
async def second(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


@app.post("/cat")  # rest 통신에서 post이고 함수명은 cat
async def cat(cat: Cat):  # 받은 타입명은 cat이다.
    return cat  # pass = ...자바 스크립트의 명령문과는 다르다.
# return cat으로 해준다.
# rest api에서 raw는 그냥 데이터를 말한다.

# rest api - raw에서 json형태로 만들어 데이터를 보냄
# {
#     "name": "야옹이",
#     "id": 1
# }
