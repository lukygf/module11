#!/usr/bin/python3

import sys

def score_analytics() -> None:
    print("=== Player Score Analytics ===")

    scores = []

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):

            try:
                numero = int(sys.argv[i])
                scores.append(numero)

            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
        
        if len(scores) == 0:
            print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    
        else: 
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    score_analytics()