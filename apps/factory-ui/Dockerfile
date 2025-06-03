# Node.js 18 Alpine 이미지 사용
FROM node:18-alpine

# 작업 디렉토리 설정
WORKDIR /usr/src/app

# pnpm 설치
RUN npm install -g pnpm

# package.json과 pnpm-lock.yaml 복사 (캐싱을 위해)
COPY package.json pnpm-lock.yaml* ./

# 의존성 설치
RUN pnpm install

# 소스 코드 복사
COPY . .

# 포트 노출
EXPOSE 5173

# 개발 서버 실행
CMD ["pnpm", "dev", "--host"] 