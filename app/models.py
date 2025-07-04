from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Counter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, unique=True, description="Unique name for the counter")
    value: int = Field(default=0, description="Current counter value")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    
    def increment(self) -> None:
        """Increment the counter value by 1."""
        self.value += 1
        self.updated_at = datetime.utcnow()
    
    def decrement(self) -> None:
        """Decrement the counter value by 1."""
        self.value -= 1
        self.updated_at = datetime.utcnow()
    
    def reset(self) -> None:
        """Reset the counter value to 0."""
        self.value = 0
        self.updated_at = datetime.utcnow()