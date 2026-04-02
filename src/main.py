"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Taste profile: target values for every song feature used in scoring.
    # This persona enjoys upbeat, danceable electronic/pop with high energy —
    # think workout playlist or late-night city drive.
    user_prefs = {
        "favorite_genre": "electronic",   # preferred genre (string match)
        "favorite_mood":  "energetic",    # preferred mood  (string match)
        "target_energy":       0.88,      # 0.0 (calm) – 1.0 (intense)
        "target_tempo_bpm":   135.0,      # beats per minute
        "target_valence":      0.70,      # 0.0 (negative) – 1.0 (positive)
        "target_danceability": 0.85,      # 0.0 (least) – 1.0 (most)
        "target_acousticness": 0.10,      # 0.0 (electronic) – 1.0 (acoustic)
        "likes_acoustic":     False,      # boolean shorthand used by Recommender
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
