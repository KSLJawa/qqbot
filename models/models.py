from sqlalchemy import create_engine, Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# SQLite数据库文件路径
DATABASE_URL = "sqlite:///./task_bot.db"

# 创建引擎和会话
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# QQ用户模型
class QQUser(Base):
    __tablename__ = "qq_users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, unique=True, index=True, nullable=False)  # QQ号
    nickname = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 关联任务
    tasks = relationship("Task", back_populates="owner", cascade="all, delete-orphan")


# 任务模型
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 关联用户
    owner_id = Column(Integer, ForeignKey("qq_users.id"))
    owner = relationship("QQUser", back_populates="tasks")


# 创建数据库表
def init_db():
    Base.metadata.create_all(bind=engine)