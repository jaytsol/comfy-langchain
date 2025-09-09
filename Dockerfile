# 1. 베이스 이미지 설정
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /code

# 3. 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 4. 애플리케이션 코드 복사
COPY ./app /code/app

# 5. 서버 실행
# 포트 8000번으로, 외부의 모든 IP로부터의 접속을 허용하여 서버를 실행합니다.
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
