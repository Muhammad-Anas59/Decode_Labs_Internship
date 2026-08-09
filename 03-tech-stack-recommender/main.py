import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_user_skills():
    """Prompts the user to enter at least 3 skills."""
    print("Enter your skills one at a time (minimum 3). Type 'done' when finished.\n")
    
    skills = []
    while True:
        skill = input(f"Skill {len(skills) + 1}: ").strip()

        if skill.lower() == "done":
            if len(skills) < 3:
                print(f"Please enter at least 3 skills before typing 'done'. ({len(skills)}/3 so far)\n")
                continue
            break

        if skill:  # ignore empty input
            skills.append(skill)

    return skills
def load_dataset(filepath):
    """Loads the job roles dataset from CSV."""
    df = pd.read_csv(filepath)
    return df

def build_vectorizer(df):
    """Fits a TF-IDF vectorizer on the job roles' skills text."""
    vectorizer = TfidfVectorizer()
    skill_vectors = vectorizer.fit_transform(df["skills"])
    return vectorizer, skill_vectors
def get_recommendations(user_skills, df, vectorizer, skill_vectors, top_n=3):
    """Matches user skills against job roles using cosine similarity."""
    user_text = ", ".join(user_skills)
    user_vector = vectorizer.transform([user_text])

    similarity_scores = cosine_similarity(user_vector, skill_vectors).flatten()

    df = df.copy()
    df["similarity"] = similarity_scores

    top_matches = df.sort_values(by="similarity", ascending=False).head(top_n)
    return top_matches[["role", "similarity"]]
if __name__ == "__main__":
    df = load_dataset("raw_skills.csv")
    vectorizer, skill_vectors = build_vectorizer(df)

    user_skills = get_user_skills()
    recommendations = get_recommendations(user_skills, df, vectorizer, skill_vectors)

    print(f"\nBased on your skills {user_skills}, here are your top career matches:\n")
    for rank, (_, row) in enumerate(recommendations.iterrows(), start=1):
        match_percent = row["similarity"] * 100
        print(f"{rank}. {row['role']} — {match_percent:.1f}% match")