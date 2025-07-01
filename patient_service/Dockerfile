FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y curl && apt-get clean
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#ENV PYTHONPATH="/app"
EXPOSE 8001

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
#CMD ["sh", "-c", "python create_table.py && uvicorn main:app --host 0.0.0.0 --port 8001"]