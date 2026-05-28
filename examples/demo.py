"""
Quick demo — run: python examples/demo.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.analyzer import PlayerAnalyzer

analyzer = PlayerAnalyzer()

players = [
    {"name": "Ronaldo", "age": 22, "position": "FW",
     "pace": 92, "shooting": 93, "passing": 80, "dribbling": 89, "defending": 35, "physical": 88},
    {"name": "Messi",   "age": 22, "position": "FW",
     "pace": 87, "shooting": 89, "passing": 92, "dribbling": 96, "defending": 40, "physical": 70},
    {"name": "Kroos",   "age": 26, "position": "MF",
     "pace": 72, "shooting": 79, "passing": 93, "dribbling": 81, "defending": 72, "physical": 74},
    {"name": "Van Dijk","age": 27, "position": "DF",
     "pace": 78, "shooting": 60, "passing": 75, "dribbling": 65, "defending": 92, "physical": 90},
]

print("── Ranking ────────────────────────────────")
for i, s in enumerate(analyzer.rank(players), 1):
    tags = " ".join(s.tags) if s.tags else ""
    print(f"{i}. {s.name:<12} OVR {s.overall}  POT {s.potential}  {tags}")

print("\n── Head-to-Head: Ronaldo vs Messi ─────────")
result = analyzer.compare(players[0], players[1])
import json
print(json.dumps(result, indent=2))