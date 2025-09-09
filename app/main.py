from fastapi import FastAPI

from . import api

app = FastAPI(
    title="SurfAI LangChain Server",
    description="SurfAI의 LLM 기능을 처리하는 내부 API 서버입니다.",
    version="0.1.0",
)

# /api/v1 접두사와 함께 api 라우터 포함
app.include_router(api.router, prefix="/api/v1")


@app.get("/")
def read_root():
    """서버의 상태를 확인하는 기본 엔드포인트"""
    return {"status": "ok"}
