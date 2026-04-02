"""
Command-line runner for the Music Recommender Simulation.

Loads the song catalog, defines a sample user taste profile, runs the
recommender over all songs, and prints the ranked results with scores
and explanations. Implement the core logic in recommender.py.
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    """Load songs, score them against a sample user profile, and print ranked results."""
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Taste profile: target values for every song feature used in scoring.
    # This persona enjoys upbeat, danceable electronic/pop with high energy —
    # think workout playlist or late-night city drive.
    user_prefs = {
        "favorite_genre": "pop",          # preferred genre (string match)
        "favorite_mood":  "happy",        # preferred mood  (string match)
        "target_energy":       0.72,      # 0.0 (calm) – 1.0 (intense)
        "target_tempo_bpm":   118.0,      # beats per minute
        "target_valence":      0.88,      # 0.0 (negative) – 1.0 (positive)
        "target_danceability": 0.78,      # 0.0 (least) – 1.0 (most)
        "target_acousticness": 0.30,      # 0.0 (electronic) – 1.0 (acoustic)
        "likes_acoustic":     False,      # boolean shorthand used by Recommender
    }

    recommendations = recommend_songs(user_prefs, songs, k=len(songs))

    print("\n" + "=" * 50)
    print(f"  ALL SONGS RANKED  ({len(recommendations)} total)")
    print("=" * 50)
    for i, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"\n#{i}  {song['title']}  —  {song['artist']}")
        print(f"    Score : {score:.2f}")
        print(f"    Why   :", end="")
        reasons = [r.strip() for r in explanation.split(",")]
        for j, reason in enumerate(reasons):
            prefix = " " if j == 0 else "            "
            print(f"{prefix}{reason}")
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
