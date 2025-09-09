import os
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

API_KEY_NAME = "X-Internal-API-Key"
API_KEY = os.getenv("INTERNAL_API_KEY")

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


async def get_api_key(api_key: str = Security(api_key_header)):
    """API 키를 검증하는 의존성 함수"""
    if not API_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="서버에 API 키가 설정되지 않았습니다.",
        )

    if api_key == API_KEY:
        return api_key
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="제공된 API 키가 유효하지 않습니다.",
        )
