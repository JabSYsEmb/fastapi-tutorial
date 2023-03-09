FROM python:3.10.10-alpine

WORKDIR /home/backend/

COPY . .

RUN pip install -r requirements.txt

RUN adduser fastapi-user --disabled-password --ingroup wheel

USER fastapi-user

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--reload"]
