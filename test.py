import langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

print(f"LangChain 버전: {langchain.__version__}")

# 간단한 테스트
try:
    # ChatOpenAI는 자동으로 OPENAI_API_KEY 환경 변수를 사용합니다.
    llm = ChatOpenAI(model="gpt-5-nano")
    response = llm.invoke("안녕하세요!")
    print("✅ 설치 완료 - 정상 작동")
    print(f"응답: {response.content}")
except Exception as e:
    print(f"❌ 설정 오류: {e}")
