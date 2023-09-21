from pydantic import BaseModel

class Body(BaseModel):
    question: str = None