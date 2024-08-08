# fastapi-template

## ローカルで起動

```bash
docker compose up -d --build mysql
export SQLALCHEMY_DATABASE_URL=mysql+pymysql://app:app@127.0.0.1:3306/app
python migrate.py
uvicorn main:app --reload
```

```bash
docker compose up -d --build postgres
export SQLALCHEMY_DATABASE_URL=postgresql://postgres:postgres@127.0.0.1:5432/postgres
python migrate.py
uvicorn main:app --reload
```

## dockerで起動

```bash
cp .env.sample .env
```

```bash
docker compose up -d --build postgres
docker compose up -d --build mysql
docker compose up -d --build python
docker compose up -d --build nginx
docker compose up -d --build migrate
```
