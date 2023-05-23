from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel
from typing import Dict, List, Optional

from models.audio_element import AudioElementModel
from use_case.add_delete_use_case import add_audio_element_use_case

router = APIRouter()


@router.post("/audio_elements", status_code=201)
def add_audio_element(audio_element: AudioElementModel, response: Response):
    result = add_audio_element_use_case(audio_element)
    response.status_code = result.status_code
    return result

@router.get("/audio_elements")
def get_audio_elements():
    return audio_elements

