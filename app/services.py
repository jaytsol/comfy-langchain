from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

def get_llm_response(prompt: str) -> str:
    """주어진 프롬프트에 대해 LLM 응답을 반환합니다."""
    try:
        llm = ChatOpenAI(model="gpt-5-nano")  # 비용 효율적인 모델 사용
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        # 실제 프로덕션에서는 로깅 라이브러리를 사용하는 것이 좋습니다.
        print(f"Error during LLM call: {e}")
        return "죄송합니다, AI 응답을 생성하는 중에 오류가 발생했습니다."
