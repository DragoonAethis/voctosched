import re
from string import ascii_letters, digits

from fahrplan.model import Conference, Event


class StandardSlugGenerator:
    def __init__(self, conference: Conference):
        self.acronym = conference.acronym

    def __call__(self, event: Event):
        title = StandardSlugGenerator.normalize_name(event.title)
        return f"{self.acronym}-{event.id}-{title}"[:240]

    @staticmethod
    def normalize_name(name: str):
        name = re.sub(r"\W+", "_", name)
        legal_chars = ascii_letters + digits + "_"
        pattern = f"[^{legal_chars}]+"
        name = re.sub(pattern, "", name)
        name = name.lower()
        return name
