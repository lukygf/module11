#!/usr/bin/python3    

import random

players = [
    "alice",
    "bob",
    "charlie",
    "dylan"
]

actions = [
    "run",
    "eat",
    "sleep",
    "move",
    "grab",
    "release",
    "swim",
    "climb",
    "use"
]

def consume_event(lista):
    while lista:
        evento_a_eliminar = random.choice(lista)
        print(f"Got event from list: {evento_a_eliminar}")
        lista.remove(evento_a_eliminar)
        yield lista


def gen_event():
    while True:
        event = []

        event.append(random.choice(players))
        event.append(random.choice(actions))

        final = tuple(event)
        yield final 


def data_stream() -> None:
    print("=== Game Data Stream Processor ===")

    generator = gen_event()

    for i in range(0, 1000):
        evento = next(generator)
        print(f"Event {i}: Player {evento[0]} did action {evento[1]}")
    
    lista = []
    for i in range(0, 10):
        evento = next(generator)
        lista.append(evento)

    print(f"Built list of 10 events: {lista}\n")

    for evento in consume_event(lista):
        print(f"Remains in list: {lista}")


if __name__ == "__main__":
    data_stream()