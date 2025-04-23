# Dockerfile

FROM python:3.11-slim

# Tạo thư mục app trong container
WORKDIR /app

# Copy code vào container
COPY . .

# Cài đặt thư viện
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Cổng ứng dụng chạy
EXPOSE 5000

# Lệnh chạy app
CMD ["python", "run.py"]
