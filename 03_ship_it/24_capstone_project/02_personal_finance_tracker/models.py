from datetime import date
from dataclasses import dataclass,asdict
from uuid import uuid4

@dataclass
class Transaction:
    type: str
    category: str
    amount: float
    date : str
    description : str =""
    id :str =""
    
    def __post_init___(self):
        self.type=self.type.lower().strip()
        self.category=self.category.strip()
        self.description=self.description.strip()
        
        if self.type not in("income","expense"):
            raise ValueError("Type must be income or expense.")
        if not self.category:
            raise ValueError("Category cannot be empty.")    
        if self.amount <=0:
            raise ValueError("Amount must be greater than zero.")
        try:
            date.fromisoformat(self.date)
        except ValueError:
            raise ValueError("Date must be YYYY-MM-DD format.")
        if not self.id:
            self.id= str(uuid4())[:8]
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls,data):
        return cls(**data)
               