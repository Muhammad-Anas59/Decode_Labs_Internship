# Project 3: AI Recommendation Logic — Tech Stack Recommender

A content-based recommendation engine built as part of the DecodeLabs AI Engineering Internship (Batch 2026). Given a user's skills, it recommends the most relevant career paths/job roles using TF-IDF vectorization and cosine similarity — the same core technique used in real-world recommendation systems.

## Features

- **Content-based filtering** — matches user skills directly to job role requirements, no historical user data needed
- **TF-IDF vectorization** — weights skills by specificity/importance rather than simple keyword overlap
- **Cosine similarity scoring** — measures how closely a user's skill profile aligns with each job role, independent of profile length
- **Ranked Top-3 output** — returns the most relevant matches with a similarity percentage
- **Interactive CLI input** — enforces a minimum of 3 user-provided skills

## Tech Stack

- Python 3
- [pandas](https://pandas.pydata.org/) — dataset loading and handling
- [scikit-learn](https://scikit-learn.org/) — `TfidfVectorizer` and `cosine_similarity`

## How It Works (Pipeline)

1. **Ingestion** — user enters 3+ skills via the terminal
2. **Vectorization** — both the job roles dataset and the user's skills are converted into TF-IDF vectors in a shared vocabulary space
3. **Scoring** — cosine similarity is calculated between the user's vector and every job role's vector
4. **Sorting & Filtering** — results are ranked highest to lowest, and truncated to the Top 3 matches

## Setup

1. Navigate into the project folder:
   ```bash
   cd project-3-recommender
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   env\Scripts\activate      # Windows
   source env/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the recommender:
```bash
python main.py
```

Example session:
```
Enter your skills one at a time (minimum 3). Type 'done' when finished.

Skill 1: Python
Skill 2: Cloud Computing
Skill 3: Automation
Skill 4: done

Based on your skills ['Python', 'Cloud Computing', 'Automation'], here are your top career matches:

1. Cloud Architect — 53.2% match
2. Data Engineer — 43.4% match
3. Machine Learning Engineer — 36.8% match
```

## Dataset

`raw_skills.csv` contains 10 job roles, each mapped to a set of representative skills. This is a small, hand-curated dataset built for demonstration purposes — it can be expanded with more roles and richer skill sets to improve recommendation quality.

| role | skills |
|---|---|
| Data Scientist | Python, SQL, Machine Learning, Statistics, Data Analysis, Pandas |
| DevOps Engineer | AWS, Docker, Kubernetes, CI/CD, Automation, Linux |
| ... | ... |

## Project Structure

```
project-3-recommender/
  main.py            # loading, vectorization, similarity scoring, CLI
  raw_skills.csv      # job roles dataset
  requirements.txt    # dependencies
  README.md           # this file
```

## Notes

- This implementation uses **content-based filtering** rather than collaborative filtering, since it requires no historical user interaction data to function — matches are made purely on the intrinsic attributes (skills) of each item (job role).
- Cosine similarity was chosen over Euclidean distance because it measures the *angle* (orientation) between vectors rather than raw magnitude, making it more robust to differences in profile/skill-set length.
