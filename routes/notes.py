from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from auth import get_current_user

router = APIRouter()

# Create Note
@router.post("/notes")
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db), token: str = Header(...)):
    user = get_current_user(token, db)

    new_note = models.Note(
        title=note.title,
        content=note.content,
        user_id=user.id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


# Get all notes
@router.get("/notes")
def get_notes(db: Session = Depends(get_db), token: str = Header(...)):
    user = get_current_user(token, db)

    notes = db.query(models.Note).filter(models.Note.user_id == user.id).all()

    return notes


# Update note
@router.put("/notes/{id}")
def update_note(id: int, note: schemas.NoteCreate, db: Session = Depends(get_db), token: str = Header(...)):
    user = get_current_user(token, db)

    db_note = db.query(models.Note).filter(models.Note.id == id, models.Note.user_id == user.id).first()

    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")

    db_note.title = note.title
    db_note.content = note.content

    db.commit()

    return {"message": "Updated"}


# Delete note
@router.delete("/notes/{id}")
def delete_note(id: int, db: Session = Depends(get_db), token: str = Header(...)):
    user = get_current_user(token, db)

    db_note = db.query(models.Note).filter(models.Note.id == id, models.Note.user_id == user.id).first()

    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(db_note)
    db.commit()

    return {"message": "Deleted"}