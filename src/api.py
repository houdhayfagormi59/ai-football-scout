"""
FastAPI backend — run with: uvicorn src.api:app --reload
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from .analyzer import PlayerAnalyzer, PlayerScore

app = FastAPI(title="AI Football Scout API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

analyzer = PlayerAnalyzer()


class Player(BaseModel):
    name: str
    age: int = 25
    position: str = "MF"
    pace: float = 70
    shooting: float = 70
    passing: float = 70
    dribbling: float = 70
    defending: float = 70
    physical: float = 70


@app.get("/")
def root():
    return {"message": "AI Football Scout API", "docs": "/docs"}


@app.post("/score", response_model=dict)
def score_player(player: Player):
    result = analyzer.score(player.dict())
    return {
        "name": result.name,
        "overall": result.overall,
        "potential": result.potential,
        "position": result.position,
        "tags": result.tags,
        "attributes": {
            "pace": result.pace, "shooting": result.shooting,
            "passing": result.passing, "dribbling": result.dribbling,
            "defending": result.defending, "physical": result.physical,
        },
    }


@app.post("/rank")
def rank_players(players: List[Player]):
    ranked = analyzer.rank([p.dict() for p in players])
    return [{"rank": i + 1, "name": s.name, "overall": s.overall, "tags": s.tags}
            for i, s in enumerate(ranked)]


@app.post("/compare")
def compare_players(p1: Player, p2: Player):
    return analyzer.compare(p1.dict(), p2.dict())