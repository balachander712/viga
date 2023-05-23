from typing import Optional

from use_case.audio_element import AudioElement


def find_audio_element_by_id(audio_element_id: str) -> Optional[AudioElement]:
    loader = AudioElement()
    audio_elements = loader.load_audio_elements()

    # Example implementation:
    for audio_element in audio_elements:
        if audio_element.id == audio_element_id:
            return audio_element

    return None

