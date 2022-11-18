from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, odject
from fastapi.responses import JSONResponse
# pydantic 데이터의 이동을 할때 사용하는것


class ResponseDTO(BaseModel):

    code: int
    message: str
    data: odject | None


class Cat(BaseModel):
    name: str
    # id: int | None = None
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


# 만약에 id의 값을 None 또는 0 으로 지정 할 경우
# {
#     "name": "야옹이"
# }

# id = 0 일 경우 출력 되는값 id = 0으로 출력이 된다.
# {
#     "name": "야옹이",
#     "id": 0
# }

# id = None 일 경우 출력 되는값 id = null으로 출력이 된다.
# {
#     "name": "야옹이",
#     "id": null
# }

# Query로 처리하기전의 값들 q: str | None = None 파이썬에서는 None값이라서 사실상 필요가 없다.
# @app.get("/items/")
# async def read_items(q: str | None = None):
#     results = {"items": [{"item_id": "Fo"}, {"item_id": "Foo"}]}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get("/items/")
# async def read_items(q: str | None = Query(default=None, max_length=50)):
#     results = {"items": [{"item_id": "Fo"}, {"item_id": "Foo"}]}
#     if q:
#         results.update({"q": q})
#     return results

@app.get("/error")
async def error():
    dto = ResponseDTO(
        code=0,
        message="페이지가 없습니다.",
        data=None
    )
    return JSONResponse(status_code=404, content=jsonable_encoder{dto})


@app.get("/error1")
async def error1():
    return HTTPException(status_code=404, content={"message": "item not found"})

# http://127.0.0.1:8000/redoc , http://127.0.0.1:8000/docs는 fastapi에서 만든 값을 저장한 문서들
