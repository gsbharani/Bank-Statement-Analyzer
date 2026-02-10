from pydantic import BaseModel
from typing import Dict

class SummaryResponse(BaseModel):
    total_inflow: float
    total_outflow: float
    net: float
    spending: Dict[str, float]
