from fastapi import APIRouter, Depends

from . import schemas, services, security

router = APIRouter()


@router.post("/chat", response_model=schemas.ChatResponse)
async def chat_endpoint(
    request: schemas.ChatRequest,
    api_key: str = Depends(security.get_api_key),
):
    """LLM 채팅 응답을 반환하는 엔드포인트"""
    response_text = services.get_llm_response(request.prompt)
    return schemas.ChatResponse(response=response_text)
