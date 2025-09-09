from pydantic import BaseModel


class ChatRequest(BaseModel):
    """채팅 요청을 위한 모델"""

    prompt: str


class ChatResponse(BaseModel):
    """채팅 응답을 위한 모델"""

    response: str
