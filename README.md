# ai-football-scout

> AI-powered football player scouting and performance analysis dashboard.

![Python](https://img.shields.io/badge/python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/tensorflow-2.x-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![React](https://img.shields.io/badge/react-18-61DAFB?style=flat-square&logo=react&logoColor=black)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

## overview

A full-stack application that uses machine learning to scout football players, analyze performance data, and generate actionable insights for coaches and analysts.

## features

- player performance tracking & scoring
- AI-powered match outcome prediction
- interactive heatmaps & pass maps
- automated scouting reports (PDF export)
- real-time stats dashboard

## tech stack

| layer | tech |
|---|---|
| frontend | react 18, typescript, recharts, tailwind css |
| backend | python, fastapi, postgresql |
| ml/ai | tensorflow, scikit-learn, pandas, numpy |
| infra | docker, github actions |

## getting started

```bash
# clone the repo
git clone https://github.com/houdhayfagormi59/ai-football-scout
cd ai-football-scout

# backend
cd backend
pip install -r requirements.txt
python main.py

# frontend
cd frontend
npm install
npm run dev
```

## project structure

```
ai-football-scout/
├── backend/
│   ├── main.py
│   ├── models/
│   ├── routers/
│   └── ml/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── hooks/
│   └── package.json
├── notebooks/
│   └── player_analysis.ipynb
└── docker-compose.yml
```

## license

MIT © [houhou_59](https://github.com/houdhayfagormi59)