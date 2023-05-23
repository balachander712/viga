import json


class AudioElement:
    def __init__(self):
        self.AUDIO_ELEMENTS_FILE = "audio_elements.json"

        # Load audio elements from file
    def load_audio_elements(self):
        try:
            with open(self.AUDIO_ELEMENTS_FILE, "r") as file:
                audio_elements = json.load(file)
        except FileNotFoundError:
            audio_elements = []
        return audio_elements

    # Save audio elements to file
    def save_audio_elements(self, audio_elements):
        with open(self.AUDIO_ELEMENTS_FILE, "w") as file:
            json.dump(audio_elements, file)

