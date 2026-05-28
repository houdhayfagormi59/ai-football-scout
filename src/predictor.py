"""
Match outcome predictor using scikit-learn.
"""
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report


class MatchPredictor:
    OUTCOMES = {0: "Away Win", 1: "Draw", 2: "Home Win"}

    def __init__(self):
        self.model = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, random_state=42)
        self.scaler = StandardScaler()
        self._trained = False

    def _features(self, match: dict) -> list:
        return [
            match.get("home_form", 0.5),
            match.get("away_form", 0.5),
            match.get("home_goals_avg", 1.5),
            match.get("away_goals_avg", 1.5),
            match.get("home_possession_avg", 50),
            match.get("away_possession_avg", 50),
            match.get("h2h_home_wins", 0),
            match.get("h2h_away_wins", 0),
        ]

    def train(self, data: pd.DataFrame):
        """data must have columns matching _features() keys + 'result' (0/1/2)."""
        feature_cols = [
            "home_form", "away_form", "home_goals_avg", "away_goals_avg",
            "home_possession_avg", "away_possession_avg", "h2h_home_wins", "h2h_away_wins",
        ]
        X = self.scaler.fit_transform(data[feature_cols])
        y = data["result"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        self._trained = True
        acc = accuracy_score(y_test, self.model.predict(X_test))
        print(f"Model trained — test accuracy: {acc:.3f}")
        print(classification_report(y_test, self.model.predict(X_test),
                                    target_names=list(self.OUTCOMES.values())))

    def predict(self, match: dict) -> dict:
        if not self._trained:
            raise RuntimeError("Call .train() first")
        X = self.scaler.transform([self._features(match)])
        pred = int(self.model.predict(X)[0])
        proba = self.model.predict_proba(X)[0]
        return {
            "prediction": self.OUTCOMES[pred],
            "confidence": round(float(proba[pred]) * 100, 1),
            "probabilities": {self.OUTCOMES[i]: round(float(p) * 100, 1) for i, p in enumerate(proba)},
        }

    def save(self, path="predictor.pkl"):
        joblib.dump({"model": self.model, "scaler": self.scaler, "trained": self._trained}, path)

    @classmethod
    def load(cls, path="predictor.pkl"):
        data = joblib.load(path)
        obj = cls()
        obj.model, obj.scaler, obj._trained = data["model"], data["scaler"], data["trained"]
        return obj