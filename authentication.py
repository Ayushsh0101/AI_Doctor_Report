# import os
# import bcrypt
# from dotenv import load_dotenv
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker, declarative_base

# # Load environment variables
# load_dotenv()

# DB_USER = os.getenv("DB_USER", "root")
# DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
# DB_HOST = os.getenv("DB_HOST", "localhost")
# DB_NAME = os.getenv("DB_NAME", "ai_doctor")

# # MySQL Database URL
# DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# # SQLAlchemy setup
# engine = create_engine(DATABASE_URL, echo=True)  # echo=True for debugging
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()

# # User Model
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50), unique=True, index=True, nullable=False)
#     password = Column(String(255), nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     phone = Column(String(20), nullable=True)


# # Create tables if not exists
# Base.metadata.create_all(bind=engine)

# # ✅ Register User
# def register_user(username: str, password: str, email: str, phone: str) -> str:
#     session = SessionLocal()
#     try:
#         existing_user = session.query(User).filter(
#             (User.username == username) | (User.email == email)
#         ).first()
#         if existing_user:
#             return "❌ Username or Email already exists!"
        
#         hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
#         new_user = User(
#             username=username,
#             password=hashed_pw.decode("utf-8"),
#             email=email,
#             phone=phone
#         )
#         session.add(new_user)
#         session.commit()
#         return "✅ Registered successfully!"
#     finally:
#         session.close()


# # ✅ Login User
# def login_user(username: str, password: str):
#     if not username or not password:
#         return False, "⚠️ Username and Password required!"

#     session = SessionLocal()
#     try:
#         user = session.query(User).filter(User.username == username).first()
#         if not user:
#             return False, "❌ User not found"
        
#         if bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
#             return True, f"✅ Welcome {username}"
#         return False, "❌ Incorrect password"
#     finally:
#         session.close()

# # ✅ Reset Password
# def reset_password(username: str, new_password: str) -> str:
#     if not username or not new_password:
#         return "⚠️ Username and New Password required!"

#     session = SessionLocal()
#     try:
#         user = session.query(User).filter(User.username == username).first()
#         if not user:
#             return "❌ User not found!"
        
#         hashed_pw = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt())
#         user.password = hashed_pw.decode("utf-8")
#         session.commit()
#         return "✅ Password updated successfully!"
#     finally:
#         session.close()


# # ✅ Debug mode (Run this file directly for quick test)
# if __name__ == "__main__":
#     print(register_user("testuser", "123456", "test@example.com", "1234567890"))
#     print(login_user("testuser", "123456"))
#     print(reset_password("testuser", "newpassword123"))
#     print(login_user("testuser", "newpassword123"))
import os
import bcrypt
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "ai_doctor")

# MySQL Database URL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# User Model (fix column order)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(255), nullable=False)

# Register User
def register_user(username: str, email: str, phone: str, password: str) -> str:
    session = SessionLocal()
    try:
        existing_user = session.query(User).filter(User.username == username).first()
        if existing_user:
            return "❌ User already exists!"
        
        hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        new_user = User(
            username=username,
            email=email,
            phone=phone,
            password=hashed_pw.decode("utf-8")
        )
        session.add(new_user)
        session.commit()
        return "✅ Registered successfully!"
    finally:
        session.close()


# ✅ Login User
def login_user(username: str, password: str):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if not user:
            return False, "❌ User not found"
        
        if bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            return True, f"✅ Welcome {username}"
        return False, "❌ Incorrect password"
    finally:
        session.close()

# Debug mode
if __name__ == "__main__":
    print(register_user("testuser", "test@mail.com", "9999999999", "123456"))
    print(login_user("testuser", "123456"))
