from calendar import weekday
import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class CalenderDays(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.date = Field(unique=True)

class Duties(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    abbr: str = Field(unique=True)
    
class Comments(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    startDate: int = Field(foreign_key="calenderdays.id")
    endDate: int = Field(foreign_key="calenderdays.id")

class WorkingDays(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    duty: int = Field(foreign_key="duties.id")
    date: int = Field(foreign_key="calenderdays.id")
    employe: int = Field(foreign_key="employes.id")

class Employes(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    surnameName: str
    firstname: str
    positionID: str

class Missions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    startDate: int = Field(foreign_key="calenderdays.id")
    endDate: int = Field(foreign_key="calenderdays.id")
    duty: int = Field(foreign_key="duties.id")

class Assignments(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    employe: int = Field(foreign_key="employes.id")
    mission: int = Field(foreign_key="missions.id")
    comment: int = Field(foreign_key="comments.id")