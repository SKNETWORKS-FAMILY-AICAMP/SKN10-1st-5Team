# KIA FAQ DB 연결 및 쿼리

## 주요 기능
- kia faq DB에 쿼리할 수 있음.

## DB 구성
docker-compose.yaml
```yaml
version: "3"

services:
  db:
    image: mysql
    restart: always
    command:
      - --character-set-server=utf8mb4
      - --collation-server=utf8mb4_unicode_ci
    volumes:
      - ./database:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: "root12345"
      MYSQL_DATABASE: "faq"
      MYSQL_USER: "user"
      MYSQL_PASSWORD: "u12345"
    ports:
      - "3307:3306"
```

PowerShell
```shell
docker-compose up -d
```

## 필수 요구사항 설치
두 가지 방법 중 택 1
```shell
pip install PyMySQL pandas cryptography
```
```shell
pip install -r requirements.txt
```

## SQL 쿼리문 실행
```shell
python main.py
```
---
HoneyWater8