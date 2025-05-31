from abc import ABC, abstractmethod
from typing import List, Dict, Any


class Report(ABC):
    @abstractmethod
    def generate(self, data: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        pass