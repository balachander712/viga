from fastapi import APIRouter, HTTPException, Response, Depends
from pydantic import BaseModel
from typing import Dict, List, Optional

from models.audio_element import AudioElementModel
from requests.audio_elements_params import GetAudioElementParams, GetUpdateAudioElementParam, DeleteAudioElementParams
from use_case.add_delete_use_case import add_audio_element_use_case, update_audio_element_use_case, \
    delete_audio_element_use_case
from use_case.get_audio_elements_use_case import get_audio_elements_use_case, get_audio_element_use_case

router = APIRouter()


@router.post("/audio_elements", status_code=201)
def add_audio_element(audio_element: AudioElementModel, response: Response):
    result = add_audio_element_use_case(audio_element)
    response.status_code = result.status_code
    return result


@router.get("/audio_elements")
def get_audio_elements(response: Response):
    result = get_audio_elements_use_case()
    response.status_code = result.status_code
    return result


@router.get("/audio_element")
def get_audio_element(
        response: Response,
        params: GetAudioElementParams = Depends(GetAudioElementParams)
):
    result = get_audio_element_use_case(**(params.dict()))
    response.status_code = result.status_code
    return result

@router.put("/audio_elements")
def update_audio_element(
        response: Response,
        params: GetUpdateAudioElementParam = Depends(GetUpdateAudioElementParam)
):
    result = update_audio_element_use_case(**(params.dict()))
    response.status_code = result.status_code
    return result


@router.delete("/audio_elements")
def update_audio_element(
        response: Response,
        params: DeleteAudioElementParams = Depends(DeleteAudioElementParams)
):
    result = delete_audio_element_use_case(**(params.dict()))
    response.status_code = result.status_code
    return result
