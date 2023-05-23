from use_case.audio_element import AudioElement


def get_audio_elements():
    loader = AudioElement()
    audio_elements = loader.load_audio_elements()
    if audio_elements:
        return