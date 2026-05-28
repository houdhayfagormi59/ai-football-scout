"""
Player performance analyzer.
Scores each player out of 100 across multiple attributes.
"""
import pandas as pd
import numpy as np
from dataclasses import dataclass, field
from typing import List


@dataclass
class PlayerScore:
    name: str
    overall: float
    pace: float
    shooting: float
    passing: float
    dribbling: float
    defending: float
    physical: float
    potential: float
    position: str
    tags: List[str] = field(default_factory=list)


class PlayerAnalyzer:
    WEIGHTS = {
        "FW": {"pace": 0.20, "shooting": 0.30, "passing": 0.15,
               "dribbling": 0.20, "defending": 0.05, "physical": 0.10},
        "MF": {"pace": 0.15, "shooting": 0.15, "passing": 0.30,
               "dribbling": 0.20, "defending": 0.10, "physical": 0.10},
        "DF": {"pace": 0.15, "shooting": 0.05, "passing": 0.15,
               "dribbling": 0.10, "defending": 0.35, "physical": 0.20},
        "GK": {"pace": 0.05, "shooting": 0.01, "passing": 0.10,
               "dribbling": 0.04, "defending": 0.50, "physical": 0.30},
    }

    def score(self, player: dict) -> PlayerScore:
        pos = player.get("position", "MF")
        weights = self.WEIGHTS.get(pos, self.WEIGHTS["MF"])
        attrs = ["pace", "shooting", "passing", "dribbling", "defending", "physical"]
        overall = sum(player.get(a, 50) * weights[a] for a in attrs)

        age = player.get("age", 25)
        potential = overall + max(0, (28 - age) * 0.8) if age < 28 else overall

        tags = []
        if player.get("pace", 0) >= 85: tags.append("⚡ Pace Monster")
        if player.get("shooting", 0) >= 85: tags.append("🎯 Clinical Finisher")
        if player.get("passing", 0) >= 85: tags.append("🎩 Playmaker")
        if player.get("defending", 0) >= 85: tags.append("🛡️ Brick Wall")
        if age <= 21 and potential >= 75: tags.append("⭐ High Potential")

        return PlayerScore(
            name=player.get("name", "Unknown"),
            overall=round(overall, 1),
            pace=player.get("pace", 50),
            shooting=player.get("shooting", 50),
            passing=player.get("passing", 50),
            dribbling=player.get("dribbling", 50),
            defending=player.get("defending", 50),
            physical=player.get("physical", 50),
            potential=round(potential, 1),
            position=pos,
            tags=tags,
        )

    def rank(self, players: list) -> List[PlayerScore]:
        scored = [self.score(p) for p in players]
        return sorted(scored, key=lambda s: s.overall, reverse=True)

    def compare(self, p1: dict, p2: dict) -> dict:
        s1, s2 = self.score(p1), self.score(p2)
        attrs = ["pace", "shooting", "passing", "dribbling", "defending", "physical"]
        return {
            "player1": s1.name, "player2": s2.name,
            "winner": s1.name if s1.overall >= s2.overall else s2.name,
            "comparison": {a: {s1.name: getattr(s1, a), s2.name: getattr(s2, a)} for a in attrs},
        }