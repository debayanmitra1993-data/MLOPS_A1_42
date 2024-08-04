FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN python model_v2.py
EXPOSE 5000
EXPOSE 8000
RUN chmod +x dualhost.sh
CMD ["./dualhost.sh"]