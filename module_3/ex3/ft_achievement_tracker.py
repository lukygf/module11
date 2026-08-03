#!/usr/bin/python3

import random

achievements = [
    "Boss Slayer",
    "Collector Supreme",
    "Treasure Hunter",
    "World Savior",
    "Master Explorer",
    "Strategist",
    "Untouchable",
    "Speed Runner",
    "Survivor",
    "First Steps"
]

def gen_player_achievements() -> set:
    numero = random.randint(1, 10)

    conjunto = set()

    while len(conjunto) < numero:
        conjunto.add(random.choice(achievements))

    return conjunto


def achievements_tracker() -> None:
    print("=== Achievement Tracker System ===")

    Alice = gen_player_achievements()
    Bob = gen_player_achievements()
    Charlie = gen_player_achievements()
    Dylan = gen_player_achievements()

    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")

    print(f"\nAll distinct achievements: {set.union(Alice, Bob, Charlie, Dylan)}")

    print(f"\nCommon achievements: {set.intersection(Alice, Bob, Charlie, Dylan)}")

    print(f"\nOnly Alice has: {set.difference(Alice, Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {set.difference(Bob, Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {set.difference(Charlie, Bob, Alice, Dylan)}")
    print(f"Only Dylan has: {set.difference(Dylan, Bob, Charlie, Alice)}")

    print(f"\nAlice is missing: {set.difference(set(achievements), Alice)}")
    print(f"Bob is missing: {set.difference(set(achievements), Bob)}")
    print(f"Charlie is missing: {set.difference(set(achievements), Charlie)}")
    print(f"Dylan is missing: {set.difference(set(achievements), Dylan)}")


if __name__ == "__main__":
    achievements_tracker()