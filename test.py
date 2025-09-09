import langchain
from langchain_openai import ChatOpenAI

print(f"LangChain 버전: {langchain.__version__}")

# 간단한 테스트
try:
    llm = ChatOpenAI(model="gpt-4o-mini")
    response = llm.invoke("안녕하세요!")
    print("✅ 설치 완료 - 정상 작동")
    print(f"응답: {response.content}")
except Exception as e:
    print(f"❌ 설정 오류: {e}")