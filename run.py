from app import create_app
from app.extensions import db

app = create_app()

print("✅ App Flask đã khởi tạo!")

with app.app_context():
    db.create_all()
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
