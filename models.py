from sqlalchemy import Column, Integer, String, Date, Time, Text
from database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    interaction_id = Column(Integer, primary_key=True, index=True)
    hcp_id = Column(Integer)
    hcp_name = Column(String(150), nullable=False)
    interaction_type = Column(String(50))
    interaction_date = Column(Date)
    interaction_time = Column(Time)
    attendees = Column(Text)
    topics_discussed = Column(Text)
    samples_distributed = Column(Integer)
    sentiment = Column(String(30))
    outcome = Column(Text)
    follow_up_date = Column(Date)