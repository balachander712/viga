from typing import Optional, Dict

from pydantic import BaseModel


# Define the model for the Audio Element
class AudioElementModel(BaseModel):
    id: str
    type: str
    high_volume: int
    low_volume: int
    video_component_id: Optional[str] = None
    url: Optional[str] = None
    duration: Optional[Dict[str, int]] = None