FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y curl && apt-get clean
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8003

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
