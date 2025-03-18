from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from typing import List

router = APIRouter()

# ✅ 1. สร้างผู้ใช้ใหม่ (Create)
@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ✅ 2. ค้นหาผู้ใช้ทั้งหมด (Search All)
@router.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# ✅ 3. ค้นหาผู้ใช้จาก ID (Search by ID)
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ✅ 4. อัปเดตข้อมูลผู้ใช้ (Update)
@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user_data.name:
        user.name = user_data.name
    if user_data.email:
        user.email = user_data.email
    if user_data.age is not None:
        user.age = user_data.age

    db.commit()
    db.refresh(user)
    return user

# ✅ 5. ลบผู้ใช้ (Delete)
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
