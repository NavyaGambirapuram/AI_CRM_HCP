
from sqlalchemy.orm import Session
from models import Interaction
import schemas
from schemas import InteractionCreate

def create_interaction(db: Session, interaction: schemas.InteractionCreate):
    db_interaction = Interaction(**interaction.model_dump())

    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    return db_interaction


def get_interactions(db: Session):
    return db.query(Interaction).all()


def get_interaction(db: Session, interaction_id: int):
    return (
        db.query(Interaction)
        .filter(Interaction.interaction_id == interaction_id)
        .first()
    )


def update_interaction(
    db: Session,
    interaction_id: int,
    interaction: InteractionCreate,
):
    db_interaction = get_interaction(db, interaction_id)

    if db_interaction:
        for key, value in interaction.model_dump().items():
            setattr(db_interaction, key, value)

        db.commit()
        db.refresh(db_interaction)

    return db_interaction


def delete_interaction(db: Session, interaction_id: int):
    db_interaction = get_interaction(db, interaction_id)

    if db_interaction:
        db.delete(db_interaction)
        db.commit()

    return db_interaction