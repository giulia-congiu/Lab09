from dataclasses import dataclass

from model.areoporto import Areoporto


@dataclass
class Arco:
    o1: Areoporto
    o2: Areoporto
    peso: int