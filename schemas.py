from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class InteractionBase(BaseModel):
    hcp_id: int
    hcp_name: str
    interaction_type: str
    interaction_date: Optional[date] =None
    interaction_time: Optional[time] = None
    attendees:  Optional[str] = None
    topics_discussed: str
    samples_distributed: int
    sentiment: str
    outcome: str
    follow_up_date: date


class InteractionCreate(InteractionBase):
    pass


class InteractionResponse(InteractionBase):
    interaction_id: int

    class Config:
        from_attributes = True
class ConversationInput(BaseModel):
    text: str
