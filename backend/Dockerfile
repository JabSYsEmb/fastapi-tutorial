FROM python:3.10.10-alpine

WORKDIR /home/backend/

COPY . .

RUN pip install -r requirements.txt && \
    chmod +x runner.sh

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--reload"]
