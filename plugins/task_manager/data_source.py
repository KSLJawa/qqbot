from models.models import SessionLocal, QQUser, Task
from typing import List, Optional

# 获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 获取或创建用户
async def get_user(user_id: int) -> Optional[QQUser]:
    db = next(get_db())
    user = db.query(QQUser).filter(QQUser.user_id == user_id).first()
    if not user:
        user = QQUser(user_id=user_id)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

# 添加任务
async def add_task(user_id: int, title: str) -> Task:
    db = next(get_db())
    user = await get_user(user_id)
    task = Task(title=title, owner_id=user.id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# 获取用户所有任务
async def get_tasks(user_id: int) -> List[Task]:
    db = next(get_db())
    user = await get_user(user_id)
    return db.query(Task).filter(Task.owner_id == user.id).order_by(Task.created_at.desc()).all()

# 标记任务完成
async def complete_task(user_id: int, task_num: int) -> Optional[Task]:
    db = next(get_db())
    user = await get_user(user_id)
    tasks = await get_tasks(user_id)
    if 1 <= task_num <= len(tasks):
        task = tasks[task_num-1]
        task.is_completed = True
        db.commit()
        db.refresh(task)
        return task
    return None

# 删除任务
async def delete_task(user_id: int, task_num: int) -> Optional[Task]:
    db = next(get_db())
    user = await get_user(user_id)
    tasks = await get_tasks(user_id)
    if 1 <= task_num <= len(tasks):
        task = tasks[task_num-1]
        db.delete(task)
        db.commit()
        return task
    return None