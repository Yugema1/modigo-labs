def top_scorers(results):
    # TODO: find the highest score, collect all players who achieved it,
    highest_score = max(score for name, score in results)
    top_scorers = []
    for players in results:
        name, score = players
        if score == highest_score:
            top_scorers.append(name)
    # and return their names as a sorted tuple
    return tuple(sorted(top_scorers))
print(top_scorers([("Zara", 50), ("Ade", 50), ("Bola", 40)]))