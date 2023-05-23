from typing import Dict, Any

from pydantic import BaseModel, validator


class GetAudioElementParams(BaseModel):
    audio_element_id: str


class DeleteAudioElementParams(BaseModel):
    audio_element_id: str


class GetUpdateAudioElementParam(BaseModel):
    audio_element_id: str
    update_fields: Dict[str, Any]

    @validator('update_fields')
    def check_update_fields(cls, update_fields):
        if not update_fields:
            raise ValueError("update_fields cannot be empty")
        valid_fields = {'high_volume', 'low_volume', 'video_component_id', 'url', 'duration'}
        invalid_fields = set(update_fields.keys()) - valid_fields
        if invalid_fields:
            raise ValueError(f"Invalid fields found in update_fields: {', '.join(invalid_fields)}")
        return update_fields
